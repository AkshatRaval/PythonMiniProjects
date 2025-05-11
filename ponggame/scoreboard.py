import turtle as t


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__() 
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_Score = 0
        self.r_Score = 0
        self.update_board()
              
        
    def update_board(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_Score, align="center", font=("Arial", 25, "normal"))
        self.goto(100, 250)
        self.write(self.r_Score, align="center", font=("Arial", 25, "normal"))
    
    def l_point(self):
        self.l_Score += 1
        self.update_board()        
        
    def r_point(self):
        self.r_Score += 1
        self.update_board()        
