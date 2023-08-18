'''Генератор карточной колоды с заданной масти'''
def card_deck(suit: str):
    suits = ['пик', 'треф', 'бубен', 'червей']
    face_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    suits.remove(suit)
    while True:
        for suit_ in suits:
            for face_value in face_values:
                yield f'{face_value} {suit_}'

'''Достаточно быстрый генератор палиндромов'''
from string import digits

def palindromes():
    def pali(n):    # Внутренний генератор "строковых" палиндромов длиной n
        if n == 1:
            yield from digits
        elif n == 2:
            yield from (d * 2 for d in digits)
        else:       # Рекурсивный случай - "оборачиваем" одинаковыми цифрами "внутренние палиндромы"
            yield from (f"{d}{p}{d}" for d in digits for p in pali(n - 2))

    i = 0
    while True:
        i += 1
        for x in pali(i):    # Получаем все значения из внутреннего генератора
            if x[0] != "0":  # Если значение начинается с "0", оно недопустимо
                yield int(x)

'''Генератор, "распрамляющий" вложенные списки'''
def flatten(nested_list):
    nested_list.reverse()
    while nested_list :
        i = nested_list.pop()
        if isinstance(i, list):
            nested_list.extend(i[::-1])
        else:
            yield i
          
'''Генераторная функция, отображающая все первые элементы итераторов, затем все вторые и т.д.'''
def interleave(*args):
    for iterable in zip(*args):
        yield from iterable

'''Генератор, отображающий все даты в текущем году'''
from datetime import date, timedelta

def years_days(year: int):
    start = date(year, 1, 1)
    while start.year == year:
        yield start
        start += timedelta(days=1)
      
'''Генератор порождающий последовательность элементов итерируемого объекта iterable до тех пор, пока не будет достигнут элемент, равный obj'''
def stop_on(iterable, obj):
    it = iter(iterable)
    return iter(it.__next__, obj)
