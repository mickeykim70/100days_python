import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

NUMBER_OF_CIRCLES = 50
RADIUS = 100

tim.home()
tim.position()
tim.speed("fastest")

# COLORS
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_color = (r,g,b)
    return rand_color

angle = 0
for _ in range(NUMBER_OF_CIRCLES):
    angle = angle + 360 / NUMBER_OF_CIRCLES
    tim.color(random_color())
    tim.setheading(angle)
    tim.circle(RADIUS)


screen = t.Screen()
screen.mainloop()