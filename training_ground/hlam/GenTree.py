while input('Строим дерево? y/n\n') == 'y':

    tree = []

    if input('Дерево новое, или возьмем пример? новое - y\n') == 'y':

        enother_branch = True

        while enother_branch:
            father = input('Father name ')
            son = input('Son name ')
            tree.append([father, son])
            enother_branch = input('Следующая ветка? y/n\n') == 'y'
    else:
        tree = [['Logan', 'Mike'], ['Logan', 'Jack'], ['Mike', 'Alexander'],
                ['Antonio', 'Hose'], ['Dima', 'Logan'], ['Alexander', 'Basil']]

    print('Задача:\n', tree)

    '''список пап'''
    fathers = []
    for i in range(len(tree)):
        fathers.append(tree[i][0])

    '''список сыновей'''
    sons = []
    for i in range(len(tree)):
        sons.append(tree[i][1])

    '''поиск суперпап'''
    superfathers = []
    for i in range(len(tree)):
        father = tree[i][0]
        if father not in sons:
            superfathers.append([father])

    '''дети суперпап'''

    for i in range(len(superfathers)):
        sons = []
        for m in range(len(tree)):
            if superfathers[i][0] == tree[m][0]:
                sons.append(tree[m][1])
                sons2 = []
                if tree[m][1] in fathers:
                    for k in range(len(tree)):
                        if tree[m][1] == tree[k][0]:
                            sons2.append(tree[k][1])
                        sons3 = []
                        if tree[k][1] in fathers:
                            for x in range(len(tree)):
                                if tree[k][1] == tree[x][0]:
                                    sons3.append(tree[x][1])
                            sons2.append(sons3)
                    sons.append(sons2)
        superfathers[i].append(sons)

    print('Решение:\n', superfathers, '\n', 'Дерево достоверно' if len(
        superfathers) == 1 else 'Дерево недостоверно')


print('До новых встреч!')
