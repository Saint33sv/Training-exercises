import pygame as pg
import sys
poinlist = [(950, 120), (1100, 220), (800, 500)]

pg.init()

screen = pg.display.set_mode((1200, 800))
screen.fill((255, 255, 255))
r = pg.Rect(50, 60, 100, 200)
re = pg.Rect(1000, 600, 80, 100)
pg.draw.rect(screen, (166, 20, 200), r, 0)
pg.draw.line(screen, (255, 40, 20), (800, 550), (320, 40), 3)
pg.draw.circle(screen, (20, 200, 20), (350, 500), 220, 0)
pg.draw.lines(screen, (100, 0, 59), True, poinlist, 3)
pg.draw.ellipse(screen, (23, 250, 88), re, 4)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()