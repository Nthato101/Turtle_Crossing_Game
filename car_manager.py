from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []

    def create_car(self):
        number = random.randint(1, 5)
        if number == 3:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            color = random.choice(COLORS)
            car.color(color)
            car.setheading(180)
            y_cor = random.randint(-230, 230)
            car.goto(x=600, y=y_cor)
            self.cars.append(car)

    def car_move(self, level):
        if level == 1:
            for car in self.cars:
                car.forward(STARTING_MOVE_DISTANCE)
        else:
            for car in self.cars:
                car.forward(STARTING_MOVE_DISTANCE + ((level-1) * MOVE_INCREMENT))
