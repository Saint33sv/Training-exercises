import sys
import pygame as pg
from pygame.color import THECOLORS


pg.init()

screen = pg.display.set_mode((640, 480))
screen.fill(THECOLORS['white'])
rect_scr = screen.get_rect()
font = pg.font.SysFont('italic', 200)
W = font.render("W", True, THECOLORS['red'])
S = font.render("S", True, THECOLORS['red'])
A = font.render("A", True, THECOLORS['red'])
D = font.render("D", True, THECOLORS['red'])
space = font.render("SPACE", True, THECOLORS['red'])
enter = font.render("ENTER", True, THECOLORS['red'])
esc = font.render("ESC", True, THECOLORS['red'])


def rect_font(variable):
    rect_var = variable.get_rect(center=rect_scr.center)
    screen.blit(variable, rect_var)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                screen.fill(THECOLORS['white'])
                rect_font(W)
            elif event.key == pg.K_s:
                screen.fill(THECOLORS['white'])
                rect_font(S)
            elif event.key == pg.K_a:
                screen.fill(THECOLORS['white'])
                rect_font(A)
            elif event.key == pg.K_d:
                screen.fill(THECOLORS['white'])
                rect_font(D)
            elif event.key == pg.K_SPACE:
                screen.fill(THECOLORS['white'])
                rect_font(space)
            elif event.key == pg.K_KP_ENTER:
                screen.fill(THECOLORS['white'])
                rect_font(enter)
            elif event.key == pg.K_ESCAPE:
                screen.fill(THECOLORS['white'])
                rect_font(esc)

    pg.display.flip()
