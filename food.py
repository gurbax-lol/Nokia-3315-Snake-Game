from turtle import Turtle
from random import randint, choice

# TODO: Build timeout functionality for superfoods

SUPER_FOOD_COLORS = ["medium violet red", "orange", "navajo white", "SteelBlue1"]


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


class SuperFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.generate_super_food()

    def generate_super_food(self):
        self.color(choice(SUPER_FOOD_COLORS))
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)
