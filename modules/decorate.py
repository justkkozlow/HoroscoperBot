from datetime import datetime, timedelta


def yesterday(callback):
    yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%d.%m.%Y')
    return yesterday_date


def today(callback):
    current_date = datetime.now().strftime('%d.%m.%Y')
    return current_date


def tommorow(callback):
    tomorrow_date = (datetime.now() + timedelta(days=1)).strftime('%d.%m.%Y')
    return tomorrow_date


def month(callback):
    month_dict = {"01": "Январь",
                  "02": "Февраль",
                  "03": "Март",
                  "04": "Апрель",
                  "05": "Май",
                  "06": "Июнь",
                  "07": "Июль",
                  "08": "Август",
                  "09": "Сентябрь",
                  "10": "Октябрь",
                  "11": "Ноябрь",
                  "12": "Декабрь"
                  }
    month_value = datetime.now().strftime('%m')
    return month_dict.get(f"{month_value}")


def year(callback):
    year = datetime.now().strftime('%Y')
    return year


choose_signs = "Выберите свой знак зодиака:"
subscribe_question = 'хотите получать ежедневный гороскоп'
