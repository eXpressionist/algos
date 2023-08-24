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

'''Самое частое слово в введенной строке независимо от регистра'''
d = __import__('collections').Counter(input().lower().split()).most_common()
print(max(k for k, v in d if v == d[0][1]))

'''Сколько раз пользователь менял имя (таблица csv, три столбца - имя, почта и дата изменения)'''
from collections import Counter
import csv

with open('name_log.csv','r',encoding='utf-8') as file:
    lines = list(csv.reader(file))
    changes = Counter(l[1] for l in lines[1:])
    for el in sorted(changes.items()):
        print(f'{el[0]}: {el[1]}')

'''Можно ли из символов составить слово'''
from collections import Counter

def scrabble(symbols, word):
    return Counter(word.lower()) <= Counter(symbols.lower())

'''Выдает множество ключей словарей'''
from collections import ChainMap

def get_all_values(chainmap, key):
    return {d[key] for d in chainmap.maps if key in d}

'''Поиск ключа в словарях (слева направо или наоборот)'''
from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    for item in chainmap.maps if from_left else reversed(chainmap.maps):
        if key in item:
            return item[key]
    return None
