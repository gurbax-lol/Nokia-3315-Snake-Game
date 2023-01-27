from turtle import Screen
from time import sleep
from snake import Snake
from food import Food, SuperFood
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("dark olive green")
screen.title("Nokia 3315 Snake Game")
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
superfood = SuperFood()


def detect_wall_collision():
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        global game_is_on
        game_is_on = False
        scoreboard.reset()


def loop_over_walls():
    if snake.head.xcor() > 290:  # If the snake has reached the right edge,
        snake.head.goto(-290, snake.head.ycor())  # loop over to the left edge.

    if snake.head.xcor() < -290:  # If the snake has reached the left edge,
        snake.head.goto(290, snake.head.ycor())  # loop over to the right edge.

    if snake.head.ycor() > 290:  # If the snake has reached the up edge,
        snake.head.goto(snake.head.xcor(), -290)  # loop over to the down edge.

    if snake.head.ycor() < -290:  # If the snake has reached the down edge,
        snake.head.goto(snake.head.xcor(), 290)  # loop over to the up edge.


while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    # Detect eating food
    if snake.head.distance(food) < 15:
        food.generate_food()
        scoreboard.increase_score(1)
        snake.extend()
    if snake.head.distance(superfood) < 15:
        scoreboard.increase_score(5)
        superfood.generate_super_food()
        snake.extend()
    # Detect running into a wall,
    detect_wall_collision()
    # Start from the opposite edge if the snake has reached the screen's edge
    # loop_over_walls()
    # Detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
