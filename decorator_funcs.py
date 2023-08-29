'''Возвращает кортеж (значение, сообщение об успешном выполнении) либо (None, сообщение об ошибке)'''
def exception_decorator(func):
    def wrapper(*args, **kargv):
        try:
            res, msg = func(*args, **kargv), 'Функция выполнилась без ошибок'
        except:
            res, msg = None, "При вызове функции произошла ошибка"
        finally:
            return res, msg        
        
    return wrapper

'''Проверяет, что все значения в качестве аргументов - положительные целые числа, иначе возбуждает Value Error'''
def takes_positive(func):
    def wrapper(*args,**kwargs):
        if not all([isinstance(a,int) for a in args]+[isinstance(kw,int) for kw in kwargs.values()]):
            raise TypeError
        elif not all([a>0 for a in args]+[kw>0 for kw in kwargs.values()]):
            raise ValueError
        return func(*args,**kwargs)
    return wrapper

'''Выводит отладочное сообщение
TRACE: вызов <имя функции>() с аргументами: <кортеж позиционных аргументов>, <словарь именованных аргументов>
TRACE: возвращаемое значение <имя функции>(): <возвращаемое значение>'''
def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(func(*args, **kwargs))}')
        return value
    return wrapper

'''Обрамляет возвращаемое значение декорируемой функции в HTML-тег tag'''
def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = '<'+tag+'>'+func(*args, **kwargs)+'</'+tag+'>'
            return value
        return wrapper
    return decorator

'''Выполняет функцию times раз'''
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                val = func(*args, **kwargs)
            return val
        return wrapper        
    return decorator

'''Принимает произвольное количество позиционных аргументов @ignore_exception(ZeroDivisionError, TypeError, ValueError) — типов исключений, и выводит текст: Исключение <тип исключения> обработано
если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов. Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.'''
def ignore_exception(*exceptions):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                print(f"Исключение {type(e).__name__} обработано")
        return wrapper
    return decorator

'''Визуализирует выполнение декорируемой функции, в том числе и рекурсивной. Декоратор должен отображать все рекурсивные вызовы и возвращаемые значения, полученные при этих вызовах, причем рекурсивные вызовы, выполняемые в глубину, должны отделяться друг от друга четырьмя пробелами.'''
import functools
def recviz(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        wrapper.count += 1
        print(f'{wrapper.count*"    "}-> {func.__name__}(',end='')
        print(', '.join(list(map(repr, args)) +
              [f'{k}={repr(v)}' for k, v in kwargs.items()]),end=')\n')
        f1 = func(*args,**kwargs)
        print(f'{wrapper.count*"    "}<- {repr(f1)}')
        wrapper.count -= 1
        return f1
    wrapper.count = -1
    return wrapper
