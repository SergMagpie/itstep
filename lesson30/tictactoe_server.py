# by SergMagpie
from socketserver import BaseRequestHandler
from socketserver import ThreadingTCPServer
from time import sleep
import json
import sys


class Game:
    '''here are the actual games'''

    def __init__(self, playerX, playerO) -> None:
        self.step = 1
        self.playground = '123456789'
        self.playerX = playerX
        self.playerO = playerO
        self.winner = None

    def whose_move(self, player):
        '''determines whose turn it is to move'''
        if self.step % 2:
            moved_player = self.playerX
        else:
            moved_player = self.playerO
        return player is moved_player

    def move(self, player, message):
        '''processes the player's move'''
        if len(message) == 1 and message in self.playground:
            new_playground = []
            for i in self.playground:
                if message == i:
                    new_playground.append(player.symbol)
                else:
                    new_playground.append(i)
            self.playground = ''.join(new_playground)
            self.step += 1
            return 'Step ' + str(self.step)
        else:
            if self.step == 1:
                return 'Your move'
            else:
                return 'You made a mistake'

    def show_playground(self):
        '''draws the playing field'''
        string_top = "┌─┬─┬─┐"
        string1 = "│" + "│".join(self.playground[6:9]) + "│"
        string_med = "├─┼─┼─┤"
        string2 = "│" + "│".join(self.playground[3:6]) + "│"
        string3 = "│" + "│".join(self.playground[0:3]) + "│"
        string_bottom = "└─┴─┴─┘"
        return f"\n{string_top}\n{string1}\n{string_med}\n{string2}"\
            f"\n{string_med}\n{string3}\n{string_bottom}"

    def end(self) -> bool:
        '''checks if the game is over'''
        comb = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9},
                {1, 5, 9}, {7, 5, 3},
                {1, 4, 7}, {2, 5, 8}, {3, 6, 9})
        game_state_total = [(n + 1, i) for n, i in enumerate(self.playground)]
        cross_list = set(n for n, i in game_state_total if i == 'X')
        zero_list = set(n for n, i in game_state_total if i == 'O')
        ability_to_move = [i for i in self.playground if i.isdigit()]
        for i in comb:
            if i.issubset(cross_list):
                self.winner = self.playerX
                return True
            elif i.issubset(zero_list):
                self.winner = self.playerO
                return True
        if not ability_to_move:
            return True
        return False


class Player:
    '''here are the players'''
    player_list = []

    def __init__(self) -> None:
        self.name = ''
        self.opponent = None
        Player.player_list.append(self)
        self.gameover = False

    def delete(self):
        '''removes the player'''
        if self.opponent:
            self.opponent.opponent = None
        if self in Player.player_list:
            Player.player_list.remove(self)

    def registration(self, dic):
        '''registers a new player'''
        self.name = dic['name']
        dic['action'] = 'opponent_s_choice'
        return dic

    def opponent_s_choice(self, dic):
        '''selects and appoints the first opponent found on the server'''
        opponents = [
            play for play in Player.player_list
            if play is not self and not play.opponent and play.name]
        if self.opponent:
            pass  # this pass is a ficha, not the bag!
        elif opponents:
            self.opponent = opponents[0]
            game = Game(self, self.opponent)
            self.round = game
            self.opponent.round = game
            self.symbol = 'X'
            self.opponent.opponent = self
            self.opponent.symbol = 'O'
        else:
            dic['message'] = 'You must wait for opponent'
            sleep(2)
            return dic
        dic['message'] = f'Your opponent is {self.opponent.name}' +\
                         f'\nYou symbol is {self.symbol}' +\
                         f'\nPress enter to continue'
        dic['action'] = 'step'
        return dic

    def step(self, dic):
        '''controls the game step by step'''
        message = dic['message']
        if self.opponent:
            rem = 'Your move '
            if self.round.whose_move(self):
                rem = self.round.move(self, message)
            trying = 15  # settimeout
            # the second player expects
            while not self.round.whose_move(self) and trying:
                trying -= 1
                if self.opponent:  # if an opponent exists
                    sleep(0.5)
                else:
                    break
            if self.round.end():
                if self.round.winner:
                    dic['message'] = self.round.show_playground() +\
                        '\nPlayer ' + self.round.winner.name + ' win!'
                else:
                    dic['message'] = self.round.show_playground() +\
                        '\nThe game of chess ended in a draw'
                dic['action'] = 'end_of_game'

                if self.opponent:
                    self.opponent.opponent = None
                self.opponent = None
            else:
                dic['message'] = rem + \
                    self.round.show_playground() + \
                    '\nYour move '
        else:
            dic['message'] = 'Your opponent disconnected!\nYou win!'
            dic['action'] = 'end_of_game'
        return dic

    def end_of_game(self, dic):
        '''removes the client at the end of the game'''
        print('end of game', self.name)
        self.delete()
        self.round = None
        self.gameover = True
        return dic

    def processing_request(self, data):
        '''distributes the request among the handlers'''
        if data:
            text = data.decode('utf-8')
            dic = json.loads(text)
            actions = {
                'registration': self.registration,
                'opponent_s_choice': self.opponent_s_choice,
                'step': self.step,
                'end_of_game': self.end_of_game
            }
            dic = actions[dic['action']](dic)
            return str.encode(json.dumps(dic))


class EchoHandler(BaseRequestHandler):
    '''here is the server itself'''

    def handle(self):
        print('New connection from:', self.client_address)
        self.player = Player()  # creating a new player
        self.request.settimeout(30)
        self.game = True
        while not self.player.gameover:
            try:
                msg = self.player.processing_request(self.request.recv(4096))
            except (ConnectionAbortedError, ConnectionResetError):
                print(f'Player {self.player.name} disconected')
                self.player.delete()
                del self.player
                break
            if not msg:
                break
            self.request.send(msg)


if __name__ == '__main__':
    server_address = ('localhost', 8888)
    server = ThreadingTCPServer(server_address, EchoHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
