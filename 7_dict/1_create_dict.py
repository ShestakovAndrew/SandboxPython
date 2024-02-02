# Словарь — неупорядоченная структура данных, которая позволяет хранить пары «ключ — значение».

# Вопрос: Что значит неупорядоченная?
"""
Неупорядоченная - значит значения в памяти компьютера хранятся в разных местах
"""

# Создание 1
student_1 = {'name': 'Andrew', 'age': 22}
print(student_1)

# Создание 2
student_2 = dict(name='Tol9', age=21)
print(student_2)

# Сравнение
print(student_1 == student_2)
print("----------------")

# Для получения значения конкретного ключа используются []
print(student_1['name'])
print(student_2['name'])
print("----------------")

# Обновление существующих значений:
print(student_1)
student_1['name'] = 'No Andrew'
print(student_1)
print("----------------")

# Удаление записи по ключу:
print(student_1)
del student_1['name']
print(student_1)
print("----------------")



