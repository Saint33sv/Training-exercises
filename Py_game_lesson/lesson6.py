import pygame as pg
import sys
from pygame.color import THECOLORS
from random import randint
color = (randint(0, 255), randint(0, 255), randint(0, 255))

pg.init()

screen = pg.display.set_mode((700, 700))
screen.fill(THECOLORS['white'])
r_scr = screen.get_rect()
rect = pg.Rect(350, 350, 20, 20)
screen.fill(THECOLORS['white'])
pg.draw.rect(screen, color, rect, 0)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and rect.left > 0:
                rect.move_ip(-10, 0)
                screen.fill(THECOLORS['white'])
                pg.draw.rect(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), rect, 0)
            elif event.key == pg.K_RIGHT and rect.right <= r_scr.width-10:
                rect.move_ip(10, 0)
                screen.fill(THECOLORS['white'])
                pg.draw.rect(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), rect, 0)
            elif event.key == pg.K_UP and rect.top > 0:
                rect.move_ip(0, -10)
                screen.fill(THECOLORS['white'])
                pg.draw.rect(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), rect, 0)
            elif event.key == pg.K_DOWN and rect.bottom <= r_scr.bottom-10:
                rect.move_ip(0, 10)
                screen.fill(THECOLORS['white'])
                pg.draw.rect(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), rect, 0)

    pg.display.flip()
