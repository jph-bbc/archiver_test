# подключение функций аrchiver, unpacker из модуля functions
from functions import аrchiver, unpacker

# Переменной compressed_string присваивается значение результата выполнения функции archiver,
# чтение строки происходит с клавиатуры
compressed_string = аrchiver(input('Введите строку для сжатия: '))
# Обработка исключений
if compressed_string == 'Входной текст должен быть строкой' or compressed_string == 'Введена пустая строка':
    print(compressed_string)
else:
    # Вывод на экран значения compressed_string
    print('Сжатая строка:            ', compressed_string)
    # Переменной uncompressed_string присваивается значение результата выполнения функции unpacker,
    # в которую прередается переменная compressed_string
    uncompressed_string = unpacker(compressed_string)
    # Вывод на экран значения uncompressed_string
    print('Распакованная строка:     ', uncompressed_string)
