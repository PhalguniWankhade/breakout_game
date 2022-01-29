from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("White")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.goto(-10, 250)
        self.write(f"Score: {self.score}", move=False, align=ALLIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"You Won!Your score is {self.score}", move=False, align=ALLIGNMENT, font=("Courier", 16, "normal"))

    def point(self):
        self.score += 1
        self.clear()
        self.update_score()