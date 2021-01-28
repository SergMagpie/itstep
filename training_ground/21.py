while input('Поиграем в очко? y/n\n') == 'y':

    karty = {6:'six',7:'seven',8:'eith',9:'nine',10:'then',2:'jock',3:'quin',4:'king',11:'ase'}

    koloda = []

    for i_masty in ('♠','♣','♥','♦'):
            for i_karty in karty.keys():
                i=(i_karty, karty.get(i_karty), i_masty)
                koloda.append(i)
    '''
    создаем колоду {6:'six',7:'seven',8:'eith',9:'nine',10:'then',2:'jock',3:'quin',4:'king',11:'ase'}
            {6:'six♠',7:'seven♠',8:'eith♠',9:'nine♠',10:'then♠',2:'jock♠',3:'quin♠',4:'king♠',11:'ase♠'}
            {6:'six♣',7:'seven♣',8:'eith♣',9:'nine♣',10:'then♣',2:'jock♣',3:'quin♣',4:'king♣',11:'ase♣'}
            {6:'six♥',7:'seven♥',8:'eith♥',9:'nine♥',10:'then♥',2:'jock♥',3:'quin♥',4:'king♥',11:'ase♥'}
            {6:'six♦',7:'seven♦',8:'eith♦',9:'nine♦',10:'then♦',2:'jock♦',3:'quin♦',4:'king♦',11:'ase♦'})
            '''
    import random
    random.shuffle(koloda)

    choiceM = input('Махлевать будем? y/n\n') == 'y'
    if choiceM:
        print('Вот Вам колода: ',koloda)

    count = 0
    countK = 0
    comp_v_igre = True

    while True:
        choice = input('Будете брать карту? y/n\n')
        if choice == 'y':
            current = koloda.pop()
            print('Вам попалась ', current[1],current[2])
            count += current[0]

            # комп берет карту

            if countK + koloda[koloda.__len__()-1][0] < 22 and comp_v_igre:
                countK += koloda.pop()[0]
                if countK == 21 and count == 21:
                    print('У нас ничья!')
                    print('У вас %d очков, у меня %d очков.' % (count, countK))
                    break
                elif countK == 21 and count < 21:
                    print('Я победил!')
                    print('У вас %d очков, у меня %d очков.' % (count, countK))
                    break
                if choiceM:
                    print('Я тоже взял карту, у меня %d очков' %countK)
                else:
                    print('Я тоже взял карту')
            else:  # комп карту больше не берет
                comp_v_igre = False

            if count > 21:
                print('Извините, но вы проиграли')
                print('У вас %d очков, у меня %d очков.' % (count, countK))
                break
            elif count == 21:
                print('Поздравляю, вы набрали 21!')
                print('У вас %d очков, у меня %d очков.' % (count, countK))
                break
            else:
                print('У вас %d очков.' %count)
        elif choice == 'n':
            while comp_v_igre:
                if countK + koloda[koloda.__len__()-1][0] < 22:
                    countK += koloda.pop()[0]
                    if choiceM:
                        print('Я взял карту, у меня %d очков' % countK)
                    else:
                        print('Я взял карту')
                else:  # комп карту больше не берет
                    comp_v_igre = False

            if count > countK:
                print('Поздравляю!\nВы победили!')
            elif count < countK:
                print('Вы проиграли')
            else:
                print('У нас ничья!')
            print('У вас %d очков, у меня %d очков.' % (count, countK))
            break

print('До новых встреч!')

