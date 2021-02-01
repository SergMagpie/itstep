# Import library tkinter
from tkinter import *
import random
play_ground = {'b7': '7', 'b8': '8', 'b9': '9', 'b4': '4',
               'b5': '5', 'b6': '6', 'b1': '1', 'b2': '2', 'b3': '3'}

# Check winners


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

# Read play_ground


def see_board():
    return [b7['text'], b8['text'], b9['text'], b4['text'],
            b5['text'], b6['text'], b1['text'], b2['text'], b3['text']]


def set_board(board):
    b7['text'], b8['text'], b9['text'], b4['text'], b5['text'], b6['text'], \
    b1['text'], b2['text'], b3['text'] = board


def comp_turn():
    
    board = see_board()
    if check_win(board) == 'X':
        label['text'] = 'You win!'
    else:
        # Comp_turn
        
        if board[4] == '5':
            board[4] = 'O'
        else:
            # Тут нужно подумать над механизмом выбора хода, но я спать!
            a = []
            for i in board:
                if i.isdigit():
                    a.append(i)
                if a:
                    turn = random.choice(a)
            adr_item = board.index(turn)
            board[adr_item] = 'O'

    
    set_board(board)
    if check_win(board) == 'O':
        label['text'] = 'Computer win!'


# handling button presses
def klickb7():
    if b7['text'] == '7':
        b7['text'] = 'X'
        comp_turn()


def klickb8():
    if b8['text'] == '8':
        b8['text'] = 'X'
        comp_turn()


def klickb9():
    if b9['text'] == '9':
        b9['text'] = 'X'
        comp_turn()


def klickb4():
    if b4['text'] == '4':
        b4['text'] = 'X'
        comp_turn()


def klickb5():
    if b5['text'] == '5':
        b5['text'] = 'X'
        comp_turn()


def klickb6():
    if b6['text'] == '6':
        b6['text'] = 'X'
        comp_turn()


def klickb1():
    if b1['text'] == '1':
        b1['text'] = 'X'
        comp_turn()


def klickb2():
    if b2['text'] == '2':
        b2['text'] = 'X'
        comp_turn()


def klickb3():
    if b3['text'] == '3':
        b3['text'] = 'X'
        comp_turn()


def klicklb():
    new_play_ground()

# Create new play ground


def new_play_ground():
    b7['text'] = '7'
    b8['text'] = '8'
    b9['text'] = '9'
    b4['text'] = '4'
    b5['text'] = '5'
    b6['text'] = '6'
    b1['text'] = '1'
    b2['text'] = '2'
    b3['text'] = '3'
    label['text'] = "Your turn"


# Create object window
root = Tk()

# Create buttons
b7 = Button(text="7", command=klickb7)
b7.grid(row=0, column=0, sticky=NSEW)
b8 = Button(text="8", command=klickb8)
b8.grid(row=0, column=1, sticky=NSEW)
b9 = Button(text="9", command=klickb9)
b9.grid(row=0, column=2, sticky=NSEW)
b4 = Button(text="4", command=klickb4)
b4.grid(row=1, column=0, sticky=NSEW)
b5 = Button(text="5", command=klickb5)
b5.grid(row=1, column=1, sticky=NSEW)
b6 = Button(text="6", command=klickb6)
b6.grid(row=1, column=2, sticky=NSEW)
b1 = Button(text="1", command=klickb1)
b1.grid(row=2, column=0, sticky=NSEW)
b2 = Button(text="2", command=klickb2)
b2.grid(row=2, column=1, sticky=NSEW)
b3 = Button(text="3", command=klickb3)
b3.grid(row=2, column=2, sticky=NSEW)
label = Button(text="Your turn", command=klicklb)
label.grid(row=3, column=0, columnspan=3, sticky=NSEW)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

# Displaying the object window
root.mainloop()
# I win!