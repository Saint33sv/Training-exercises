import pygame as pg
import sys
from pygame.color import THECOLORS


pg.init()


def mright(anim_count, coords):
    animetion_set = [pg.image.load(f'animations/r{i}.png') for i in range(1, 6)]
    screen.blit(animetion_set[anim_count // 12], coords)


def mleft(anim_count, coords):
    animetion_set = [pg.image.load(f'animations/l{i}.png') for i in range(1, 6)]
    screen.blit(animetion_set[anim_count // 12], coords)


screen = pg.display.set_mode((700, 700))
sprite = pg.image.load('animations/0.png')
r_s = screen.get_rect()
spr_rct = sprite.get_rect(centerx=r_s.centerx, bottom=r_s.bottom)
clock = pg.time.Clock()
isjump = False
jumpcount = 10
left = False
right = False
i = 0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and spr_rct.left > 0:
        spr_rct.centerx -= 1
        left = True
        right = False
    elif keys[pg.K_RIGHT] and spr_rct.right < r_s.right:
        spr_rct.centerx += 1
        left = False
        right = True
    elif not (isjump):
        if keys[pg.K_SPACE]:
            isjump = True
    else:
        if jumpcount >= -10:
            if jumpcount < 0:
                spr_rct.y += (jumpcount ** 2) / 2
            else:
                spr_rct.y -= (jumpcount ** 2) / 2
            jumpcount -= 1
        else:
            isjump = False
            jumpcount = 10
        left = False
        right = False
    screen.fill(THECOLORS['white'])
    if left:
        mleft(i, spr_rct)
    elif right:
        mright(i, spr_rct)
    else:
        screen.blit(sprite, spr_rct)
    i += 1
    if i == 60:
        i = 0
    pg.display.flip()
    clock.tick(60)
