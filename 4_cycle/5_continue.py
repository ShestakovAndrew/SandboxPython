# Оператор continue начинает повторение цикла заново.

i = 0
while i < 5:
    i += 1
    if i % 2 == 1:  # если значение i нечетно, то вызываем оператор continue
        continue  # оператор continue начинает повторение цикла заново, запуская следующую итерацию
    print(i)  # в случае вызова continue число не печатается

