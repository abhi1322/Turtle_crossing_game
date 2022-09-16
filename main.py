import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
LEVEL = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("The turtle crossing Game")

player = Player()
player.create_player()

score_board = Scoreboard()

# Move player
screen.onkey(player.move_player, "Up")
car_manager = CarManager()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    score_board.create_score_board(LEVEL)
    random_value = random.randint(0, 4)
    if random_value == 1:
        car_manager.random_car_gen()
    car_manager.move_car(car_manager.starting_speed)

    if player.player.ycor() == 280:
        player.player.goto(0, -280)
        LEVEL += 1
        car_manager.starting_speed += car_manager.increment_speed
        score_board.clear_score_board()

    for car in car_manager.cars:
        if car.distance(player.player) < 35:
            car_manager.cars.clear()
            score_board.game_over()
            game_is_on = False

screen.exitonclick()
