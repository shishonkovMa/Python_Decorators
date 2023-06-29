def bread(func):
    def wrapper():
        print()
        func()
        print("<\______/>")
    return wrapper


def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper


def sandwich(food="--ветчина--"):
    print(food)


sandwich = bread(ingredients(sandwich))
sandwich()


# или теперь это можно написать иначе, используя синтаксис декораторов
print()


@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)


sandwich()
