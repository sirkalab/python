#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: bala
"""

import turtle

def draw_square():
    
    window = turtle.Screen()
    window.bgcolor("red")
        
    walk = turtle.Turtle()
    walk.shape("turtle")
    walk.color("green")
    walk.speed(3)
    
    walk.forward(100)
    walk.right(90)
    walk.forward(100)
    walk.right(90)
    walk.forward(100)
    walk.right(90)
    walk.forward(100)
    
    window.exitonclick()
    
    
draw_square()    
