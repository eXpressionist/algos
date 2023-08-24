'''Показывает объем файлов внутри zip в сжатом и исходном виде'''
from zipfile import ZipFile
from datetime import datetime

pattern = '%Y-%m-%d %H:%M:%S'
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    for el in sorted(filter(lambda x: not x.is_dir(),info), key = lambda x: x.filename.split('/')[-1]):
        print(el.filename.split('/')[-1])
        print('  Дата модификации файла:',datetime.strftime(datetime(*el.date_time),pattern))
        print('  Объем исходного файла:',el.file_size,'байт(а)')
        print('  Объем сжатого файла:',el.compress_size,'байт(а)')
        print()

'''Показывает структуру zip файла и объем файла (округлен до ближайшей единицы)'''
from zipfile import ZipFile

def hr_size(n, k = 0):
    return f"{round(n)} {['B', 'KB', 'MB', 'GB', 'TB'][k]}" if n < 1024 else hr_size(n / 1024, k + 1)

with ZipFile('workbook.zip') as z:
    for i in z.infolist():
        p = i.filename.strip('/').split('/')
        print('  ' * (len(p) - 1) + p[-1] + ('' if i.is_dir() else ' ' + hr_size(i.file_size)))
