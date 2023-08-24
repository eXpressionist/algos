'''В первом столбце записано измененное имя пользователя, во втором — адрес электронной почты, в третьем — дата и время изменения. При этом email пользователь менять не может, только имя:
Код отбирает из файла name_log.csv только самые свежие записи для каждого пользователя и записывает их в файл new_name_log.csv. В файле new_name_log.csv первой строкой должны быть заголовки столбцов такие же, как в файле name_log.csv. 
Логи в итоговом файле должны быть расположены в лексикографическом порядке названий электронных ящиков пользователей.'''
import csv
from datetime import datetime

with open('name_log.csv', encoding='UTF-8') as f:
	header, *rows = csv.reader(f)

d = {i[1]:i for i in sorted(rows, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))}

with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as f:
	w = csv.writer(f)
	w.writerow(header)
	w.writerows(sorted(d.values(), key=lambda x: x[1]))

'''Функция принимает filename — название csv файла, каждая строка файла содержит три значения через запятую, а именно имя объекта, свойство этого объекта, значение свойства; все объекты имеют равные свойства и в равных количествах
id_name — общее название для объектов
Функция должна привести содержимое файла в привычный CSV формат, сгруппировав строки по первому столбцу и назвав первый столбец id_name. Полученный результат функция должна записать в файл condensed.csv.'''
import csv

def condense_csv(filename, id_name):
    with open(filename, encoding='utf-8') as file:
        objects = {}
        for obj, attr, value in csv.reader(file):
            if obj not in objects:
                objects[obj] = {id_name: obj}
            objects[obj][attr] = value
    
    with open('condensed.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=objects[obj])
        writer.writeheader()
        writer.writerows(objects.values())

'''Lоступен файл prices.csv, который содержит информацию о ценах продуктов в различных магазинах. В первом столбце записано название магазина, а в последующих — цена на соответствующий товар в этом магазине:
Магазин;Творог;Гречка;Рис;Бородинский хлеб;Яблоки;Пельмени;Овсяное печенье;Спагетти;Печеная фасоль;Мороженое;Фарш;Вареники;Картофель;Батончик
Пятерочка;69;133;129;83;141;90;72;123;149;89;88;106;54;84
Магнит;102;87;95;75;109;112;97;82;101;134;69;61;141;79
...
Программа определяет и выводит самый дешевый продукт и название магазина, в котором он продается, в следующем формате:
<название продукта>: <название магазина>'''
import csv

prices = []
with open('prices.csv', encoding='utf-8') as infile:
    reader = csv.reader(infile, delimiter=";")
    products = reader.__next__()[1:]    # Отбрасываем строку "Магазин"
    for shop, *price_list in reader:
        prices.extend(map(lambda price, product: (int(price), product, shop), price_list, products))

print("{1}: {2}".format(*min(prices)))
