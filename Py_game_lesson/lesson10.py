import sys
import pygame
from pygame.color import THECOLORS

pygame.init()

WIDTH = 1280
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

circle_center = (WIDTH // 2, HEIGHT // 2)
circle_radius = 50
circle_color = THECOLORS['purple2']
dx = 3
dy = 2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    x, y = circle_center
    if x >= WIDTH-circle_radius or x <= 0+circle_radius:
        dx = -dx
    if y >= HEIGHT-circle_radius or y <= 0+circle_radius:
        dy = -dy

    circle_center = (x+dx, y+dy)
    screen.fill(THECOLORS['black'])
    pygame.draw.circle(screen, circle_color, circle_center, circle_radius)
    pygame.display.flip()
    pygame.time.wait(4)
