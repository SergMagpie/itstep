# by SergMagpie

import socket
import json
import sys


class TicTacClient:
    def __init__(self, name) -> None:
        self.name = name
        self.game = True
        # self.must_unswer = False
    '''
    action:
    'registration'
    'opponent_s_choice'
    'step'
    'message'
    '''

    def processing_request(self, data):
        if data != b'null' and data:
            print('text', data)
            text = data.decode('utf-8')
            dic = json.loads(text)
            print(dic['message'])
            if dic['action'] == 'step':
                message = input('Input ')
                if message == 'exit':
                    self.game = False
                dic['message'] = message
            return str.encode(json.dumps(dic))
        else:
            print('Goodbye')
            self.game = False

    def registration_message(self):
        dic = {
            'name': self.name,
            'action': 'registration',
            'message': ''
        }
        return str.encode(json.dumps(dic))

    def run_game(self):

        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            # Connect the socket to the port where the server is listening
            server_address = ('127.0.0.1', 8888)
            print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)
            sock.sendall(self.registration_message())
            while self.game:
                # Look for the response
                try:
                    text = self.processing_request(sock.recv(4096))
                except (ConnectionResetError, KeyboardInterrupt,
                        ConnectionAbortedError):
                    sock.close()
                    print('Server disconnected\nGoodbye!')
                    sys.exit(0)
                print(text)
                sock.sendall(text)
            sock.close()


if __name__ == "__main__":

    print("Hello!")
    player_name = input("Enter your name, please ")
    player = TicTacClient(player_name)
    player.run_game()
