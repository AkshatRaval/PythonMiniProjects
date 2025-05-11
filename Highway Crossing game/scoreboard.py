from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-220,260)
        self.update_board()
        
        
    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)
        
    def game_over(self):
        self.goto()
        self.write(f"GAME OVER", align="center", font=FONT)
        
    def increment(self):
        self.level += 1
        self.update_board()