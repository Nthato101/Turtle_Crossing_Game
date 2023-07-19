import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1200, height=600)
screen.tracer(0)
level = 1
player = Player()
car = CarManager()
stage = Scoreboard(level)
stage.level_update(level)

game_is_on = True
while game_is_on:

    car.create_car()
    time.sleep(0.1)
    screen.update()
    screen.listen()
    car.car_move(level=level)

    screen.onkeypress(key="Up", fun=player.crossing_forward)

    if player.ycor() > 290:
        player.restart()
        level += 1
        stage.level_update(level)

    for veh in car.cars:
        if veh.distance(player) < 20:
            stage.game_over()
            game_is_on = False

screen.exitonclick()
