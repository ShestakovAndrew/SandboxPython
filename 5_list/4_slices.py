#Срезом называется некоторая подпоследовательность.
#Принцип действия срезов очень прост: мы "отрезаем" кусок от исходной последовательности (то-есть итерируемого) элемента,
#не меняя её при этом.

fruits = list(['Apple', 'Grape', 'Peach', 'Banan', 'Orange'])
print(fruits)

fruits_slice_v1 = fruits[0:2]
print(fruits_slice_v1)

fruits_slice_v2 = fruits[:3]
print(fruits_slice_v2)

fruits_slice_v3 = fruits[:]
print(fruits_slice_v3)

fruits_slice_v4 = fruits[::2]
print(fruits_slice_v4)

fruits_slice_v5 = fruits[::-1]
print(fruits_slice_v5)

fruits_slice_v6 = fruits[2:5:-1]
print(fruits_slice_v6)  #Почему здесь выводит пуской список?

fruits_slice_v6 = fruits[5:2:-1]
print(fruits_slice_v6)