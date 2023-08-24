from datetime import date
'''Вывод диапазона дат'''

def get_date_range(start, end):
    s = [date.fromordinal(i) for i in range(date.toordinal(start),date.toordinal(end)+1)]
    return s

'''Вывод дат в порядке неубывания по формату DD/MM/YYYY'''
dates = [date.fromisoformat(input()) for _ in range(int(input()))]

for d in sorted(dates):
    print(d.strftime('%d/%m/%Y'))

'''Проверка корректности введенной даты'''
def is_correct(day, month, year):
    try: return bool(date(year, month, day))
    except: return False

'''booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата, либо период (две даты через дефис).
date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает забронировать номер.
Функция выводит доступны ли полностью выбранные даты для бронирования'''
from datetime import datetime

def str2period(str_dates):
    period = tuple(map(lambda x: datetime.strptime(x, "%d.%m.%Y"), str_dates.split("-")))
    return period if len(period) > 1 else period * 2

def not_overlapping(period1, period2):
    return period1[1] < period2[0] or period1[0] > period2[1]

def is_available_date(booked_dates, date_for_booking):
    check_dates = str2period(date_for_booking)
    for bd in booked_dates:
        if not not_overlapping(str2period(bd), check_dates):
            return False
    return True

'''dates — список строковых дат в формате DD.MM.YYYY. Функция должна возвращать список, в котором содержатся все даты из списка dates, расположенные в порядке возрастания, а также все недостающие промежуточные даты'''
def fill_up_missing_dates(dates):
    pattern = '%d.%m.%Y'
    dates = [datetime.strptime(d, pattern) for d in dates]
    start, end = min(dates), max(dates)
    days = (end - start).days
    return [(start + timedelta(days=i)).strftime(pattern) for i in range(days + 1)]

'''Функция показывает оставшееся время до указанной даты, склоняя ответ'''
from datetime import datetime, timedelta
def choose_plural(amount, variants):
    variant = 2
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    return '{} {}'.format(amount, variants[variant])
hs = ('час', 'часа', 'часов')
ds = ('день', 'дня', 'дней')
mt = ('минута', 'минуты', 'минут')
pattern = '%d.%m.%Y %H:%M'
release = datetime.strptime('08.11.2022 12:00',pattern)
now = datetime.strptime(input(),pattern) #запрашиваем текущее время
delta = -int((now-release).total_seconds())
if delta <= 0:
    print('Релиз уже состоялся!')
else:
    days = delta // 86400
    hours = (delta - days * 86400) // 3600
    minutes = (delta - days * 86400 - hours * 3600) // 60
    result = ('До релиза осталось:')+(' '+choose_plural(days,ds) if days else "") + \
             (' и' if days and hours else "")+(' '+choose_plural(hours,hs) if hours else "") + \
             (' и' if not days and hours and minutes else "")+(' '+choose_plural(minutes,mt) if minutes and not days else "")
    print(result)

'''Все понедельники года'''
import datetime
import calendar
def get_all_mondays(year):
    mondays = []
    for month in range(1, 13):
        for week in calendar.monthcalendar(year, month):
            monday = week[0]
            if monday:
                mondays.append(date(year, month, monday))
    return mondays

'''Функция находит самую быструю по выполнению из переданных funcs для arg'''
import time

def get_the_fastest_func(funcs,arg):
    test = []
    for f in funcs:
        start = time.perf_counter()
        something = f(arg)
        end = time.perf_counter()
        test.append((end-start,f))
    x = min(test)
    return x[1]
