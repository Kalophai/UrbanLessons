def test_function(*args):
    def inner_function(x):
        print(x)

    inner_function("Я в области видимости функции test_function")

test_function()