import turtle as t
from color_wizard import color_rgb_list
import random as r

stamp = t.Turtle()
screen = t.Screen()
stamp.speed("fastest")
stamp.hideturtle()
t.colormode(255)


def set_colour():
    color = r.choice(color_rgb_list)
    stamp.color(color)


def painting():
    screen.screensize(700, 700)
    for y_coord in range(-250, 250, 50):
        for x_coord in range(-250, 250, 50):
            stamp.teleport(x_coord, y_coord)
            set_colour()
            stamp.dot(20)
    screen.exitonclick()


# stamp.shape("circle")
# stamp.stamp()
# for step in range(10):
#     stamp.stamp()
#     stamp.forward(20)
#     stamp.stamp()
#     stamp.forward(20)
# screen.exitonclick()

painting()
