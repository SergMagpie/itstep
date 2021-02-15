def finder(pile, cont, goal, start, weight, history):
    if pile[start] + weight == goal or history == goal:
        return goal, True
    elif pile[start] + weight < goal:
        weight += pile[start]
        base = True
    else:
        base = False

    if start == cont - 1:
        if weight > history:
            history = weight
#backing
        
    else:
        history, last_base = finder(pile, cont, goal, start+1, weight,
                                    history)
        if history == goal:
            return goal, base
        elif base and not last_base:
            base = False
            history, last_base = finder(pile, cont, goal, start+1,
                                        weight - pile[start],
                                        history)



    return history, base

from sys import stdin

cont, *stones = list(map(int,stdin.read().split()))
#cont = 20
#stones=[23416, 96577, 30371, 28914, 72502, 54875, 60542, 88126, 94719, 48998, 22536, 91681, 94437, 69805, 27082, 11177, 76937, 70229, 4410, 87610]
#adding a bunch of stones
pile = sorted(stones, reverse=True)
#weighing half of the pile
goal = sum(pile)/2

history, _ = finder(pile, cont, goal, start=0, weight=0, history=0)

#make a bucket with stones
#rows = list(range(cont))
#columns = list(range(cont))
#weights = []
#bucket = 0
#result = None
#checking the largest stone
#if pile[0] > half_pile:
#    weights.append(pile[0] - half_pile)
#trim end of list
#while result == None:
#    if bucket+pile[columns[-1]] <= half_pile:
#        bucket += pile[columns.pop()]
#        if bucket == half_pile:
#            result = 0
#    else:
#        weights.append(half_pile-bucket)
#        break
##search for results
#if result == None:
#    for trying in columns:
#        print('trying')
#        bucket = 0
#        for stone in rows[trying:]:
#            print('rows',bucket,pile[stone])
#            if bucket+pile[stone] <= half_pile:
#                bucket += pile[stone]
#                if bucket == half_pile:
#                    result = 0
#                    break
#                #
'''
            else:
                for next_stone in rows[stone+1:]:
                    print('next',bucket,pile[next_stone])
                    if bucket+pile[next_stone] <= half_pile:
                        bucket += pile[next_stone]
                        if bucket == half_pile:
                            result = 0
                            break
                        else:
                            print('next weight', half_pile-bucket,
                                  bucket, stone)
                            weights.append(half_pile-bucket)
                            bucket = 0
                            
                if stone > rows[trying:][0]+1:
                    
                    print('rows weight', half_pile-bucket)
                    weights.append(half_pile-bucket)
                    bucket -= pile[stone-1]
                else:
                    bucket = 0

if result == None:
    result = int(min(weights)*2)
    
print(result)
print('cont', cont, 'stones', stones, 'pile', pile, 'half_pile', half_pile,
      'rows', rows, 'columns', columns, 'bucket', bucket, 'weights', weights,
      'result', result, sep='\n')'''
print(int((goal-history)*2))
