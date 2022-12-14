from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        super().__init__()
        self.player = Turtle()

    def create_player(self):
        self.player.shape("turtle")
        self.player.color("black")
        self.player.penup()
        self.player.setheading(90)
        self.player.goto(STARTING_POSITION)

    def move_player(self):
        self.player.forward(MOVE_DISTANCE)

    def goto_starting(self):
        self.player.goto(STARTING_POSITION)
