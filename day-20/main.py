from turtle import Turtle, Screen
import time

# Canvas
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

# Snake feed



# Snake body
snake_bodies = []
for position in starting_position:
    snake_body = Turtle(shape='square')
    snake_body.color('white')
    snake_body.penup()
    snake_body.goto(position)
    snake_bodies.append(snake_body)


# Game is on
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    for snake_body in snake_bodies:
        snake_body.forward(20)




screen.mainloop()