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
pile = sorted(stones, reverse=True)
goal = sum(pile)/2

history, _ = finder(pile, cont, goal, start=0, weight=0, history=0)
print(int((goal-history)*2))
