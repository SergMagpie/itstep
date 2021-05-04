# by SergMagpie
from socketserver import BaseRequestHandler
from socketserver import ThreadingTCPServer
from time import sleep
import json



class Player:
    player_list = []

    def __init__(self) -> None:
        self.name = ''
        self.count = 0
        self.opponent = None
        self.message = None
        self.must_answer = False
        self.massage_not_sending = True
        Player.player_list.append(self)
        pass

    def delete(self):
        Player.player_list.remove(self)

    def processing_request(self):
        pass

    # @staticmethod
    # def regestration(name, trying=0):
    #     names = [i.name for i in Player.player_list]
    #     # print(names)
    #     if name in names:
    #         trying += 1
    #         name = Player.regestration(
    #             name[:-1 if trying > 1 else None] + str(trying), trying)
    #         return name
    #     else:
    #         return name

    # def send_invite_to_the_opponent(self, opponent_name):
    #     '''peturn name of opponent or None'''
    #     for i in Player.player_list:
    #         if i.name == opponent_name:
    #             opponent = i
    #     opponent.message = f'{self.name} invites you to play tic tac toe. y/n '
    #     opponent.must_unswer = True
    #     while not self.message:
    #         pass
    #     if self.message == 'y':
    #         answer = opponent_name
    #     else:
    #         answer = None
    #     return answer

    # def received_message(self, data) -> None:
    #     '''Receives a message from the client, processes it 
    #     and generates a response message.'''
    #     if data:
    #         self.data = data
    #         self.text = data.decode('utf-8')
    #         self.dic = json.loads(self.text)
    #         if self.dic['message']:
    #             print('recv', self.text)
    #         if self.dic['action'] == 'registration':  # registration mode
    #             self.name = Player.regestration(self.dic['name'])
    #             self.dic['message'] = f'Player is registred, hello {self.name}!'
    #             return str.encode(json.dumps(self.dic))
    #         if self.dic['action'] == 'opponent_s_choice':  # opponent selection mode
    #             names = [i.name for i in Player.player_list
    #                      if i.name != self.name and not self.opponent]
    #             # print(names)
    #             sleep(2)
    #             if self.must_answer:
    #                 # when there is an invitation from the opponent
    #                 self.dic['message'] = self.message     
    #                 self.dic['must_unswer'] = True               
    #             elif self.dic['message'] in names: 
    #                 # if an opponent's name is entered
    #                 # send invite to the opponent
    #                 self.opponent = self.send_invite_to_the_opponent(self.dic['message'])
    #             elif names:
    #                 # offer to choose an opponent if there is someone to choose from
    #                 self.dic['message'] = f"Dear {self.name}!" +\
    #                     f" You can choose an opponent {' '.join(names)}"
    #                 self.dic['must_unswer'] = True 
    #             elif self.massage_not_sending:
    #                 self.dic['message'] = f"Dear {self.name}!" +\
    #                     'There are no opponents yet, check back later!'
    #                 self.massage_not_sending = False
    #             pass
    #         '''
    #         action:
    #         'registration'
    #         'opponent_s_choice'
    #         'step'
    #         'message'
    #         '''
    #     else:
    #         print('No data in message')
    #     return str.encode(json.dumps(self.dic))
    pass


# class TicTacServer:
#     def __init__(self) -> None:
#         pass
#     player_list = []

#     pass


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('New connection from:', self.client_address)
        # creating a new player
        self.player = Player()
        while True:
            try:
                msg = self.player.processing_request(self.request.recv(1024))
            except ConnectionAbortedError:
                print(f'Player {self.player.name} disconected')
                self.player.delete()
                del self.player
                break
            if self.player.must_answer:
                print('send {}'.format(msg.decode()))
            if not msg:
                break
            self.request.send(msg)


if __name__ == '__main__':
    server_address = ('127.0.0.1', 8888)
    server = ThreadingTCPServer(server_address, EchoHandler)
    server.serve_forever()
