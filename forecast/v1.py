from colorama import init, Fore, Back, Style

init()






def outWhite(text):
    print("\033[37m {}" .format(text))


def outTurquoise (text):
    print("\033[36m {}" .format(text))


def out_blue(text):
    print("\033[34m {}" .format(text))


def calculationOfCoefficients(choise):
    global listRate_1
    global listRate_2

    for n in range(totalAmount):
        rate_1 = totalAmount - n
        rate_2 = totalAmount - rate_1
        overallResult_1 = rate_1 * coefficient_1
        overallResult_2 = rate_2 * coefficient_2
        total_1 = overallResult_1 - totalAmount
        total_2 = overallResult_2 - totalAmount
        if overallResult_1 < totalAmount or overallResult_2 < totalAmount:
            continue

        listRate_1.append(rate_1)
        listRate_2.append(rate_2)
        listTotal_1.append(total_1)
        listTotal_2.append(total_2)
        listOverallResult_1.append(overallResult_1)
        listOverallResult_2.append(overallResult_2)
        if choise == 0:
            print('Твой выигрыш первого события -', total_1, 'р, ', 'Твой выигрыш второго события -', total_2, 'р')
            print('Итого средств первого события', overallResult_1, 'Итого средств второго события', overallResult_2, '\nСтавка на первое событие', rate_1,
                  'Ставка на второе событие', rate_2, '\n')



state_user = 0

while True:
    out_blue('\n\n-------START-------\n')
    outTurquoise('')
    coefficient_1 = float(input('Введите коэфицент на первую команду '))
    coefficient_2 = float(input('Введите коэффицент на вторую команду '))
    totalAmount = int(input('Какую сумму хотите поставить? '))


    listRate_1 = []
    listRate_2 = []
    listTotal_1, listTotal_2 = [], []
    listOverallResult_1, listOverallResult_2 = [], []




    valRate_1 = 0
    if len(listRate_1) % 2 == 0:
        val = len(listRate_1) // 2
    else:
        val = len(listRate_1) + 1 // 2

    valTotal_1 = 0
    if len(listTotal_1) % 2 == 0:
        val = len(listTotal_1) // 2
    else:
        val = len(listTotal_1) + 1 // 2

    valOverallResult_1 = 0
    if len(listOverallResult_1) % 2 == 0:
        val = len(listOverallResult_1) // 2
    else:
            val = len(listOverallResult_1) + 1 // 2


    valRate_2 = 0
    if len(listRate_2) % 2 == 0:
        val = len(listRate_2) // 2
    else:
        val = len(listRate_2) + 1 // 2

    valTotal_2 = 0
    if len(listTotal_2) % 2 == 0:
        val = len(listTotal_2) // 2
    else:
        val = len(listTotal_2) + 1 // 2

    valOverallResult_2 = 0
    if len(listOverallResult_2) % 2 == 0:
        val = len(listOverallResult_2) // 2
    else:
        val = len(listOverallResult_2) + 1 // 2




    choiceUser = int(input('Что хочешь узнать? \n'
                          '0. Вывести результат всех возможных событий \n'
                          '1. Вывести результат первой ставки \n'
                          '2. Вывести результат второй ставки \n'
                          '3. Вывести средний результат \n'
                          '4. Посмотреть все события \n'
                          'Вводить цифры '))

    calculationOfCoefficients(choiceUser)



    if choiceUser == 1:
        print('\nИтог первой ставки \n'
              'Победа первой команды: \n'
              'Ставка:', listRate_1[0], '\n'
              'Выигрыш:', listTotal_1[0], '\n'
              'Итоговый результат:', listOverallResult_1[0], '\n'
              '\nПобеда второй команды: \n'
              'Ставка:', listRate_2[0], '\n'
              'Выигрыш:', listTotal_2[0], '\n'
              'Итоговый результат:', listOverallResult_2[0], '\n'
              )

    if choiceUser == 2:
        print('\nИтог второй ставки \n'
              'Победа первой команды: \n'
              'Ставка:', listRate_1[-1], '\n'
              'Выигрыш:', listTotal_1[-1], '\n'
              'Итоговый результат:', listOverallResult_1[-1], '\n'
              '\nПобеда второй команды: \n'
              'Ставка:', listRate_2[-1], '\n'
              'Выигрыш:', listTotal_2[-1], '\n'
              'Итоговый результат:', listOverallResult_2[-1], '\n'
              )


    if choiceUser == 3:
        print('\nСредний результат: \n'
              'Победа первой команды: \n'
              'Ставка:', listRate_1[valRate_1], '\n'
              'Выигрыш:', listTotal_1[valTotal_1], '\n'
              'Итоговый результат:', listOverallResult_1[valOverallResult_1], '\n'
              '\nПобеда второй команды: \n'
              'Ставка:', listRate_2[valRate_2], '\n'
              'Выигрыш:', listTotal_2[valTotal_2], '\n'
              'Итоговый результат:', listOverallResult_2[valOverallResult_2], '\n'
              )

    if choiceUser == 4:
        print('\nАкцент на первое событие {} \n'
              'Победа первой команды: \n'
              'Ставка:', listRate_1[0], '\n'
              'Выигрыш:', listTotal_1[0], '\n'
              'Всего средств:', listOverallResult_1[0], '\n'
              '\nПобеда второй команды: \n'
              'Ставка:', listRate_2[0], '\n'
              'Выигрыш:', listTotal_2[0], '\n'
              'Всего средств:', listOverallResult_2[0], '\n'
              '\n\nАкцент на второе событие{} \n'
              'Победа первой команды: \n'
              'Ставка:', listRate_1[-1], '\n'
              'Выигрыш:', listTotal_1[-1], '\n'
              'Всего средств:', listOverallResult_1[-1], '\n'
              '\nПобеда второй команды: \n'
              'Ставка:', listRate_2[-1], '\n'
              'Выигрыш:', listTotal_2[-1], '\n'
              'Всего средств:', listOverallResult_2[-1], '\n'
              '\n\nСредний результат: \n'
              'Победа первой команды: \n'
              'Ставка:', listRate_1[valRate_1], '\n'
              'Выигрыш:', listTotal_1[valTotal_1], '\n'
              'Всего средств:', listOverallResult_1[valOverallResult_1], '\n'
              '\nПобеда второй команды: \n'
              'Ставка:', listRate_2[valRate_2], '\n'
              'Выигрыш:', listTotal_2[valTotal_2], '\n'
              'Всего средств:', listOverallResult_2[valOverallResult_2], '\n'
              )
    user_exit = int(input('Сделать еще раз ставку?\n'
                      '1.Еще раз!\n2.Выход '))
    if user_exit == 2:
        out_blue('\n\n------Bye Bye------')
        break



# Если кто-то дочитал до этого момента и понял насколько это дно в плане проектировании,
# то мои Вам сочуствия, изначально я писал код не для публики, сильно не заморачивался. Спасибо за понимание!