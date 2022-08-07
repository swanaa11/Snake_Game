from turtle import Turtle, Screen
screen = Screen()


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"score: {self.score}  High score:{self.high_score}", move=False, align="center", font=("Arial", 24, "normal"))

    def increase(self):
        self.score += 1
        self.clear()

        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data", mode="w") as file:

                file.write(f"{self.high_score}")

        self.score = 0
        self.update()
        # self.update_score()


