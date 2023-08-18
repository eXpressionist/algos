'''Является ли объект итерируемым'''
def is_iterable(obj):
    return '__iter__' in dir(obj)
'''Является ли объект итератором'''
def is_iterator(obj):
    return hasattr(obj, '__next__')

'''Функция возвращает кортеж из минимального и максимального в итераторе за 1 проход'''
def get_min_max(iterable):
    iterable = iter(iterable)
    try:
        smallest = largest = next(iterable)
    except:
        return None
    for elem in iterable:
        if elem < smallest:
            smallest = elem
        if elem > largest:
            largest = elem
    return smallest, largest

'''Итератор, порождающий степени числа от 0'''
class PowerOf:
    def __init__(self, number):
        self.cache = 1
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        value =  self.cache
        self.cache *= self.number
        return value

'''Итератор, порождающий пары из словаря (ключ, значение)'''
class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.keys = iter(data)

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.keys)
        return key, self.data[key]

'''Итератор порождает колоду карт'''
class CardDeck:
    def __init__(self):
        self.index = -1
        self.suit = ("пик", "треф", "бубен", "червей")
        self.rank = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index > 51:
            raise StopIteration
        return f'{self.rank[self.index % 13]} {self.suit[(self.index // 13) % 4]}'

'''Итератор, генерирующий арифметическую последовательность целых или вещ.чисел'''
class Xrange:
    def __init__(self, start, end, step=1):
        self.step = step
        self.end = end
        self.start = start - step


    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start >= self.end and self.step > 0:
            raise StopIteration
        if self.start <= self.end and self.step < 0:
            raise StopIteration
        return self.start
