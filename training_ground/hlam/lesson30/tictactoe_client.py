# by SergMagpie

import socket
import json

# class Msg:
#     def __init__(self, dic):
#         self.name = dic['name']
#         self.message = dic['message']
#         self.action = dic['action']



class TicTacClient:
    def __init__(self, name) -> None:
        self.name = name
        self.action = 'registration'
        # self.must_unswer = False
    '''
    action:
    'registration'
    'opponent_s_choice'
    'step'
    'message'
    '''

    def run_game(self):

        # def push(message=''):
        #     if self.must_unswer:
                
        #         message = input("enter msg ")
        #         self.must_unswer = False
        #     dic = {}
        #     dic["name"] = self.name
        #     dic["message"] = message
        #     dic["action"] = self.action
        #     dic['must_unswer'] = self.must_unswer
        #     rez = json.dumps(dic).encode()
        #     return rez

        # def pull(text):
        #     if text:
        #         text = text.decode()
        #         dic = json.loads(text)
        #         if dic['message']:
        #             print(dic['message'])
        #             dic['message'] = ''
        #         self.must_unswer = dic['must_unswer']
        #         if dic['action'] == 'registration':
        #             self.name = dic['name']
        #             self.action = 'opponent_s_choice'
        #         return text

        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            # Connect the socket to the port where the server is listening
            server_address = ('127.0.0.1', 8888)
            print('connecting to {} port {}'.format(*server_address))
            # sock.connect(server_address)
            # sock.sendall(push())
            # text = pull(sock.recv(1024))
            while True:
                # добавить функцию инпут только если нужен (ожидается) инпут
                # в ответ на запрос сервера
                # message = push()
                # print('sending {}'.format(message.decode('utf-8')))
                sock.sendall(message)
                # Look for the response
                text = pull(sock.recv(1024))
                # print('received {}'.format(text))


if __name__ == "__main__":

    print("Hello!")
    player_name = input("Enter your name, please ")
    player = TicTacClient(player_name)
    player.run_game()
