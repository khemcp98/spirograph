import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.pensize(1)
tim.speed(0)
# color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#          "SeaGreen"]


def ran_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(no_of_gap):

    for i in range(360 // no_of_gap):
        tim.color(ran_color())
        tim.circle(50)
        tim.setheading(tim.heading() + no_of_gap)


# choose = int(input("enter the size of gap between circles"))
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
