from turtle import Turtle
import random
MOVING_DISTANCE = 20

class Ball(Turtle):
    def __init__(self, shape = "circle"):
        super().__init__(shape)
        self.shapesize(1,1)
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        
    def reset_screen(self):
        self.goto(0,0)
        self.bounce_x()