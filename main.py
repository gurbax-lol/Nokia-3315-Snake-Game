from turtle import Screen
from time import sleep
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
# screen.bgcolor("black")
screen.tracer(0)
screen.bgcolor("dark olive green")
screen.title("Nokia 3315 Snake Game")
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.generate_food()

















screen.exitonclick()