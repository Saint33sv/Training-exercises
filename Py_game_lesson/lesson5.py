import sys
import pygame as pg
from pygame.color import THECOLORS


pg.init()

scr = pg.display.set_mode((600, 600))
scr.fill(THECOLORS['white'])
scr_rect = scr.get_rect()


def moving_rect(x_coord, y_coord):
    rect = pg.Rect(x_coord, y_coord, 10, 10)
    for y in range(10):
        rect.move_ip(-100, 10)
        for x in range(20):
            rect.move_ip(5, 0)
            pg.draw.rect(scr, (THECOLORS['red']), rect, 0)


moving_rect(150, 150)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()


