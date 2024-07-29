# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и
# проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#    - Тип объекта.
#    - Атрибуты объекта.
#    - Методы объекта.
#    - Модуль, к которому объект принадлежит.
#    - Другие интересные свойства объекта, учитывая его тип (по желанию).
##
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
#
# Вывод на консоль:
# {'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [], 'module': '__main__'}


import inspect
import sys


def introspection_info(obj):
    dict_ = {}
    attrbbutes = []
    methods = []
    t = type(obj)

    for atr in dir(obj):
        if atr.startswith('__'):
            attrbbutes.append(atr)
        else:
            methods.append(atr)
    mod_ = inspect.getmodule(introspection_info)
    name_modul = mod_.__name__
    size_ = sys.getsizeof(obj)
    
    dict_.update({'type': t, 'attributes': attrbbutes, 'methods': methods, 'module': name_modul, 'Вес объекта в байтах': size_})
    return dict_

number_info = introspection_info(42)
print('Интроспекция числа')
print(number_info)
print()
print('Интроспекция строки')
string_info = introspection_info('Hello')
print(string_info)

