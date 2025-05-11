import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
scoreboard = Scoreboard()
player = Player()
carmanager = CarManager()

screen.onkey(player.move, "Up")
time_of_delay = 0.2

game_is_on = True
while game_is_on:
    time.sleep(time_of_delay)
    screen.update()
    carmanager.create_car()
    carmanager.move_cars()
    
    if player.ycor() > FINISH_LINE_Y:
        player.level_up()
        scoreboard.increment()
        carmanager.increase_speed(scoreboard.level)
        time_of_delay -= 0.001

    for car in carmanager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            