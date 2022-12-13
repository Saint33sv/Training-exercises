import pygame as pg
import sys
from random import randint
from pygame.color import THECOLORS
rand_num = randint(1, 24)
rand_color = (randint(0, 255), randint(0, 255), randint(0, 255))

pg.init()


def grid(size, wight, height):
    num = 1
    for x in range(wight):
        for y in range(height):
            rect = pg.Rect(y*(size+1), x*(size+1), size, size)
            pg.draw.rect(scr, (THECOLORS['cyan']), rect, 4)
            if num == rand_num:
                sur = pg.Surface((size-8, size-8))
                sur_rect = sur.get_rect(center=rect.center)
                sur.fill(rand_color)
                scr.blit(sur, sur_rect)
                font = pg.font.SysFont('italic', 100)
                text = font.render(str(num), True, THECOLORS['red'])
                rect_text = text.get_rect(center=sur_rect.center)
                scr.blit(text, rect_text)
            font = pg.font.SysFont('italic', 100)
            text = font.render(str(num), True, THECOLORS['red'])
            rect_text = text.get_rect(center=rect.center)
            scr.blit(text, rect_text)
            num += 1


scr = pg.display.set_mode((1200, 800))
scr.fill((255, 255, 255))
grid(200, 4, 6)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()
