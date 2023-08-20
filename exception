'''Функция должна возвращать идентификационный номер, который получит поступающий в школу ученик, проверяя является ли имя строкой и состоит только из букв'''

def get_id(names, name):
    if not type(name) is str:
        raise TypeError('Имя не является строкой')
    if not name.istitle() or not name.isalpha():
        raise ValueError('Имя не является корректным')
    return len(names) + 1

'''Проверка пароля на длину, наличие малых и больших букв и цифр, если что-то не так - выдать ошибку'''
import sys

class PasswordError(Exception): ...
class LengthError(PasswordError): ...
class LetterError(PasswordError): ...
class DigitError(PasswordError): ...

def is_good_password(string:str):
    if len(string)<9:
        raise LengthError('LengthError')
    if string == string.upper() or string == string.lower():
        raise LetterError('LetterError')
    if not any(char.isdigit() for char in string):
        raise DigitError('DigitError')
    print('Success!')
    return True

for l in sys.stdin:
    try:
        if is_good_password(l.strip()):
            break
    except Exception as err:
        print(err.__class__.__name__)
