import turtle

class Ball:

    def __init__(self,ballpos,ballhead):
        self.ball = turtle.Turtle()
        self.ball.shape("circle")
        self.ball.color("blue")
        self.ball.penup()
        self.ball.goto(ballpos)#R1
        self.ball.setheading(ballhead)#R1
