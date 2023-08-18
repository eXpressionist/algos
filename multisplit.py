import re
'''Функция принимает строку с разделителями и массив из разделителей, выдает слова без разделителей'''

def multiple_split(string,delimeters):
    regex = re.compile(f'{"|".join(map(re.escape, delimeters))}')
    return re.split(regex, string)
