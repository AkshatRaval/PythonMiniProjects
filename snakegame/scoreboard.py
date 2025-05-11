from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./snakegame/data.txt") as data:
            self.highscore = int(data.read()) 
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 14, "normal"))
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("./snakegame/data.txt", mode="w") as data:
            data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
        
    def scoreup(self):
        self.score += 1
        self.update_scoreboard()
        