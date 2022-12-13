import pygame as pg
import sys
from pygame.color import THECOLORS
from random import randint, choice

pg.init()


def distance(p1, p2):
    return ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5


def point_in_circle(p, circle_center, circle_radius):
    dist = distance(circle_center, p)
    if dist < circle_radius:
        return True
    else:
        return False


def circle_center():
    return (randint(circle_radius, WIDTH-circle_radius), randint(circle_radius, HEIGHT-circle_radius))


circle_radius = 50
WIDTH = 640
HEIGHT = 480
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Тир')
shot = pg.mixer.Sound('shot.wav')
colors = list(THECOLORS.values())
color = THECOLORS['cyan']
center_circle = circle_center()
clock = pg.time.Clock()
points = 0


def draw_points():
    font = pg.font.SysFont('rockwellcondensed', 20)
    text = font.render(f"{str(points)}", True, THECOLORS['yellow'])
    screen.blit(text, (10, 10))


def controls():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            global color
            global center_circle
            global points
            point = event.pos
            p_i_c = point_in_circle(point, center_circle, circle_radius)
            if p_i_c:
                shot.play()
                color = choice(colors)
                center_circle = circle_center()
                time_count = int(clock.tick_busy_loop())
                if time_count < 1000:
                    points += 100
                elif time_count > 1000 and time_count < 2000:
                    points += 50
                else:
                    points += 1
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            one_shot = False


while True:
    screen.fill(THECOLORS['black'])
    controls()
    pg.draw.circle(screen, color, center_circle, circle_radius)
    draw_points()
    pg.display.update()
