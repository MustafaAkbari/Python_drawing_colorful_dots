import turtle
from turtle import Turtle, Screen
import random

# import colorgram
# rgb_colors = []
# color_list = colorgram.extract("image.jpg", 15)
# for color in color_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
turtle.colormode(255)
color_bank = [(230, 147, 73), (22, 43, 62), (25, 102, 135), (184, 15, 65), (191, 75, 29),
              (247, 234, 189), (243, 211, 50), (216, 172, 16), (62, 27, 7), (25, 136, 109),
              (234, 65, 35), (62, 21, 47), (21, 167, 140), (243, 213, 4), (16, 46, 32)]
window = Screen()
window.bgcolor("Black")
window.title("100 colorful dots")
dots = Turtle()
dots.speed("fastest")
dots.hideturtle()
dots.penup()
dots.setheading(225)
dots.forward(330)
dots.setheading(0)
# dots.showturtle()
end_0f_dots = 0
while end_0f_dots < 10:
    end_0f_dots += 1
    for number in range(10):
        dots.dot(25, random.choice(color_bank))
        dots.forward(50)
    dots.setheading(90)
    dots.forward(50)
    dots.setheading(180)
    dots.forward(500)
    dots.setheading(0)




window.mainloop()
