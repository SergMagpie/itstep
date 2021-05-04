# by SergMagpie
from socketserver import BaseRequestHandler
from socketserver import ThreadingTCPServer
from time import sleep
import json
import sys


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
            play for play in Player.player_list if play is not self and not play.opponent]
        if self.opponent:
            pass
        elif opponents:
            self.opponent = opponents[0]
            self.symbol = 'x'
            self.opponent.opponent = self
            self.opponent.symbol = '0'
        else:
            dic['message'] = 'You must wait for opponent'
            print(*[play.name for play in Player.player_list])
            sleep(2)
            return dic
        dic['message'] = f'Your opponent is {self.opponent.name}' +\
                         f'\nYou symbol is {self.symbol}'
        dic['action'] = 'step'
        return dic

    def step(self, dic):
        message = dic['message']
        if self.opponent:
            print(message)
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
