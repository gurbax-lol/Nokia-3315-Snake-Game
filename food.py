from turtle import Turtle
from random import randint, choice
from time import sleep
#TODO: Generate Super Food

# SUPER_FOOD_COLORS = ["medium violet red", "orange", "navajo white", "SteelBlue1"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.generate_food()

    def generate_food(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)


# class SuperFood(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("triangle")
#         self.penup()
#         self.shapesize(stretch_len=0.5, stretch_wid=0.5)
#         self.color(choice(SUPER_FOOD_COLORS))
#         self.generate_food()
#
#
#     def generate_food(self):
#         rand_x = randint(-280, 280)
#         rand_y = randint(-280, 280)
#         self.goto(rand_x, rand_y)
#
