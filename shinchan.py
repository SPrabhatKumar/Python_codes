import turtle

from pyparsing import Forward 
turtle.speed(0)
turtle.bgcolor("black")
for i in range(15):
    for colours in("red","magenta","blue","green","cyan"):
        turtle.color(colours)
        turtle.pensize(3)
        turtle.left(4)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)