# Цикл - это многократное выполнение одного и то же действия.

# В цикл for - это цикл перебора последовательности.
# Он состоит из двух компонент: переменной (переменных) цикла и последовательности.

# Вопрос 7: почему переменная называется как переменная?
"""
Потому что она может в разные моменты времени программы иметь разные значения.
То-есть изменяться, то-есть быть переменной.
"""

# Пример 1
# item - переменная;
# 'one', 'two', 'three' - последовательность
for item in 'one', 'two', 'three':
    print(item)

# Пример 2
for letter in 'Hello world':
    print(letter)

# Пример 3, можно записать конструкцию else.
for letter in '1':
    print(letter)
else:
    print("Цикл окончен")

# Вопрос 8: последовательностью чего 'Hello world' является?
"""
Последовательностью символов
"""