def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print("Я создаю декораторы! И я получил следующие аргументы:",
          decorator_arg1, decorator_arg2)

    def my_decorator(func):
        print("Я - декоратор. И ты всё же смог передать мне эти аргументы:",
              decorator_arg1, decorator_arg2)
        # Не перепутайте аргументы декораторов с аргументами функций!

        def wrapped(function_arg1, function_arg2):
            print("Я - обёртка вокруг декорируемой функции.\n"
                  "И я имею доступ ко всем аргументам\n"
                  "\t- и декоратора: {0} {1}\n"
                  "\t- и функции: {2} {3}\n"
                  "Теперь я могу передать нужные аргументы дальше"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)
        return wrapped
    return my_decorator


@decorator_maker_with_arguments("Леонард", "Шелдон")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print("Я - декорируемая функция и я знаю только о своих аргументах: {0}"
          " {1}".format(function_arg1, function_arg2))


decorated_function_with_arguments("Раджеш", "Говард")
