# Вопрос: что такое методы?

numbers_list = list([40, 20, 90, 11, 5])
fruits_list = list(['Apple', 'Grape', 'Banan', 'Orange'])
print("--------------------")

# Метод append() - добавляет элемент в конец списка.

print("append")
print(numbers_list)
numbers_list.append(60)
numbers_list.append("String")
print(numbers_list)
print("--------------------")

# Метод pop() - удаляет элемент из списка по его индексу (если нужно удалить последний, то вызываем без ничего)

print("pop")
print(numbers_list)
numbers_list.pop()
print(numbers_list)
print("--------------------")

# Метод insert() - добавляет элемент в список на произвольную позицию (1 аргумент - позиция, 2 аргумент - значение)

print("insert")
print(numbers_list)
numbers_list.insert(0, 0)
print(numbers_list)
numbers_list.insert(5, 10)
print(numbers_list)
print("--------------------")

# Метод remove() - удаляет первый найденный по значению элемент в списке

print("remove")
print(numbers_list)
numbers_list.remove(40)
print(numbers_list)
print("--------------------")

# Метод count() - подсчёт элементов списка по значению

print("count")
print(numbers_list)
numbers_list.append(60)
numbers_list.append(60)
numbers_list.append(60)
print(numbers_list)
print(numbers_list.count(60))
print("--------------------")

# Метод sort() - сортирует список по возрастанию значений его элементов

print("sort 1 ")
print(numbers_list)
numbers_list.sort()
print(numbers_list) # Какое преимущество нам даёт отсортированный лист, если мы хотим получить конкретное значение ?
print("--------------------")

# Вопрос: Как происходит сортировка строк?
print("sort 1 ")
print(fruits_list)
fruits_list.sort()
print(fruits_list)
print("--------------------")

# Метод reverse() - позволяет перевернуть список

print(numbers_list)
numbers_list.reverse()
print(numbers_list)
print("--------------------")

# Метод clear() - позволяет очистить список

print(numbers_list)
print(fruits_list)

numbers_list.clear()
fruits_list.clear()

print(numbers_list)
print(fruits_list)
print("--------------------")

# Вопрос: чем отличаются функции от методов?