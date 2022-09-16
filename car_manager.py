from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.new_x = 300
        self.starting_speed = STARTING_MOVE_DISTANCE
        self.increment_speed = MOVE_INCREMENT

    def create_car(self, x_value):
        random_y = random.randint(-240, 240)
        new_car = Turtle()
        new_car.setheading(180)
        new_car.penup()
        new_car.speed(0)
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=3)
        new_car.goto(x_value, random_y)
        self.cars.append(new_car)

    def random_car_gen(self):
        for _ in range(random.randint(0, 5)):
            self.create_car(self.new_x)
            self.new_x += random.randint(5, 20)
        self.new_x += random.randint(20, 60)

    def move_car(self, starting_speed):
        for car in self.cars:
            car.forward(starting_speed)

