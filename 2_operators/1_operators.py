number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

# В языке программирования Python есть арифметические, операторы сравнения, логические операторы.

print("\nОсновные операторы:")
print("Сумма:", number1 + number2)
print("Вычитание:", number1 - number2)
print("Произведение:", number1 * number2)
print("Деление:", number1 / number2)

# Дополнительные
print("\nДополнительные операторы:")
print("Остаток от деления:", number1 % number2)
print("Деление нацело:", number1 // number2)
print("Возведение в степень:", number1 ** number2)

# Операторы сравнения Всегда возвращает True / False
print("\nОператоры сравнения:")
print("Оператор равенства:", 1 == 1, 0 == 1)
print("Оператор неравенства:", 0 != 1, 1 != 1)

print("\nОператор больше:", 1 > 1, 0 > 1, 2 > 1)
print("Оператор меньше:", 0 < 1, 1 < 1, 2 < 1)

print("\nОператор больше или равно:", 1 >= 1, 0 >= 1, 2 >= 1)
print("Оператор меньше или равно:", 0 <= 1, 1 <= 1, 2 <= 1)

# Логические операторы; Вопрос 6: какие основные вы знаете? Причём здесь диаграммы Эйлера?
"""
and, or, not
"""

print("\n(3 > 1) and (2 > 1): ", (3 > 1) and (1 > 1))
print("(3 > 1) or (2 > 1): ", (3 > 1) or (2 > 1))
print("not (2 == 0): ", not (2 == 0))
print("not ((1 == 0) or (2 == 0)): ", not ((1 == 0) or (2 == 0)))