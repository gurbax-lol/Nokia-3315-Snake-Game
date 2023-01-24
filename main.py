from turtle import Turtle, Screen
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
# screen.bgcolor("black")
screen.tracer(0)
screen.bgcolor("dark olive green")
screen.title("Nokia 3315 Snake Game")

game_is_on = True
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("light gray")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

while game_is_on:
    screen.update()
    sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

















screen.exitonclick()