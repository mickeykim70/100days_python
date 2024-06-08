from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
x_position = -230
end_position = 215
y_position = [125, 75, 25, -25, -75, -125]
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False


turtle_racers = []
for turtle_index in range(len(colors)):
    turtle_racer = Turtle(shape='turtle')
    turtle_racer.color(colors[turtle_index])
    turtle_racer.penup()
    turtle_racer.goto(x_position, y_position[turtle_index])
    turtle_racers.append(turtle_racer)

user_bet = screen.textinput(title='Betting', prompt='Enter a color? ')

if user_bet:
    is_race_on = True


def random_step():

    rand_step = random.randint(0, 10)
    return rand_step


while is_race_on:

    for turtle_racer in turtle_racers:

        if turtle_racer.xcor() > end_position:
            is_race_on = False
            winner_turtle = turtle_racer.pencolor()

            if winner_turtle == user_bet:
                print(f'You\'ve won! The winner is: {winner_turtle}')
            else:
                print(f'Lose! The winner is: {winner_turtle}')

        turtle_racer.penup()
        turtle_racer.forward(random_step())



screen.mainloop()





