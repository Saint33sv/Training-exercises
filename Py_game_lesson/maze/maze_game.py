import random
import sys, os
import pygame
from pygame.color import THECOLORS


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


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
    path = resource_path(os.path.join('img', f'wall_64x64_{i}.png'))
    wall_textures.append(pygame.image.load(path))
key_path = resource_path(os.path.join('img', 'key.png'))
key_texture = pygame.image.load(key_path)
door_textures = []
for i in range(4):
    d_path = resource_path(os.path.join('img', f'door{i}.png'))
    door_textures.append(pygame.image.load(d_path))
player_path = resource_path(os.path.join('img', 'player.png'))
player_texture = pygame.image.load(player_path)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('arial', 60)
text = font.render('You Win!', True, THECOLORS['green'])


class Wall:
    def __init__(self, x, y, texture):
        self.x = x
        self.y = y
        self.texture = texture

    def draw(self):
        screen.blit(self.texture, (self.x, self.y))


class Exit:
    def __init__(self, x, y, cell, textures):
        self.x = x
        self.y = y
        self.cell = (self.x*cell, self.y*cell)
        self.sprite1 = textures[0]
        self.sprite2 = textures[1]
        self.sprite3 = textures[2]
        self.sprite4 = textures[3]
        self.quantity_keys = 0

    def draw(self):
        if self.quantity_keys == 0:
            screen.blit(self.sprite1, self.cell)
        if self.quantity_keys == 1:
            screen.blit(self.sprite2, self.cell)
        if self.quantity_keys == 2:
            screen.blit(self.sprite3, self.cell)
        if self.quantity_keys == 3:
            screen.blit(self.sprite4, self.cell)


class Key:
    def __init__(self, x, y, cell, texture):
        self.x = x
        self.y = y
        self.cell = (self.x*cell, self.y*cell)
        self.texture = texture
        self.is_taken = False

    def draw(self):
        if not self.is_taken:
            screen.blit(self.texture, self.cell)


class Maze:
    def __init__(self):
        self.walls = []
        self.player = None
        self.door = None
        self.keys = []
        for y in range(len(MAZE_MAP)):
            for x in range(len(MAZE_MAP[y])):
                if MAZE_MAP[y][x] == '#':
                    wall = Wall(x*CELL_SIDE, y*CELL_SIDE, random.choice(wall_textures))
                    self.walls.append(wall)
                elif MAZE_MAP[y][x] == '@':
                    self.player = Player(x*CELL_SIDE, y*CELL_SIDE)
                elif MAZE_MAP[y][x] == 'X':
                    self.door = Exit(x, y, CELL_SIDE, door_textures)
                elif MAZE_MAP[y][x] == 'K':
                    key = Key(x, y, CELL_SIDE, key_texture)
                    self.keys.append(key)

    def move_player(self):
        self.set_player_direction(self.player.direction)
        self.player.move()
        for i in self.keys:
            if (self.player.x, self.player.y) == i.cell:
                i.is_taken = True
                if i.is_taken:
                    self.door.quantity_keys += 1
                    num = self.keys.index(i)
                    self.keys.pop(num)

    def set_player_direction(self, direction):
        if self.player_can_move(direction):
            self.player.direction = direction
        else:
            self.player.direction = Direction.NONE

    def player_can_move(self, direction):
        global CELL_SIDE
        pcx, pcy = self.get_player_cell()
        if (direction == 1 and MAZE_MAP[pcy-1][pcx] == '#') or (direction == 2 and MAZE_MAP[pcy+1][pcx] == '#') or \
                (direction == 3 and MAZE_MAP[pcy][pcx-1] == '#') or (direction == 4 and MAZE_MAP[pcy][pcx+1] == '#'):
            return False
        elif self.door.quantity_keys != 3 and (direction == 1 and MAZE_MAP[pcy - 1][pcx] == 'X') or \
                self.door.quantity_keys != 3 and (direction == 2 and MAZE_MAP[pcy + 1][pcx] == 'X') or \
                self.door.quantity_keys != 3 and (direction == 3 and MAZE_MAP[pcy][pcx - 1] == 'X') or \
                self.door.quantity_keys != 3 and (direction == 4 and MAZE_MAP[pcy][pcx + 1] == 'X'):
            return False
        else:
            return True

    def draw(self):
        for i in self.walls:
            i.draw()
        self.player.draw()
        self.door.draw()
        for a in self.keys:
            a.draw()

    def win(self):
        if self.door.quantity_keys == 3 and (self.player.x, self.player.y) == self.door.cell:
            return True

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
        self.x = x
        self.y = y
        self.texture = player_texture
        self.step = CELL_SIDE
        self.direction = Direction.NONE

    def draw(self):
        screen.blit(self.texture, (self.x, self.y))

    def move(self):
        if self.direction == Direction.UP:
            self.y -= self.step
        elif self.direction == Direction.DOWN:
            self.y += self.step
        elif self.direction == Direction.LEFT:
            self.x -= self.step
        elif self.direction == Direction.RIGHT:
            self.x += self.step
        else:
            self.direction = Direction.NONE


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





