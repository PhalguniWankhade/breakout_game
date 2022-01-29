from turtle import Turtle
import random

BRICK_COLORS = ["red", "green", "blue", "cyan", "orange", "yellow", "violet"]
BRICK_WIDTHS = [1, 1.5, 2, 2.5, 3]
TOTAL_WALL_WIDTH = 780
BRICK_WALL_START_YCOR = 0

class Wall():
    def __init__(self) -> None:
        self.bricks = []
        for row in range(0,5):
            global prev_brick_color
            brick_row_width = 0
            wall_row_ycor = BRICK_WALL_START_YCOR + row*44
            prev_brick_color = BRICK_COLORS[0]
            while brick_row_width < TOTAL_WALL_WIDTH:
                stretch_len = random.choice(BRICK_WIDTHS)
                if stretch_len*20 + 4 + brick_row_width > TOTAL_WALL_WIDTH:
                    stretch_len = (TOTAL_WALL_WIDTH - brick_row_width) / 20
                new_brick = Brick(
                    y_cor=wall_row_ycor,
                    x_cor= brick_row_width - 400 + stretch_len*10 + 2,
                    length=stretch_len, 
                    prev_brick_color = prev_brick_color
                    )
                prev_brick_color = new_brick.color()[0]
                self.bricks.append(new_brick)
                brick_row_width += stretch_len*20 + 4

class Brick(Turtle):

    def __init__(self, y_cor, x_cor, length, prev_brick_color) -> None:
        super().__init__()
        brick_color = random.choice(BRICK_COLORS)
        if prev_brick_color == brick_color:
            self.color(BRICK_COLORS[(BRICK_COLORS.index(brick_color) + 1) % 7])
        else:
            self.color(brick_color)
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=length, outline=2)
        self.penup()
        self.goto(x_cor, y_cor)
