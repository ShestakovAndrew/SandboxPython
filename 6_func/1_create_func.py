# Функция - это именованный блок кода, к которому можно обратиться из любого места программы.
# У функции есть имя и список входных параметров, а также возвращаемое значение.

# def function_name(arg1, arg2, ...): - типичный шаблон объявления функции

# def - DEclare Function
# function_name - имя функции
# arg1, arg2, ... - список аргументов


# Пример 1 - только печатает, ничего не возвращает
def hello(name):
    print('Hello, ' + name)


hello('Andrew')


# Пример 2 - возвращает строку
def hello(name):
    return 'Hello, ' + name


print(hello('Andrew'))


# Пример 3 - возвращает bool.
# Вопрос: Как по другому можно назвать данную функцию, которая возвращает bool по 1 значению?
def isEven(x):
    return x % 2 == 0


print(isEven(7))
print(isEven(8))


# Пример 4 - несколько параметров
def sum2(a, b):
    return a + b


def sumList(lst):
    result = 0
    for number in lst:
        result += number
    return result

def lenList(lst):
    result = 0
    for _ in lst:
        result += 1
    return result


print(sum2(2, 2))
print(sumList([1, 2, 3, 4, 5, 6, 7]))
print(lenList([1, 2, 3, 4, 5, 6, 7]))






