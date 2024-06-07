import turtle as t

tim = t.Turtle()

NUMBER_OF_SIDES = 10
STEP = 100


def draw_shape(NUMBER_OF_SIDES):
    angle = 360 / NUMBER_OF_SIDES
    for _ in range(NUMBER_OF_SIDES):
        tim.forward(STEP)
        tim.right(angle)


for shape in range(3, NUMBER_OF_SIDES + 1):
    draw_shape(shape)

screen = t.Screen()
screen.mainloop()
