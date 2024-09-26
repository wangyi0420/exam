from turtle import *


def draw_spiderMan():
    speed(13)
    bgcolor("Dark red")
    pensize(10)
    penup
    goto(0,50)
    pendown()
    circle(-120)

    begin_fill()
    seth(92)
    circle(-120, 31)
    sech(200)
    fd(45)
    left(90)
    fd(52)
    end_fill()
draw_spiderMan()
