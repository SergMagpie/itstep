def tictactoe():
    def make_play_ground(play_list):
        def ins_char(char, coords):
            for cor in coords:
                for nums, strings in enumerate(play_ground):
                    if coord_chars[cor][1] <= nums <= coord_chars[cor][1] + 4:
                        play_ground[nums] = strings[:coord_chars[cor][0]] + \
                            char[nums - coord_chars[cor][1]] + \
                            strings[coord_chars[cor][0] + 8:]
        ground = [
            ' 777777 #  8888  #  9999  ',  # 0
            '     7  # 8    8 # 9    9 ',  # 1
            '    7   #  8888  #  99999 ',  # 2
            '   7    # 8    8 #      9 ',  # 3
            '  7     #  8888  #  9999  ',  # 4
            '##########################',  # 5
            ' 4    4 # 555555 #  6666  ',  # 6
            ' 4    4 # 5      # 6      ',  # 7
            ' 444444 # 555555 # 66666  ',  # 8
            '      4 #      5 # 6    6 ',  # 9
            '      4 # 555555 #  6666  ',  # 10
            '##########################',  # 11
            '     1  # 222222 # 333333 ',  # 12
            '    11  #      2 #      3 ',  # 13
            '   1 1  # 222222 # 333333 ',  # 14
            '     1  # 2      #      3 ',  # 15
            '    111 # 222222 # 333333 ']  # 16
        cross = [
            # 01234567
            ' x    x ',  # 0
            '  x  x  ',  # 1
            '   xx   ',  # 2
            '  x  x  ',  # 3
            ' x    x ',  # 4
        ]
        zero = [
            '  0000  ',
            ' 0    0 ',
            ' 0    0 ',
            ' 0    0 ',
            '  0000  '
        ]
        coord_chars = {1: [0, 12], 2: [9, 12], 3: [18, 12], 4: [0, 6],
                       5: [9, 6], 6: [18, 6], 7: [0, 0], 8: [9, 0],
                       9: [18, 0]}
        play_ground = [i for i in ground]
        ins_char(cross, crosses_coord())
        ins_char(zero, zero_coord())
        return play_ground

    def crosses_coord():
        return [n + 1 for n, char in enumerate(play_list)
                if char == 'X']

    def zero_coord():
        return [n + 1 for n, char in enumerate(play_list)
                if char == '0']
    bottom = [
        '  H     H  EEEEE L      L      OOOOOOO  !  !  !     *   *    *   *    *   *     ',
        '  H     H  E     L      L      O     O  !  !  !      * *      * *      * *      ',
        '  HHHHHHH  EEEEE L      L      O     O  !  !  !    *******  *******  *******    ',
        '  H     H  E     L      L      O     O               * *      * *      * *      ',
        '  H     H  EEEEE LLLLLL LLLLLL OOOOOOO  !  !  !     *   *    *   *    *   *     ',
    ]
    left_player = [
        '          ЖЖЖЖЖЖЖЖЖ       ',
        '     ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ    ',
        '   ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ  ',
        '  ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ ',
        '  ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ ',
        '  ЖЖЖЖЖ   ЖЖЖЖЖЖ   ЖЖЖЖЖЖ ',
        '  ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ ',
        '  ЖЖЖЖЖЖЖЖЖЖЖ   ЖЖЖЖЖЖЖЖЖ ',
        '  ЖЖЖЖЖЖЖЖЖЖ     ЖЖЖЖЖЖЖЖ ',
        '  ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ ',
        '   ЖЖЖЖ  ЖЖЖЖЖЖЖЖЖ  ЖЖЖЖ  ',
        '   ЖЖЖЖЖЖЖ        ЖЖЖЖ    ',
        '     ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ     ',
        '      ЖЖЖЖЖЖЖЖЖЖЖЖЖЖ      ',
        '                          ',
        '                          ',
        '                          ',
    ]
    right_player = [
        '          МММММММММ       ',
        '     МММММММММММММММММ    ',
        '   МММММММММММММММММММММ  ',
        '  МММММММММММММММММММММММ ',
        '  МММММММММММММММММММММММ ',
        '  ММММММ   МММММММ   ММММ ',
        '  МММММММММММММММММММММММ ',
        '  МММММММММ    ММММММММММ ',
        '  ММММММММ     ММММММММММ ',
        '  МММММММММММММММММММММММ ',
        '   ММММ  МММММММММ  ММММ  ',
        '   ММММММ        МММММ    ',
        '     ММММММММММММММММ     ',
        '      ММММММММММММММ      ',
        '         ММММММММ         ',
        '                          ',
        '                          '
    ]
    aktive = 'X'
    last_string = 'X makes a move'
    variants = [[2, 5, 8], [1, 5, 9], [3, 5, 7], [1, 2, 3],
                [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9]]

    def print_screen():
        play_ground = make_play_ground(play_list)
        print('\n' * 10, *bottom, sep='\n')
        for i, s in enumerate(play_ground):
            print(f'{left_player[i]}{s}{right_player[i]}')
        print(f'{last_string}\nPlease, {aktive} input you try \
or 0 for exit', end=' ')
        return input()
    play_list = '123456789'
    step = print_screen()
    while step != '0':
        if step not in '123456789':
            last_string = 'You make mistake'
        else:
            if play_list[int(step) - 1] in ['0', 'X']:
                last_string = 'You make mistake'
            else:
                play_list = play_list[:int(step) - 1] + \
                    aktive + play_list[int(step):]
                if any([all([i in list(crosses_coord()) 
                    for i in var]) for var in variants]):
                    last_string = 'CONGRAT, X WIN!!!'
                    play_list = '123456789'
                elif any([all([i in list(zero_coord()) 
                    for i in var]) for var in variants]):
                    last_string = 'CONGRAT, 0 WIN!!!'
                    play_list = '123456789'
                else:
                    aktive = ('X' if aktive == '0' else '0')
                    last_string = f'{aktive} makes a move'
        step = print_screen()


if __name__ == "__main__":
    tictactoe()
