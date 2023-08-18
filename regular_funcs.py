regex = r'\+7\d{10}|\+7\(\d{3}\)\d{7}|\+7\(\d{3}\)-\d{3}-\d\d-\d\d|\+7 \d{3} \d{3} \d\d \d\d' #телефон с +7 в разных форматах
regex = r'([01]\d|2[0-3]):[0-5]\d' #время в 24ч формате
regex = r'\b([A-Za-z]+)\s+\b\b\1\b' #слова, написанные дважды подряд

import re
'''Функция принимает строку с разделителями и массив из разделителей, выдает слова без разделителей'''
def multiple_split(string,delimeters):
    regex = re.compile(f'{"|".join(map(re.escape, delimeters))}')
    return re.split(regex, string)

'''Функция удаляет лишние пробелы в строке'''
def normalize_whitespace(string):
    return re.sub(r'\s+', ' ', string)

'''Функция печатает все ссылки и их описания (html)'''
def html_href(text):
    pattern = r'<a href="(.+)">(.+)</a>'

    for address, pointer in re.findall(pattern, text):
        print(f'{address}, {pointer}')

'''Функция находит теги и их атрибуты (html)'''
def find_html_tags(data):
    # Регулярное выражение для поиска тегов и их атрибутов
    tag_pattern = re.compile(r'<(\w+)(\s+[^>]*)?>')
    attr_pattern = re.compile(r'(\S+)="[^"]*"')

    tags = {}

    # Поиск всех тегов и их атрибутов
    for match in tag_pattern.finditer(data):
        tag_name = match.group(1)
        attrs = match.group(2)
        if tag_name not in tags:
            tags[tag_name] = set()
        if attrs:
            attrs_list = [m.group(1) for m in attr_pattern.finditer(attrs)]
            tags[tag_name].update(attrs_list)

    # Сортировка тегов и их атрибутов
    for tag, attrs in sorted(tags.items()):
        if attrs:
            print(f'{tag}: {", ".join(sorted(attrs))}')
        else:
            print(f'{tag}:')
