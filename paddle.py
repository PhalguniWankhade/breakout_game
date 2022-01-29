from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cor, y_cor) -> None:
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.color("maroon")
        self.penup()
        self.goto(x_cor, y_cor)
    
    def go_left(self):
        new_x = self.xcor() - 50
        if new_x > -400:
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 50
        if new_x < 400:
            self.goto(new_x, self.ycor())
