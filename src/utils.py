from datetime import datetime, timedelta


MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля',
          'августа', 'сентября', 'октября', 'ноября', 'декабря']


def localtime(time=None):
    if not time:
        time = datetime.utcnow()
    return time + timedelta(hours=3)


def get_date(day_change):
    if day_change < 1:
        return 'Сегодня'
    if day_change == 1:
        return 'Завтра'
    if day_change == 2:
        return 'Послезавтра'
    else:
        date = localtime() + timedelta(days=day_change)
        return f'{date.day} {MONTHS[date.month]}'