from turtle import Turtle
FONT = ('Consolas', 12, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score} High Score: {self.high_score}", move=False, align='center', font=FONT)

    def increase_score(self, value):
        self.score += value
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                self.high_score = file.write(str(self.score))
        self.score = 0
