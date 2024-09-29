def calculate_structure_sum(data):
    total_sum = 0
    def recursive_sum(item):
        nonlocal total_sum

        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, (list, tuple, set)):
            for sub_item in item:
                recursive_sum(sub_item)
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive_sum(key)  # Обрабатываем ключ
                recursive_sum(value)  # Обрабатываем значение
    recursive_sum(data)
    return total_sum
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99
