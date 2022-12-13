import random
import sys
import pygame
from pygame.color import THECOLORS

# TODO(1) Отрисовать лабиринт
# TODO(2) Добавить игрока и реализовать его перемещение
# TODO(3) Добавить выход и условие победы
# TODO(4) Добавить ключи

MAZE_MAP = [
    '#######@#####',
    '#  K#     #K#',
    '# ### # # # #',
    '# #   # #   #',
    '# # # #######',
    '# # #       #',
    '# # ####### #',
    '# #     #K# #',
    '# ##### # # #',
    '#   #   # # #',
    '### # ### # #',
    '#     #     #',
    '#X###########',
]

BLOCK_SIDE = 64
CELL_SIDE = 64
WIDTH = len(MAZE_MAP[0])
HEIGHT = len(MAZE_MAP)

SCREEN_WIDTH = WIDTH * BLOCK_SIDE
SCREEN_HEIGHT = HEIGHT * BLOCK_SIDE

wall_textures = []
for i in range(0, 16):
    wall_textures.append(pygame.image.load(f'img/wall_64x64_{i}.png'))

key_texture = pygame.image.load(f'img/key.png')
door_textures = []
for i in range(4):
    door_textures.append(pygame.image.load(f'img/door{i}.png'))
player_texture = pygame.image.load(f'img/player.png')


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('arial', 60)
text = font.render('You Win!', True, THECOLORS['green'])


class Wall:
    def __init__(self, x, y, texture):
        # TODO(1.1) Атрибуты блока стены:
        #  * Координаты
        #  * Спрайт
        ...

    def draw(self):
        # TODO(1.2) Отобразить блок.
        #  Используйте метод screen.blit(surface, pos)
        ...


class Key:
    def __init__(self, x, y, cell, texture):
        # TODO(4.1) Создать атрибуты ключа:
        #  * Координаты
        #  * Ячейка
        #  * Спрайт
        #  * Признак is_taken
        ...

    def draw(self):
        # TODO(4.2) Отобразить ключ, если его еще не подобрали.
        ...


class Exit:
    def __init__(self, x, y, cell, textures):
        # TODO(3.1) Создать атрибуты выхода:
        #  * Координаты
        #  * Ячейка
        #  * Спрайты
        ...
        # TODO(4.3) Добавить атрибуты для режима игры с ключами:
        #  * Количество собранных ключей
        ...

    def draw(self):
        # TODO(3.2) Отобразить выход. Использовать последний спрайт из списка
        # TODO(4.4) Использовать спрайт, соответствующий количеству собранных
        #  ключей
        ...


class Maze:
    def __init__(self):
        # TODO(1.3) Добавить в лабиринт список стен
        # TODO(2.4) ... игрока
        # TODO(3.3) ... выход        
        # TODO(4.5) ... ключи
        ...
        # TODO(1.4) Реализовать построение лабиринта по карте.
        #  Для этого обойти список строк MAZE_MAP.
        #  Если встретили символ '#', то в список стен добавить блок Wall.
        # TODO(2.5) Если встретили символ '@', то создать игрока
        # TODO(3.4) Если встретили символ 'X', то создать выход
        # TODO(4.6) Если встретили символ 'K', то создать ключ
        ...

    def move_player(self):
        self.set_player_direction(self.player.direction)
        self.player.move()
        # TODO(4.8) Реализовать сбор ключей.
        #  * Если игрок находится на клетке с ключом,
        #    установить ключу признак is_taken
        #  * Обновить количество собранных ключей у объекта типа Exit
        ...

    def set_player_direction(self, direction):
        if self.player_can_move(direction):
            self.player.direction = direction
        else:
            self.player.direction = Direction.NONE

    def player_can_move(self, direction):
        pcx, pcy = self.get_player_cell()
        # TODO(2.7) Реализовать проверку. может ли игрок сделать шаг 
        #  в сторону direction.
        #  * Проверить выход за границы лабиринта
        #  * Проверить движение по направлению к стене
        ...
        return True

    def draw(self):
        # TODO(1.5) Отобразить стены
        # TODO(3.5) Отобразить выход
        # TODO(4.7) Отобразить ключи
        # TODO(2.6) Отобразить игрока
        ...

    def win(self):
        # TODO(3.6) Реализовать условие победы: игрок вышел из лабиринта,
        #  если находится на клетке с дверью
        # TODO(4.9) Доработать условие победы: игрок вышел из лабиринта,
        #  если находится на клетке с дверью и все ключи собраны
        ...

    def get_player_cell(self):
        return (self.player.x // CELL_SIDE, self.player.y // CELL_SIDE)


class Direction:
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Player:
    def __init__(self, x, y):
        # TODO(2.1) Создать атрибуты игрока:
        #  * Координаты
        #  * Спрайт
        #  * Шаг = CELL_SIDE
        #  * Направление движения = Direction.NONE
        ...

    def draw(self):
        # TODO(2.2) Отобразить игрока
        ...

    def move(self):
        # TODO(2.3) Реализовать движение игрока.
        #  Игрок выполняет один шаг в зависимости от направления.
        ...


def start_level():
    maze = Maze()

    while True:
        if maze.win():
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    maze.set_player_direction(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    maze.set_player_direction(Direction.DOWN)
                elif event.key == pygame.K_LEFT:
                    maze.set_player_direction(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    maze.set_player_direction(Direction.RIGHT)
            elif event.type == pygame.KEYUP:
                maze.set_player_direction(Direction.NONE)

        maze.move_player()

        screen.fill((0, 0, 0))
        maze.draw()

        pygame.display.flip()
        pygame.time.wait(66)


def show_win_message():
    screen.blit(text, (CELL_SIDE * 2, SCREEN_HEIGHT - CELL_SIDE - 60))
    pygame.display.flip()
    pygame.time.wait(1000)


while True:
    start_level()
    show_win_message()
