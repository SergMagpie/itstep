import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 48
        self.image = pygame.Surface((self.size + 2, self.size + 2))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def faze(self, size) -> int:
        if self.size < size and size < 300:
            self.size = size
            return 2
        elif self.size > size and size > 40:
            self.size = size
            return -2
        elif size > 200:
            return -4
        else:
            return 4

    def update(self):
        change_step = self.faze(self.image.get_rect()[3])
        if self.rect.width > 300:
            change_step = -change_step
        size = tuple(i + change_step for i in self.image.get_rect()[2:4])
        self.image = pygame.Surface(size)
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
