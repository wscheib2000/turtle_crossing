import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import choice

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.up, key="Up")

game_on = True
while game_on:
    if choice(range(1,6)) == 1:
        car_manager.create_car()

    if player.finished():
        scoreboard.increment()
        car_manager.speed_up()
        player.go_to_start()

    if car_manager.is_collision(player):
        game_on = False
        scoreboard.game_over()

    car_manager.move_cars()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()