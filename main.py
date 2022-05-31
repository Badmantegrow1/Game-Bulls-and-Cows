from mastermind_engine import put_numbers, check_the_number, is_gameover, result, count_num
print('''Игра "Быки и Коровы"\n
Правила:
Компьютер загадывает четырехзначное число, все цифры которого различны
(первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
Игрок вводит четырехзначное число c неповторяющимися цифрами,
компьютер сообщают о количестве «быков» и «коров» в названном числе
«бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
      что и в задуманном числе
«корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
      что и в задуманном числе

Например, если задумано число 3275 и названо число 1234,
получаем в названном числе одного «быка» и одну «корову».
Очевидно, что число отгадано в том случае, если имеем 4 «быка».''')
print()
put_numbers()
while True:
    number = list(input('введите 4 неповторяющихся числа:\n'))
    check_the_number(my_numbers=number)
    result()
    if is_gameover():
        count_num()
        a = input('Победа! Вы угадали все числа! Продолжить? (да/нет):\n')
        if a.lower() == 'да':
            put_numbers()
        elif a.lower() == "нет":
            break
        else:
            print('Вы ввели неверное значение!')
            break