from turtle import *
"""Этот скрипт рисует многоугольник с заданым количеством граней"""
title()
shape('turtle')
bgcolor('green')
num = 10
color('black')
width(3)

for i in range(num):
    fd(100)
    rt(360 / num)
"""Рисуем круг"""
up()
lt(45)
fd(200)
color('red')
down()
circle(100)
"""Рисуем триугольник"""
up()
rt(180)
fd(100)
rt(45)
fd(200)
color('blue')
down()
for i in range(3):
    fd(200)
    rt(360 / 3)
done()

