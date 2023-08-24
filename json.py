'''Вывод всех пар ключ: значение'''
import sys
import json

data = json.loads(sys.stdin.read())

for key, value in data.items():
    if isinstance(value, list):
        print(f'{key}: {", ".join(map(str, value))}')
    else:
        print(f'{key}: {value}')

'''Объединение двух json в один (если дублируются ключи, значение из последнего)'''
import json
with open('data1.json','r',encoding='utf-8') as file1:
    with open('data2.json', 'r', encoding='utf-8') as file2:
        jsonlist1 = json.load(file1)
        jsonlist2 = json.load(file2)
        jsonlist1.update(jsonlist2)

        with open('data_merge.json','w',encoding='utf-8') as fileout:
            json.dump(jsonlist1,fileout,indent=3)

'''Находит максимальное количество ключей среди объектов, и выводит новый json файл со всеми ключами у каждого объекта'''
import json


with open('people.json', encoding='utf-8') as js:
    content = json.load(js)

keys = set()
for data in content:
    keys |= data.keys()

for data in content:
    data |= dict.fromkeys(keys - data.keys())

with open('updated_people.json', 'w') as js:
    json.dump(content, js, indent=3)

'''food_services.json, содержащий список JSON-объектов, которые представляют данные о заведениях общественного питания:
Под «заведением» будем подразумевать один JSON-объект из этого списка. У заведения имеются следующие атрибуты:

Name — название 
IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
OperatingCompany — название сети
TypeObject — вид (кафе, столовая, ресторан и т.д.)
AdmArea — административная зона
District — район
Address — полный адрес
SeatsCount — количество посадочных мест

Программа определяет все виды заведений и для каждого вида находит самое большое заведение этого вида (имеет наибольшее количество посадочных мест). Программа должна вывести все виды заведений в лексикографическом порядке, указав для каждого самое большое заведение и количество посадочных мест в нем. 
Данные о заведениях должны быть расположены каждые на отдельной строке, в следующем формате:
<вид заведения>: <название заведения>, <количество посадочных мест>'''
import json

with open('food_services.json','r',encoding='utf-8') as file_in:
    rows = json.load(file_in)
    tip = set(map(lambda x: x["TypeObject"],rows))
    for el in sorted(tip):
        s = max(filter(lambda x: x["TypeObject"]==el,rows),key=lambda x: x["SeatsCount"])
        print(s["TypeObject"],': ',s["Name"],', ',s["SeatsCount"],sep='')
    
