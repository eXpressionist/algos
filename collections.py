'''Разбираем csv формата Фамилия_Имя_Дата_Время, сортируем по дате и времени'''
from collections import namedtuple
import csv
from datetime import datetime

pattern = '%d.%m.%Y %H:%M'
Friend = namedtuple('Friend', ['surname', 'name', 'meet_date', 'meet_time'])
with open('meetings.csv', 'r', encoding='utf-8') as file:
    lines = list(csv.reader(file))
    friends = [Friend(*line) for line in lines[1:]]
    print(*map(lambda x: x.surname + ' ' + x.name, \
               sorted(friends, key=lambda x: datetime.strptime(x.meet_date + ' '+x.meet_time,pattern))),sep='\n')

'''dict_of_lists — словарь, в котором ключом является число или строка, а значением — список чисел или строк. Делаем новый словарь, в котором значениям из списка соответствует список ключей'''
from collections import defaultdict

def flip_dict(data):
    fliped_data = defaultdict(list)
    for key, values in data.items():
        for value in values:
            fliped_data[value].append(key)
    return fliped_data


'''Сортирует словарь ordered_dict: по ключам, если by_values имеет значение False, по значениям, если by_values имеет значение True'''
from collections import OrderedDict

def custom_sort(ord_dict,by_values=False):
    if not by_values:
        for key in sorted(ord_dict):
            ord_dict.move_to_end(key)
    else:
        for key,value in sorted(ord_dict.items(),key=lambda x: x[1]):
            ord_dict.move_to_end(key)

'''Количество уникальных букв в тексте'''
from collections import Counter

def countletter(file):
    with open(file, encoding='utf-8') as txt_file:
    c = Counter()
    for line in txt_file:
        letters = [symbol.lower() for symbol in line if symbol.isalpha()]
        c.update(letters)
    [print(f'{key}: {value}') for key, value in sorted(c.items())]

