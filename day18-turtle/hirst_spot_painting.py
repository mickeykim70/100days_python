#Picking up the colors
# import colorgram
#
# # Extract 30 colors from an image.
# colors = colorgram.extract('./spotpainting.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
#
# print(rgb_colors)
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()
screen.screensize(800, 800)

color_list = [(250, 228, 17), (199, 12, 35), (213, 13, 9), (232, 228, 5), (198, 68, 20), (32, 90, 188), (43, 212, 72),
              (234, 149, 41), (33, 30, 153), (240, 246, 251), (16, 22, 55), (66, 9, 49), (244, 39, 148), (65, 202, 229),
              (14, 205, 222), (63, 21, 10), (224, 19, 111), (230, 164, 8), (15, 154, 22), (245, 59, 16), (98, 75, 9),
              (248, 11, 9), (223, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

# Go to first position
tim.penup()
y_pos = -250

for _ in range(10):
    tim.setposition(-250, y_pos)
    for _ in range(10):
        tim.setheading(0)
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

    y_pos += 50

screen.mainloop()

