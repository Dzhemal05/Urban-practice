def calculate_structure_sum(data):
    total_sum = 0

    # Рекурсивная функция для обхода всех элементов структуры
    def recursive_sum(item):
        nonlocal total_sum

        if isinstance(item, int):
            # Если элемент - число, добавляем его к общей сумме
            total_sum += item
        elif isinstance(item, str):
            # Если элемент - строка, добавляем её длину к общей сумме
            total_sum += len(item)
        elif isinstance(item, (list, tuple, set)):
            # Если элемент - список, кортеж или множество, проходимся по каждому элементу
            for sub_item in item:
                recursive_sum(sub_item)
        elif isinstance(item, dict):
            # Если элемент - словарь, проходимся по ключам и значениям
            for key, value in item.items():
                recursive_sum(key)  # Обрабатываем ключ
                recursive_sum(value)  # Обрабатываем значение

    # Запускаем рекурсию с входным параметром
    recursive_sum(data)
    return total_sum


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99