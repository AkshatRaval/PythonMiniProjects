from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        tempVar = random.randint(1,6)
        print(tempVar)
        if tempVar == 1:
            new_car = Turtle()
            new_car.setheading(180)
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1,2)
            y_cor = random.randint(-250,250)
            new_car.goto(300, y_cor)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for cars in self.all_cars:
            cars.forward(STARTING_MOVE_DISTANCE)
    
    def increase_speed(self,level):
        for cars in self.all_cars:
            cars.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*level)
    
    