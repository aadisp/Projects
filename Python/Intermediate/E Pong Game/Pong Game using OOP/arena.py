import turtle
import score
import paddle
import ball

class Arena:

    def __init__(self,scoreA, scoreB,paddleA,paddleB,ballpos,ballhead):
        #screen setup
        self.screen = turtle.Screen()
        self.screen.setup(1000, 600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        # border setup
        self.border = turtle.Turtle()
        self.border.hideturtle()
        self.border.penup()
        self.border.goto(-450, 250)
        self.border.color("white")
        self.border.pendown()
        self.border.goto(450, 250)
        self.border.goto(450, -250)
        self.border.goto(-450, -250)
        self.border.goto(-450, 250)
        self.border.penup()
        self.border.goto(0, 250)
        self.border.pendown()
        self.border.goto(0, -250)

        #score board setup
        self.score_manager = score.Score(scoreA, scoreB)

        #paddle setup
        self.paddle_setup=paddle.Paddle(paddleA,paddleB)

        #ball setup
        self.ball_manager=ball.Ball(ballpos,ballhead)

    def endgame(self,winner, sA, sB):
        self.screen.clear()
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        self.border = turtle.Turtle()
        self.border.hideturtle()
        self.border.penup()
        self.border.goto(-450, 250)
        self.border.color("white")
        self.border.pendown()
        self.border.goto(450, 250)
        self.border.goto(450, -250)
        self.border.goto(-450, -250)
        self.border.goto(-450, 250)
        self.border.penup()

        self.score_manager = score.Score(sA, sB)

        end_screen = turtle.Turtle()
        end_screen.hideturtle()
        end_screen.penup()
        end_screen.color("white")
        end_screen.pendown()
        end_screen.write(f"Game Over", False, "center", ("Arial", 20))
        end_screen.penup()
        end_screen.goto(0, -50)
        end_screen.pendown()
        end_screen.write(f"{winner}", False, "center", ("Arial", 15))

        self.screen.update()
