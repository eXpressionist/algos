'''Разбор числа на цифры'''
def print_digits(number):
    if number < 10:
        print(number)
    else:
        print_digits(number // 10)
        print(number % 10)

'''Сумма цифр'''
def sum_of_digits(number):
    if number < 10:
        return number
    return number % 10 + sum_of_digits(number // 10)

'''Последовательность трибоначчи'''
def tribonacci(n):
    cache = {1: 1, 2: 1, 3: 1}

    def trib_rec(n):
        result = cache.get(n)
        if result is None:
            result = trib_rec(n-3) + trib_rec(n - 2) + trib_rec(n - 1)
            cache[n] = result
        return result

    return trib_rec(n)

'''Перевод в двоичную СС'''
def to_binary(number):
    if number <= 1:
        return str(number)
    return to_binary(number // 2) + str(number % 2)

'''Сумма элементов вложенных списков'''
def recursive_sum(nested_lists):
    total = 0
    for elem in nested_lists:
        if isinstance(elem, list):
            total += recursive_sum(elem)
        else:
            total += elem
    return total

'''"Распрямление" вложенных списков'''
def linear(nested_l):
    lst = []
    for elem in nested_l:
        if type(elem) == list:
            lst.extend(linear(elem))
        else:
            lst.append(elem)
    return lst

'''Функция должна выводить все пары ключ-значение словаря nested_dicts, а также значения всех его дочерних словарей. При выводе значений дочерних словарей необходимо перечислять имена всех ключей, начиная с верхнего уровня, разделяя их точками.'''
def dict_travel(data, parent_key=''):
    for key, value in sorted(data.items()):
        key = f'{parent_key}.{key}' if parent_key else key
        if isinstance(value, dict):
            dict_travel(value, key)
        else:
            print(f'{key}: {value}')
