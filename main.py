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
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.move()


screen.exitonclick()
