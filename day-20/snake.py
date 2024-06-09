from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.snake_bodies = []
        self.create_snake()
        self.head = self.snake_bodies[0]

    def create_snake(self):
        # Snake body
        for position in STARTING_POSITION:
            snake_body = Turtle(shape='square')
            snake_body.color('white')
            snake_body.penup()
            snake_body.goto(position)
            self.snake_bodies.append(snake_body)


    def move(self):
        for snake_body_segment_index in range(len(self.snake_bodies) - 1, 0, -1):
            new_x_position = self.snake_bodies[snake_body_segment_index - 1].xcor()
            new_y_position = self.snake_bodies[snake_body_segment_index - 1].ycor()
            self.snake_bodies[snake_body_segment_index].goto(new_x_position, new_y_position)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

