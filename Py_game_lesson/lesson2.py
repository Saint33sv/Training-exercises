import pygame as pg
from pygame.color import THECOLORS
import sys
list_points = [(500, 500), (800, 300), (1100, 500), (500, 500)]
pg.init()
screen = pg.display.set_mode((1200, 800))
screen.fill(THECOLORS['cyan4'])
font = pg.font.SysFont('rockwellcondensed', 40)
text = font.render("Hello world", True, THECOLORS['yellow'])
r = pg.Rect(50, 50, 150, 100)
h_r = pg.Rect(550, 501, 500, 500)
w_r = pg.Rect(600, 550, 150, 150)
d_r = pg.Rect(830, 550, 120, 240)
pg.draw.rect(screen, (THECOLORS['white']), r, 0)
pg.draw.line(screen, (THECOLORS['brown']), (49, 50), (49, 300), 3)
pg.draw.circle(screen, (THECOLORS['blue']), (82, 87), 20, 3)
pg.draw.circle(screen, (THECOLORS['black']), (124, 87), 20, 3)
pg.draw.circle(screen, (THECOLORS['red']), (166, 87), 20, 3)
pg.draw.circle(screen, (THECOLORS['yellow']), (102, 107), 20, 3)
pg.draw.circle(screen, (THECOLORS['green']), (145, 107), 20, 3)
pg.draw.polygon(screen, (THECOLORS['green']), list_points, 0)
pg.draw.rect(screen, (THECOLORS['brown']), h_r, 0)
pg.draw.rect(screen, (THECOLORS['yellow']), w_r, 0)
pg.draw.line(screen, (THECOLORS['black']), (675, 550), (675, 700), 3)
pg.draw.line(screen, (THECOLORS['black']), (600, 625), (750, 625), 3)
pg.draw.rect(screen, (THECOLORS['gray']), d_r, 0)
screen.blit(text, (600, 200))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()

