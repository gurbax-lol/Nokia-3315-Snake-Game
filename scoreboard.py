from turtle import Turtle
FONT =('Consolas', 12, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"SCORE: {self.score}", move=False, align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
