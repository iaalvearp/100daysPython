from random import randint, choice
import turtle as t
screen = t.Screen()
tim = t.Turtle()
t.colormode(255)
tim.pensize(10)


def random_num():
    return randint(0, 255)


def random_color():
    r = random_num()
    g = random_num()
    b = random_num()
    rgb = (r, g, b)
    return rgb


for _ in range(200):
    angle = choice([0, 90, 180, 270])
    tim.color(random_color())
    tim.forward(25)
    tim.setheading(angle)


screen.exitonclick()
