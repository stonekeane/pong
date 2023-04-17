import turtle as t
from math import floor

playerAscore = 0
playerBscore = 0

window = t.Screen()
window.title("pong game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# creating left paddle
left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("blue")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)
left_paddle.direction = "stop"

# creating right paddle
right_paddle = t.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("red")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)
right_paddle.direction = "stop"

# creating ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.goto(5, 5)
ballxdirection = -0.2
ballydirection = 0.2

# creating pen
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align="center", font=("Arial", 24, "normal"))

def leftpaddleup():
    left_paddle.direction = "up"

def leftpaddledown():
    left_paddle.direction = "down"

def rightpaddleup():
    right_paddle.direction = "up"

def rightpaddledown():
    right_paddle.direction = "down"

# assign keys to move
window.listen()
window.onkeypress(leftpaddleup, "w")
window.onkeypress(leftpaddledown, "s")
window.onkeypress(rightpaddleup, "p")
window.onkeypress(rightpaddledown, "l")

while True:
    window.update()

    # moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    # setting up boarder

    if left_paddle.direction == "up" and left_paddle.ycor() < 250:
        left_paddle_y = left_paddle.ycor()
        left_paddle.sety(left_paddle_y + 0.5)
    elif left_paddle.direction == "down" and left_paddle.ycor() > -250:
        left_paddle_y = left_paddle.ycor()
        left_paddle.sety(left_paddle_y - 0.5)

    if right_paddle.direction == "up" and right_paddle.ycor() < 250:
        right_paddle_y = right_paddle.ycor()
        right_paddle.sety(right_paddle_y + 0.5)
    elif right_paddle.direction == "down" and right_paddle.ycor() > -250:
        right_paddle_y = right_paddle.ycor()
        right_paddle.sety(right_paddle_y - 0.5)

    # bounce off the top and bottom
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ballydirection = ballydirection*-1

    # when it gets to the side

    if floor(ball.xcor()) == floor(right_paddle.xcor()-10):
        if ball.ycor() < (right_paddle.ycor() + 30) and ball.ycor() > right_paddle.ycor() - 30:
            ballxdirection = ballxdirection*-1

    if floor(ball.xcor()) == floor(left_paddle.xcor()+10):
        if ball.ycor() <  (left_paddle.ycor() + 30) and ball.ycor() > left_paddle.ycor() - 30:
            ballxdirection = ballxdirection*-1


    if ball.xcor() > 390: # right width paddle border
        ball.goto(5, 5)
        ballxdirection = ballxdirection*-1
        playerAscore = playerAscore + 1
        pen.clear()
        score_string = "player A: {}             player B: {} ".format(playerAscore, playerBscore)
        pen.write(score_string,align="center",font=("Monaco", 24, "normal"))

    if ball.xcor() < -390: # right width paddle border
        ball.goto(5, 5)
        ballxdirection = ballxdirection*-1
        playerBscore = playerBscore + 1
        pen.clear()
        score_string = "player A: {}             player B: {} ".format(playerAscore, playerBscore)
        pen.write(score_string,align="center",font=("Monaco", 24, "normal"))




