import turtle 
from brickwall import Wall, Brick
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(800,600)
screen.title("Breakout Game")
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle(0, -280)
ball = Ball()
wall = Wall()

turtle.update()

screen.listen()
screen.onkey(paddle.go_left,"Left")
screen.onkey(paddle.go_right,"Right")


scoreboard = ScoreBoard()
bricks_visible = len(wall.bricks)
game_is_on = True
while game_is_on:
    time.sleep(ball.speed)
    ball.move()
    if ball.ycor() > 280:
        ball.bounce_y()
    if ball.xcor() > 370 or ball.xcor() < -370 :
        ball.bounce_x()
    # Collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -260:
        ball.bounce_y()
    # Collision with brick
    for brick in wall.bricks:
        if brick.isvisible() and ball.distance(brick) < 50:
            brick_width = 20*brick.shapesize()[1] + 4
            brick_height = 40
            brick_x_cor_range = range(int(brick.xcor() - brick_width // 2), 1 + int(brick.xcor() + brick_width // 2))
            brick_y_cor_range = range(int(brick.ycor() - brick_height // 2), 1 + int(brick.ycor() + brick_height // 2))
            if ball.xcor() in brick_x_cor_range \
                and ((ball.ycor() >= brick.ycor() + 10) or (ball.ycor() <= brick.ycor() - 10)):
                ball.bounce_y()
                brick.hideturtle()
                bricks_visible -=1
                scoreboard.point()
            elif ball.ycor() in brick_y_cor_range \
                and ((ball.xcor() >= brick.xcor() - (10 +brick_width // 2)) \
                or (ball.xcor() <= brick.xcor() + (10 +brick_width // 2))):
                ball.bounce_x()
                brick.hideturtle()
                bricks_visible -=1
                scoreboard.point()
    # Ball goes out of bounds
    if ball.ycor() < -280:
        ball.reset_position()
    turtle.update()
    if bricks_visible == 0:
        game_is_on = False
        ball.reset_position()
        scoreboard.game_over()
screen.exitonclick()


