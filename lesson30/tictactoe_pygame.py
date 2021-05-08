import pygame
import os

class Queue:
    def __init__(self) -> None:
        self.steck = []

        pass

def screen():

    WIDTH = 600
    HEIGHT = 800
    FPS = 60
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    class Player(pygame.sprite.Sprite):
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
            # self.image.fill(WHITE)
            self.image = img[sign]
            self.image = pygame.transform.scale(
                self.image, (180, 180))
            # self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.rect.centerx = 195 * place[num][1] - 90
            self.rect.bottom = 195 * place[num][0]

    def make_game_ground(ground):
        player = [Player(num + 1, sign) for num, sign in enumerate(ground)]
        return player

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
    players = make_game_ground('XXXCCCOOO')
    all_sprites.add(players)
    running = True
    active_input = True
    input_text = ''
    text1 = 'Hello'
    text2 = 'Enter your name'
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверка для закрытия окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if active_input:
                    if event.key == pygame.K_RETURN:
                        print(input_text)
                        input_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
        # Обновление
        all_sprites.update()
        # Рендеринг
        screen.fill(BLACK)
        all_sprites.draw(screen)
        draw_text(screen, text1, 50, 300, 600)
        draw_text(screen, text2, 50, 300, 670)
        draw_text(screen, input_text, 50, 300, 740)

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    screen()
