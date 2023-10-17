import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.turn_left()
    if screen.onkey(player.move, "Up"):
        player.move()
    car_manager.create_car()
    car_manager.move_cars()
    if car_manager.collision(player):
        scoreboard.reset_score()
        player.reset_position()
        car_manager.reset_cars()
        car_manager.car_speed = 5
    if player.ycor() > 280:
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_score()


screen.exitonclick()
