min_limit = 0
max_limit = 10
count = 3
while count > 0:
    print('Попытка ' + str(count))
    count -= 1
    num = float(input(f'Введите число между {min_limit} и {max_limit}:'))
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
else:
    print('Исчерпаны все попытки. Сожалею.')
    quit()
print(f'Было введено число {num}.')
