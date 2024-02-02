# Выполнение цикла можно прерывать с помощью оператора break

i = 0
while True:  # бесконечный цикл
    i += 1
    print(i)
    if i == 7:  # если i равен 7, то вызываем оператор break
        break  # оператор break прерывает выполнение цикла

# Вопрос 12: Что будет если у нас есть 3 вложенных while и вызвать оператор break:
while True:  # бесконечный цикл
    print('first')
    while True:
        print('second')
        while True:
            print('third')
            break

