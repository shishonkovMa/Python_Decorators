def my_first_decorator(some_function):

    def inner_function():
        print('до функции')
        some_function()
        print('после функции')

    return inner_function


def function_0():
    print('я первая функция')


function_0 = my_first_decorator(function_0)
function_0()

# или теперь можно написать иначе
print()


@my_first_decorator
def function_0():
    print('я вторая функция')


function_0()
