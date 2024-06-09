from turtle import Turtle, Screen
from snake import Snake
import time

# Canvas
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)


# Creating snake
snake = Snake()


# Moving snake
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')



# Snake feed

# Game is on
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

screen.mainloop()
