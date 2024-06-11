from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Canvas
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)


# Creating snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# Moving snake
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


# Game is on
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 18:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_tail()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with itself
    for snake_body_segment in snake.snake_body[1:]:
        if snake.head.distance(snake_body_segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.mainloop()
