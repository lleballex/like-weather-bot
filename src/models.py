from misc import db, owm
from utils import localtime, get_date

import peewee
from pyowm.commons.exceptions import NotFoundError

from datetime import datetime


DEGREES = (
    ('celsius', '°C'),
    ('fahrenheit', '°F'),
    ('kelvin', '°K')
)

SPEED = (
    ('meters_sec', 'м/с'),
    ('miles_hour', 'mph'),
    ('knots', 'уз'),
    ('beaufort', 'по Бофарту'),
)

PRESSURE = (
    ('hPa', 'гПа'),
    ('inHg', 'inHG'),    
)

DISTANCE = (
    ('meters', 'м'),
    ('kilometers', 'км'),
    ('miles', 'mi')
)


class City(peewee.Model):
    title = peewee.CharField(unique=True)

    class Meta:
        database = db
        db_table = 'cities'

    @classmethod
    def find(cls, title):
        try:
            owm.weather_at_place(title)
        except NotFoundError:
            return None
        else:
            return cls.get_or_create(title=title.title())[0]


class User(peewee.Model):
    user_id = peewee.IntegerField(unique=True)
    cities = peewee.ManyToManyField(City)
    active_city = peewee.ForeignKeyField(City, null=True)
    degrees = peewee.CharField(choices=DEGREES, default='celsius')
    speed = peewee.CharField(choices=SPEED, default='meters_sec')
    pressure = peewee.CharField(choices=PRESSURE, default='hPa')
    distance = peewee.CharField(choices=DISTANCE, default='meters')

    class Meta:
        database = db
        db_table = 'users'

    def get_wind_from(self, deg):
        if deg < 22.5: return '⬇️'
        if deg < 67.5: return '↙️'
        if deg < 112.5: return '⬅️'
        if deg < 157.5: return '↖️'
        if deg < 202.5: return '⬆️'
        if deg < 247.5: return '↗️'
        if deg < 292.5: return '➡️'
        if deg < 337.5: return '↘️'
        return '⬇️'

    def activate_city(self, city):
        if not city in self.cities:
            self.cities.add(city)
        self.active_city = city
        self.cities = self.cities[::-1][:6]
        self.save()

    def get_degrees_label(self):
        return dict(DEGREES)[self.degrees]

    def get_speed_label(self):
        return dict(SPEED)[self.speed]

    def get_pressure_label(self):
        return dict(PRESSURE)[self.pressure]

    def get_distance_label(self):
        return dict(DISTANCE)[self.distance]

    def get_weather(self, day_change=0):
        if not self.active_city:
            return None

        if not day_change:
            data = owm.weather_at_place(self.active_city.title).weather
        else:
            forecast = owm.forecast_at_place(self.active_city.title, '3h')
            data = forecast.forecast.get(day_change*8 - 1)
            
        temp = data.temperature(self.degrees)
        temp_label = self.get_degrees_label()

        wind = data.wind(self.speed)
        wind_label = self.get_speed_label()

        press = data.barometric_pressure(self.pressure)
        press_label = self.get_pressure_label()

        visibility = data.visibility(self.distance)
        visibility_label = self.get_distance_label()

        return (f'🤘 {self.active_city.title} {get_date(days=day_change).lower()}\n\n'
                f'🌦 {int(temp["temp"])} {temp_label}, {data.detailed_status} '
                f'(ощущеатся {int(temp["feels_like"])} {temp_label})\n'
                f'🌡 Макс / мин: {int(temp["temp_max"])}° / {int(temp["temp_min"])}°\n'
                f'💨 Ветер: {wind["speed"]} {wind_label} {self.get_wind_from(wind["deg"])}\n'
                f'🤕 Давление: {press["press"]} {press_label}\n'
                f'👁 Видимость: {visibility} {visibility_label}\n'
                f'💧 Влажность: {data.humidity}%')
