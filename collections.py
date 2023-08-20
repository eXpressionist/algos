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
