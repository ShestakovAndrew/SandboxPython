# Функция range().
# Функция range() возвращает диапазон (последовательность) целых чисел.

# range() с одним аргументом
print('range(2) -> 0, 1')
for x in range(2):
    print(x, end=" ")

print('\n\nrange(5) -> 0, 1, 2, 3, 4')
for x in range(5):
    print(x, end=" ")

# Примеры функции range() с двумя аргументами:
print('\n\nrange(2, 5) -> 2, 3, 4')
for x in range(2, 5):
    print(x, end=" ")

# Примеры функции range() с тремя аргументами:
print('\n\nrange(0, 10, 2) -> 0, 2, 4, 6, 8')
for x in range(0, 10, 2):
    print(x, end=" ")

print('\n\nrange(1, 10, 2) -> 1, 3, 5, 7, 9')
for x in range(1, 10, 2):
    print(x, end=" ")
print("\n")


# Пример комбинации if и for
for month in range(1, 16):
    if (month <= 2) or (month == 12):
        print('Сейчас зима')
    elif (month <= 5) and (month >= 3):
        print('Сейчас весна')
    elif (month <= 8) and (month >= 6):
        print('Сейчас лето')
    elif (month <= 11) and (month >= 9):
        print('Сейчас осень')
    else:
        print('Такого месяца нет.')
