from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
# screen.bgcolor("black")
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
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    # Detect eating food
    if snake.head.distance(food) < 15:
        food.generate_food()
        scoreboard.increase_score()
    # Detect running into a wall,
    # disable this if you want to play the version where the snake does not collide with the wall
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     game_is_on = False
    #     scoreboard.game_over()
    # Start from the opposite edge if the snake has reached the screen's edge
    if snake.head.xcor() > 290:  # If the snake has reached the left edge,
        snake.head.goto(-290, snake.head.ycor())  # loop over to the right edge.
    if snake.head.xcor() < -290:  # If the snake has reached the right edge,
        snake.head.goto(290, snake.head.ycor())  # loop over to the left edge.
    if snake.head.ycor() > 290:  # If the snake has reached the up edge,
        snake.head.goto(snake.head.xcor(), -290)  # loop over to the down edge.
    if snake.head.ycor() < -290:  # If the snake has reached the down edge,
        snake.head.goto(snake.head.xcor(), 290)  # loop over to the up edge.
















screen.exitonclick()