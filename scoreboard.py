from turtle import Turtle

# Création du tableau de score


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score_paddle1 = 0
        self.score_paddle2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_paddle2, align='center', font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_paddle1, align='center', font=("Courier", 80, "normal"))

    def scored_paddle1(self):
        self.score_paddle1 += 1
        self.update_scoreboard()

    def scored_paddle2(self):
        self.score_paddle2 += 1
        self.update_scoreboard()
