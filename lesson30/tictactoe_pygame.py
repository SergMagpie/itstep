import pygame
import os
from time import sleep
import re
from threading import Thread
import sys
import socket
import json


class Queue:
    '''class of variables for communication between processes'''

    def __init__(self) -> None:
        self.in_message = []
        self.out_message = []
        self.field_message = ['CCCCCCCCC']
        self.waiting_for_outgoing_message = True

    def outgoing_message(self):
        '''function of waiting for a response to a server request'''
        while not self.out_message:
            self.waiting_for_outgoing_message = True
            sleep(0.5)
        return self.out_message.pop()

    def incoming_message(self, message: str):
        '''function of parsing and transferring server messages 
        to the pygame_client (wrapper for print)'''
        list_message = message.split('\n')
        field = ''
        self.in_message.clear()
        for i in list_message:
            if re.fullmatch(r"^[^┌│├└].+", i):
                self.in_message.append(i)
            if re.fullmatch(r"│[\dXO]│[\dXO]│[\dXO]│", i):
                for j in i:
                    if j.isdigit():
                        field += 'C'
                    elif j in ('X', 'O'):
                        field += j
        if field:
            self.field_message.clear()
            self.field_message.append(field)
        return message

    def field(self):
        return self.field_message[0]


transfer = Queue()


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
            print(transfer.incoming_message(dic['message']))
            if dic['action'] == 'end_of_game':
                self.game = False
            if dic['action'] == 'step':
                message = transfer.outgoing_message()  # input('Input ')
                print(transfer.incoming_message('Please, wait.'))
                if message == 'exit':
                    self.game = False
                    dic['action'] == 'end_of_game'
                dic['message'] = message
            return str.encode(json.dumps(dic))
        else:
            print(transfer.incoming_message('Goodbye'))
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
            # print(transfer.incoming_message(
            #     'connecting to {} port {}'.format(*server_address)))
            sock.connect(server_address)
            sock.sendall(self.registration_message())
            while self.game:
                # Look for the response
                try:
                    text = self.processing_request(sock.recv(4096))
                except (ConnectionResetError, KeyboardInterrupt,
                        ConnectionAbortedError, OSError):
                    sock.close()
                    print(transfer.incoming_message(
                        'Server disconnected\nGoodbye!'))
                    self.game = False
                try:
                    sock.sendall(text)
                except (ConnectionAbortedError, OSError):
                    sock.close()
                    print(transfer.incoming_message(
                        'Server disconnected\nGoodbye!'))
                    self.game = False
            sock.close()


def screen():
    '''main game loop and screen creator'''

    # variable for thread communication

    WIDTH = 600
    HEIGHT = 900
    FPS = 60
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    class Pane(pygame.sprite.Sprite):
        def __init__(self, num, sign):
            pygame.sprite.Sprite.__init__(self)
            game_folder = os.path.dirname(__file__)
            img_folder = os.path.join(game_folder, 'res')
            clear_img = pygame.image.load(
                os.path.join(img_folder, 'clear.png')).convert()
            o_img = pygame.image.load(
                os.path.join(img_folder, 'o.png')).convert()
            x_img = pygame.image.load(
                os.path.join(img_folder, 'x.png')).convert()
            img = {'X': x_img,
                   'O': o_img,
                   'C': clear_img,
                   }
            place = {1: (3, 1),
                     2: (3, 2),
                     3: (3, 3),
                     4: (2, 1),
                     5: (2, 2),
                     6: (2, 3),
                     7: (1, 1),
                     8: (1, 2),
                     9: (1, 3),
                     }

            # self.image = pygame.Surface((180, 180))
            self.image = img[sign]
            # self.image.fill(WHITE)
            self.image = pygame.transform.scale(
                self.image, (180, 180))
            # self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.rect.centerx = 195 * place[num][1] - 90
            self.rect.bottom = 195 * place[num][0]
            self.num = num

    def make_game_ground(ground):
        g3, g2, g1 = ground[:3], ground[3:6], ground[6:]
        pane = [Pane(num + 1, sign) for num, sign in enumerate(g1 + g2 + g3)]
        return pane

    def draw_text(surf, text, size, x, y):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    pygame.init()
    # pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic tac toy client by SergMagpie")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    panes = make_game_ground(transfer.field())
    all_sprites.add(panes)
    running = True
    active_input = True
    gameover = False
    first_answer = True
    text1 = 'Hello'
    text2 = 'Enter your name'
    text3 = ''
    text4 = ''
    player_name = ''
    while running:
        # Keeping the cycle at the correct speed
        clock.tick(FPS)
        # Process (event) input
        for event in pygame.event.get():
            # check to close the window
            if event.type == pygame.QUIT:
                transfer.out_message.append('exit')
                running = False
            if event.type == pygame.KEYDOWN:
                if active_input:
                    if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        if not player_name and text4:
                            player_name = text4
                            text4 = ''
                            # active_input = False
                            player = TicTacClient(player_name)
                            game = Thread(target=player.run_game)
                            game.start()
                        elif transfer.waiting_for_outgoing_message:
                            transfer.out_message.append(text4)
                            text4 = ''
                            # active_input = False
                            transfer.waiting_for_outgoing_message = False
                        elif gameover:
                            if text4 == 'y':
                                print('starting new game')
                                player = TicTacClient(player_name)
                                game = Thread(target=player.run_game)
                                game.start()
                            else:
                                running = False
                    elif event.key == pygame.K_BACKSPACE:
                        text4 = text4[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        transfer.out_message.append('exit')
                    else:
                        text4 += event.unicode
            if event.type == pygame.MOUSEBUTTONUP:
                if transfer.waiting_for_outgoing_message:
                    pos = pygame.mouse.get_pos()
                    clicked_panes = [
                        s for s in panes if s.rect.collidepoint(pos)]
                    if clicked_panes:
                        button = [i for i in clicked_panes][0]
                        button.image.fill(RED)
                        text = str(button.num)
                        transfer.out_message.append(text)
                        transfer.waiting_for_outgoing_message = False
        # Update
        # active_input = transfer.waiting_for_outgoing_message
        panes = make_game_ground(transfer.field())
        all_sprites.add(panes)
        all_sprites.update()
        # Rendering
        screen.fill(BLACK)
        all_sprites.draw(screen)
        if transfer.in_message:
            text1 = text2
            text2 = text3
            text3 = transfer.in_message.pop(0)
        if player_name:
            if not game.is_alive():
                if first_answer:
                    text1 = text2
                    text2 = text3
                    text3 = 'Will play again? y/n '
                    first_answer = False
                gameover = True
                transfer.waiting_for_outgoing_message = False
            else:
                first_answer = True
        draw_text(screen, text1, 50, 300, 600)
        draw_text(screen, text2, 50, 300, 670)
        draw_text(screen, text3, 50, 300, 740)
        draw_text(screen, text4, 50, 300, 810)

        # After drawing everything, flip the screen
        pygame.display.flip()

    pygame.quit()
    sys.exit(0)


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
            print(transfer.incoming_message(
                'connecting to {} port {}'.format(*server_address)))
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

    screen()
