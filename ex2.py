from turtle import *
from random import randint

title("Картина очень крутого художника 'Какая то хрень'")
shape('turtle')
bgcolor('blue')


def star(x, y):
    width(3)
    color('yellow')
    up()
    goto(x, y)
    down()
    goto(x+2, y)


def moon(x, y):
    color('yellow')
    begin_fill()
    up()
    goto(x, y)
    down()
    circle(50)
    fillcolor('yellow')
    end_fill()


def one_tree(x, y):
    color('brown')
    begin_fill()
    up()
    goto(x, y)
    down()
    lt(90)
    fd(25)
    lt(90)
    fd(15)
    lt(90)
    fd(25)
    lt(90)
    fd(15)
    end_fill()
    up()
    lt(90)
    fd(25)
    rt(90)
    fd(40)
    color('green')
    begin_fill()
    down()
    for i in range(3):
        lt(120)
        fd(95)
    end_fill()
    up()
    lt(120)
    fd(70)
    rt(120)
    fd(30)
    begin_fill()
    down()
    for i in range(3):
        lt(120)
        fd(85)
    end_fill()
    up()
    lt(120)
    fd(70)
    rt(120)
    fd(23)
    begin_fill()
    down()
    for i in range(3):
        lt(120)
        fd(60)
    end_fill()


def paint_stars(x):
    num_star = 0
    while num_star <= x:
        star(randint(-360, 360), randint(-100, 330))
        num_star += 1


one_tree(-340, -330)
one_tree(-290, -330)
one_tree(-240, -330)
one_tree(-140, -330)
one_tree(-90, -330)
one_tree(-40, -330)
one_tree(60, -330)
one_tree(110, -330)
one_tree(160, -330)
one_tree(260, -330)
one_tree(310, -330)
one_tree(360, -330)
moon(-150, 220)
paint_stars(60)
color('blue')

done()
