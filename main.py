import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Kart's Turtle Crossing!")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(fun=player.move, key='Up')
score = Scoreboard()
vehicles = CarManager()
game_is_on = True
while game_is_on:
    vehicles.moving_traffic()
    level_finished = player.check_pos()
    if level_finished:
        score.update_level()
        vehicles.increase_speed()
    for vehicle in vehicles.cars:
        if player.distance(vehicle.pos()) <= 20:
            game_is_on = False
            score.game_over()
            vehicles.clear_cars()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
