# by SergMagpie
from socketserver import BaseRequestHandler
from socketserver import ThreadingTCPServer
from time import sleep
import json
import sys


class Game:
    def __init__(self, playerX, playerO) -> None:
        self.step = 1
        self.playground = '123456789'
        self.playerX = playerX
        self.playerO = playerO
        self.winner = None

    def whose_move(self, player):
        if self.step % 2:
            moved_player = self.playerX
        else:
            moved_player = self.playerO
        return player is moved_player

    def move(self, player, message):
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
            return 'You made a mistake'            

    def show_playground(self):
        string1 = self.playground[6:9]
        string2 = self.playground[3:6]
        string3 = self.playground[0:3]
        return f"\n{string1}\n{string2}\n{string3}"

    def end(self) -> bool:
        comb = ((1,2,3),(4,5,6),(7,8,9),
                (1,5,9),(7,5,3),
                (1,4,7),(2,5,8),(3,6,9))
        game_state_total = [(n + 1, i) for n, i in enumerate(self.playground)]
        cross_list = tuple(n for n, i in game_state_total if i == 'X')
        zero_list = tuple(n for n, i in game_state_total if i == 'O')
        ability_to_move = [i for i in self.playground if i.isdigit()]
        for i in comb:
            if i in cross_list:
                self.winner = self.playerX
                return True
            elif i in zero_list:
                self.winner = self.playerO
                return True
        if not ability_to_move:
            return True
        return False
        
    pass


class Player:
    player_list = []

    def __init__(self) -> None:
        self.name = ''
        self.opponent = None
        Player.player_list.append(self)
        pass

    def delete(self):
        self.opponent.opponent = None
        Player.player_list.remove(self)

    def registration(self, dic):
        self.name = dic['name']
        dic['action'] = 'opponent_s_choice'
        return dic
        pass

    def opponent_s_choice(self, dic):
        opponents = [
            play for play in Player.player_list
            if play is not self and not play.opponent]
        if self.opponent:
            pass
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
            print(*[play.name for play in Player.player_list])
            sleep(2)
            return dic
        dic['message'] = f'Your opponent is {self.opponent.name}' +\
                         f'\nYou symbol is {self.symbol}' +\
                         f'\nPress enter to continue'
        dic['action'] = 'step'
        return dic

    def step(self, dic):
        message = dic['message']
        if self.opponent:
            print(message)
            if self.round.whose_move(self):
                rem = self.round.move(self, message)
            trying = 15 # settimeout
            while not self.round.whose_move(self) and trying:  # the second player expects
                trying -= 1
                if self.opponent:  # if an opponent exists
                    sleep(2)
                    rem = 'Your move '
                else:
                    break
            if self.round.end():
                if self.round.winner:
                    dic['message'] = self.round.winner.name + 'win!'
                    dic['action'] = 'opponent_s_choice'
                    if self.opponent:
                        self.opponent.opponent = None
                    self.opponent = None
            else:
                dic['message'] = rem + \
                    self.round.show_playground() + \
                    '\nYour move '
            # if message == 'exit':
            #     print(f'Player {self.name} disconected')
            #     self.delete()
            #     del self
            #     return None
            pass
        else:
            dic['message'] = 'You win!'
            dic['action'] = 'opponent_s_choice'
        return dic

    def processing_request(self, data):
        if data:
            text = data.decode('utf-8')
            print('text', text)
            dic = json.loads(text)
            actions = {
                'registration': self.registration,
                'opponent_s_choice': self.opponent_s_choice,
                'step': self.step,
            }
            dic = actions[dic['action']](dic)
            return str.encode(json.dumps(dic))
    pass


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('New connection from:', self.client_address)
        self.player = Player()  # creating a new player
        self.request.settimeout(30)
        while True:
            try:
                msg = self.player.processing_request(self.request.recv(4096))
            except ConnectionAbortedError:
                print(f'Player {self.player.name} disconected')
                self.player.delete()
                del self.player
                break
            if not msg:
                break
            self.request.send(msg)


if __name__ == '__main__':
    server_address = ('127.0.0.1', 8888)
    server = ThreadingTCPServer(server_address, EchoHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
