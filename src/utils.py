from datetime import datetime, timedelta


MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля',
          'августа', 'сентября', 'октября', 'ноября', 'декабря']


def localtime(time=None):
    if not time:
        time = datetime.utcnow()
    return time + timedelta(hours=3)


def get_date(date=None, days=0):
    now = localtime()
    if date:
        days = int((date - now).total_seconds()) // 60 // 60 // 24

    if days < 1:
        return 'Сегодня'
    if days == 1:
        return 'Завтра'
    if days == 2:
        return 'Послезавтра'

    if not date:
        date = now + timedelta(days=days)
    return f'{date.day} {MONTHS[date.month]}'