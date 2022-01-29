from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(0,-250)
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.001

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x,new_y)

    def bounce_y(self) -> None:
        self.y_move *= -1
    
    def bounce_x(self) -> None:
        # self.speed *= 0.9
        self.x_move *= -1
    
    def reset_position(self):
        self.setposition(0,-250)
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1
