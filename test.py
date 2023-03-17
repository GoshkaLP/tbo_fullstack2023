# 1
number = input('Введите число: ')

if number.isdigit() and len(number) == 2:
    print(number[0], number[1])
else:
    print('Неверный ввод')

# 2
try:
    number = int(input('Введите число: '))
    if 10 <= number <= 99:
        print(number // 10, number % 10)
    else:
        print('Неверный ввод')
except ValueError:
    print('Неверный ввод')
