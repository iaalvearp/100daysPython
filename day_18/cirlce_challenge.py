import turtle as t
from random import randint
tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
t.speed(10)


def random_num():
    return randint(0, 255)


def random_color():
    r = random_num()
    g = random_num()
    b = random_num()
    rgb = (r, g, b)
    return rgb


for angle in range(0, 361, 10):
    tim.color(random_color())
    tim.seth(angle)
    tim.circle(100)


# Angela's solution - Focused in the gap between the circles
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/ size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(5)


screen.exitonclick()
