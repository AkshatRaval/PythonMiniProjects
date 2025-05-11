import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.2)
    
    snake.move()
    if snake.head.distance(food) < 15:
        food.random_loc()
        snake.extend()
        scoreboard.scoreup()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280  or snake.head.ycor() > 280:
        scoreboard.reset()
        snake.reset()
       
    for segments in snake.segments[2:]:
        if snake.head.distance(segments) < 10:
            snake.reset()
            scoreboard.reset()
            
