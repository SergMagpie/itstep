# by SergMagpie

import socket
import json
import sys
import os


class TicTacClient:
    '''server client'''

    def __init__(self, name) -> None:
        self.name = name
        self.game = True
        # self.must_unswer = False
    '''
    action:
    'registration'
    'opponent_s_choice'
    'step'
    'end_of_game'
    '''

    def processing_request(self, data):
        '''main server message handler'''
        if data != b'null' and data:
            text = data.decode('utf-8')
            dic = json.loads(text)
            print(dic['message'])
            if dic['action'] == 'end_of_game':
                self.game = False
            if dic['action'] == 'step':
                message = input('Input ')
                print('Please, wait.')
                if message == 'exit':
                    self.game = False
                    dic['action'] == 'end_of_game'
                dic['message'] = message
            return str.encode(json.dumps(dic))
        else:
            print('Goodbye')
            self.game = False
            dic = {
                'name': self.name,
                'action': 'end_of_game',
                'message': ''
            }
            return str.encode(json.dumps(dic))

    def registration_message(self):
        '''registers the player on the server'''
        dic = {
            'name': self.name,
            'action': 'registration',
            'message': ''
        }
        return str.encode(json.dumps(dic))

    def run_game(self):
        '''main server loop'''
        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            # Connect the socket to the port where the server is listening
            server_address = init_connection()
            print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)
            sock.sendall(self.registration_message())
            while self.game:
                # Look for the response
                try:
                    text = self.processing_request(sock.recv(4096))
                except (ConnectionResetError, KeyboardInterrupt,
                        ConnectionAbortedError, OSError):
                    sock.close()
                    print('Server disconnected\nGoodbye!')
                    self.game = False
                    break
                try:
                    sock.sendall(text)
                except (ConnectionAbortedError, OSError):
                    sock.close()
                    print('Server disconnected\nGoodbye!')
                    self.game = False
            sock.close()


def init_connection():
    '''helps to connect to the server'''
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'res')
    filename = os.path.join(img_folder, "tictactoe_pygame.ini")
    key = '1'
    while key != 'exit':
        try:
            with open(filename, "r") as f:
                addr, port = json.load(f)
        except (FileNotFoundError, ValueError):
            addr = input('Enter server addres ')
            if not addr:
                addr = 'localhost'
            port = input('Enter server port ')
            if not port or not port.isdigit():
                port = "8888"
            port = int(port)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            # Connect the socket to the port where the server is listening
            server_address = (addr, port)
            print('connecting to {} port {}'.format(*server_address))
            try:
                sock.connect(server_address)
                dic = {
                    'name': 'try',
                    'action': 'end_of_game',
                    'message': 'exit'
                }
                sock.sendall(str.encode(json.dumps(dic)))
                print('connect is OK')
                with open(filename, "w") as f:
                    json.dump(server_address, f, indent=4)
                return server_address
            except (ConnectionRefusedError, socket.gaierror):
                print('not connection')
                key = input(
                    '1 - try again, 2 - change server addres, exit to exit ')
                if key == '2':
                    try:
                        os.remove(filename)
                    except OSError:
                        pass
    sys.exit(0)


if __name__ == "__main__":

    print("Hello!")
    player_name = input("Enter your name, please ")
    answ = 'y'
    while answ == 'y':
        player = TicTacClient(player_name)
        player.run_game()
        answ = input('Will play again? y/n ')
