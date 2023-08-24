'''filename — название pickle файла, например, data.pkl. objects — список произвольных объектов. typename — тип данных. 
Функция должна создавать pickle файл с названием filename, который содержит сериализованный список только тех объектов из списка objects, тип которых равен typename.'''
import pickle

def filter_dump(filename,object,typename):
    with open(filename, 'wb') as file:     
        obj = list(filter(lambda x: type(x)==typename, object))
        pickle.dump(obj,file)
