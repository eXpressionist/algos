'''Функция должна возвращать единственное число — количество объектов из списка objects, которые принадлежат типу typeinfo или одному из типов, если был передан кортеж'''
def custom_isinstance(objects, typeinfo):
    return sum(isinstance(i, typeinfo) for i in objects)

'''Функция находит сумму наибольшего арифметического выражения из введенных строк'''
from math import inf
from sys import stdin

def find_max_str()
    maximum = -inf
    for exp in stdin:
        sexp = eval(exp)
        if sexp >= maximum:
            maximum = sexp
    return(maximum)

'''Фуннкция находит минимальное и максимальное значение указанной функции на заданном отрезке'''
def minmax(func,a,b):
    mn = float('inf')
    mx = float('-inf')
    for i in range(int(a),int(b)+1):
        tmp = eval(func.replace('x', f'({i})'))
        if tmp > mx:
            mx = tmp
        if tmp < mn:
            mn = tmp
    print(f'Минимальное значение функции {func} на отрезке [{a}; {b}] равно {mn}')
    print(f'Максимальное значение функции {func} на отрезке [{a}; {b}] равно {mx}')

'''Функция вычисляет x^2+1 для заданного x, пользуясь доп.атрибутами функции'''
def polynom(x):
    polynom.__dict__.setdefault('values', set())
    value = x**2 + 1
    polynom.values.add(value)
    return value

'''n-й член последовательность Фибоначии'''
d = {1: 1, 2: 1}
fib = lambda x: d[x] if x in d else d.setdefault(x, fib(x - 1) + fib(x - 2))

'''Фибоначчи с пользовательскими атрибутами'''
def fib(num):
    if num < 2:
        return num
    if num not in fib.__dict__:
        fib.__dict__[num] = fib(num - 1) + fib(num - 2)
    return fib.__dict__[num]

'''Возвращает функцию, которая принимает произвольное количество именованных аргументов и возвращает url адрес, объединенный со строкой запроса, сформированной из переданных аргументов. При вызове без аргументов она должна возвращать исходный url адрес без изменений.'''
def sourcetemplate(url):
    def addparams(**kwargs):
        s = ''
        if kwargs!={}:
            s='?'+'&'.join([str(kw[0])+'='+str(kw[1]) for kw in sorted(kwargs.items())])
        return url+s
    return addparams
