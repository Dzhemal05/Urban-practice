def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    return inner_function()

test_function()
inner_function()

"""
При вызове внутренней функции выдается следующая ошибка:

inner_function()
    ^^^^^^^^^^^^^^
NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
"""