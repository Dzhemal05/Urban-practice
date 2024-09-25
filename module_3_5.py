def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number)
    first = int(str_number[0])
    if first == 0:
        return get_multiplied_digits(str_number[1:])
    remaining_result = get_multiplied_digits(str_number[1:])
    if remaining_result == 0:
        return first

    return first * remaining_result

result = get_multiplied_digits(420)
print(result)
