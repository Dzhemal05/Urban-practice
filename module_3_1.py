calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    tup = (len(string), string.upper(), string.lower())
    return tup
print(string_info('Костя'))

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower

print(is_contains('MB', ['mmmmm', 'aaaaa', 'MB']))
print(calls)