from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:

    def __init__(self):
        super().__init__()
        self.level_text = Turtle()
        self.level_text.hideturtle()
        self.level_text.penup()

    def create_score_board(self, level):
        self.level_text.speed(0)
        self.level_text.goto(-280, 260)
        self.level_text.write(f"Level : {level}", font=FONT)

    def clear_score_board(self):
        self.level_text.clear()

    def game_over(self):
        game_over_text = Turtle()
        game_over_text.write("Game Over", True, align="center", font=FONT)
