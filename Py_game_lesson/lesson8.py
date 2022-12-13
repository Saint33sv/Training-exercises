import pygame as pg
import sys
from pygame.color import THECOLORS
from pygame.sprite import Sprite, Group
import random
pg.init()


class Gun(Sprite):

    def __init__(self, screen):
        super(Gun, self).__init__()
        self.screen = screen
        self.scr_rect = self.screen.get_rect()
        self.image = pg.image.load('pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.scr_rect.centerx
        self.rect.bottom = self.scr_rect.bottom
        self.center = float(self.rect.centerx)
        self.mright = False
        self.mleft = False

    def update_gun(self):
        if self.mleft and self.rect.left > 0:
            self.center -= 0.6
        elif self.mright and self.rect.right < self.scr_rect.right:
            self.center += 0.6
        self.rect.centerx = self.center

    def draw_gun(self):
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.x = gun.rect.centerx
        self.y = float(gun.rect.top-4)
        self.center = (self.x, self.y)
        self.radius = 4
        self.color = THECOLORS['cyan2']
        self.speed = -2.5

    def draw_bullet(self):
        pg.draw.circle(self.screen, self.color, self.center, self.radius)

    def update_bullet(self):
        self.y += self.speed
        self.center = (self.x, self.y)


class Target(Sprite):

    def __init__(self, screen):
        super(Target, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pg.Rect(0, 0, 20, 10)
        self.color = THECOLORS['red']
        self.speed = 0.1
        self.x = float(self.rect.centerx)

    def draw_target(self):
        pg.draw.rect(self.screen, self.color, self.rect)

    def move_target(self):
        self.x += self.speed
        if self.rect.right >= self.screen_rect.right:
            self.speed = -0.1
        elif self.rect.left <= 0:
            self.speed = 0.1
        self.rect.centerx = self.x


def up_bul():
    for bullet in bullets:
        bullet.update_bullet()
        if bullet.y <= -4:
            bullets.remove(bullet)
        collide = target.rect.collidepoint(bullet.center)
        if collide:
            target.color = rand_color


def controls():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                new_bullet = Bullet(scr, gun)
                bullets.add(new_bullet)
                sound_shot.play()
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        gun.mleft = True
    elif keys[pg.K_RIGHT]:
        gun.mright = True
    else:
        gun.mright = False
        gun.mleft = False


colors = list(THECOLORS.values())
sound_shot = pg.mixer.Sound('shot.wav')
scr = pg.display.set_mode((700, 800))
pg.display.set_caption('Cтрельба с пушки')
gun = Gun(scr)
bullets = Group()
target = Target(scr)

while True:
    rand_color = random.choice(colors)
    controls()
    scr.fill(THECOLORS['black'])
    gun.update_gun()
    up_bul()
    target.move_target()
    target.draw_target()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.draw_gun()
    pg.display.update()

