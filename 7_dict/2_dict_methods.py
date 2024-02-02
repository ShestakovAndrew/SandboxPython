student = dict({'name': 'Andrew', 'age': 22})
print(student)
print("--------------------")

# Метод get() - возвращает значение по указанному ключу. Если указанного ключа не существует, метод вернёт None.

print(student.get('name'))
print(student.get('age'))
print(student.get('lastname'))
print("--------------------")

# Метод keys() - возвращает специальную коллекцию ключей в словаре dict_keys

print(student.keys())
print(list(student.keys()))
print("--------------------")

# Метод values() - возвращает специальную коллекцию значений в словаре dict_values

print(student.values())
print(list(student.values()))
print("--------------------")

# Метод pop() - удаляет ключ и возвращает соответствующее ему значение.

print(student)
deletedAge = student.pop("age")
print(deletedAge)
print(student)
print("--------------------")