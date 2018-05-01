#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: bala
"""

import turtle


def draw_triangle_turtle(walk):
    angle = 120
    tilt = 3
    count = 1
    steps = 200
    while (count < 120):
        print(count)
        if (count > 1):
            walk.right(tilt)
        walk.forward(steps)
        walk.right(angle)
        count = count + 1

def draw_circle_turtle(walk):
        walk.circle(100)


def draw_turtles():
    window = turtle.Screen()
    window.bgcolor("red")
        
    walk = turtle.Turtle()
    walk.shape("turtle")
    walk.color("green")
    walk.speed(1000)
    draw_triangle_turtle(walk)
    draw_circle_turtle(walk)
    window.exitonclick()

draw_turtles()
