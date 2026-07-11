import turtle

class Paddle:

    def __init__(self,paddleA,paddleB):
        self.py=paddleB
        self.paddle_B_list = []
        for i in range(4):
            self.paddle_B = turtle.Turtle()
            self.paddle_B.shape("square")
            self.paddle_B.color("white")
            self.paddle_B.penup()
            self.paddle_B.goto(400, self.py)
            self.paddle_B.setheading(90)
            self.py += 20
            self.paddle_B_list.append(self.paddle_B)

        self.py = paddleA
        self.paddle_A_list = []
        for i in range(4):
            self.paddle_A = turtle.Turtle()
            self.paddle_A.shape("square")
            self.paddle_A.color("white")
            self.paddle_A.penup()
            self.paddle_A.goto(-400, self.py)
            self.paddle_A.setheading(90)
            self.py += 20
            self.paddle_A_list.append(self.paddle_A)
