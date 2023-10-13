FONT = ("Courier", 24, "normal")
from turtle import Turtle
from player import Player


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.scoreboard = Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(-260, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(
            f"Level: {self.score}",
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.scoreboard.goto(0, 0)
        self.scoreboard.write("GAME OVER", align="center", font=FONT)
