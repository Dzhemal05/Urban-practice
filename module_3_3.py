#1 пункт
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
"""Выводит на консоль: 
1 строка True"""

print_params(2)
print_params(1, 2)
print_params(1, 2, 3)
# print_params(1, 2, 3, 4)

#2 пункт
values_list = [1, True, 'салам аллейкум Нияз иииу']
values_dict = {'a': '1', 'b': True, 'c': 3}
print_params(*values_list)
print_params(**values_dict)

#3 пункт
values_list_2 = [2, True]
print_params(*values_list_2, 42)