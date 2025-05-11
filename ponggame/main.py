import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



POSITIONS = [(-350,0), (350,0)]

game_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

angle = random.randint(0,359)
r_paddle = Paddle((350,0))

l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

ball.setheading(angle)


screen.onkeypress(l_paddle.up, "w") 
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

speed = 0.1
while game_on:
    time.sleep(speed)
    screen.update()
    ball.move()
    
    #Detect collison with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        speed -= 0.01
        ball.bounce_x()

#Detect game over condition thorugh right paddle
    if ball.xcor() > 400:
        speed = 0.1
        scoreboard.l_point()
        ball.reset_screen()
        
    if ball.xcor() < -400:
        speed = 0.1
        scoreboard.r_point()
        ball.reset_screen()

    
    
screen.exitonclick()