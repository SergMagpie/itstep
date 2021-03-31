import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


WIDTH = 360  # ширина игрового окна
HEIGHT = 480  # высота игрового окна
FPS = 30  # частота кадров в секунду
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
# отрисовать игрока
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# Цикл игры
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
    # Обновление
    all_sprites.update()
    # Визуализация (сборка)
    # Рендеринг
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()
