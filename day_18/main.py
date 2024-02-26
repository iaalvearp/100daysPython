from turtle import Turtle, Screen
from random import choice

tim = Turtle()

####################
# First challenge
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Second challenge
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#
# for _ in range(15):
#     tim.forward(10)
#     tim.pendown()
####################


color_list = ["AntiqueWhite4", "blue4", "BlueViolet", "brown4", "burlywood4", "CadetBlue1", "chartreuse4", "chocolate4",
              "CornflowerBlue", "cyan3", "DarkGoldenrod", "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkRed",
              "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DeepPink", "gray10"]
# Challenge 3


# def drawing(sides):
#     initial_sides = 3
#     while initial_sides <= sides:
#         angle = 360 / initial_sides
#         tim.color(choice(color_list))
#         for _ in range(initial_sides):
#             tim.forward(100)
#             tim.left(angle)
#         initial_sides += 1
#
#
# drawing(10)

directions = [0, 90, 180, 270]
# My solution to the stroke size
# tim.width(10)
# Angela's solution to stroke size
tim.pensize(10)
tim.speed()
# Challenge 4
# My solution
# for _ in range(100):
#     tim.color(choice(color_list))
#     tim.forward(25)
#     tim.left(choice(directions))
#     tim.forward(25)

for _ in range(200):
    tim.color(choice(color_list))
    tim.forward(30)
    tim.setheading(choice(directions))


screen = Screen()
screen.exitonclick()
