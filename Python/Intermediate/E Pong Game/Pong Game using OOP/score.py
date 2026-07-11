import turtle

class Score:

    def __init__(self,sA,sB):
        self.score=turtle.Turtle()
        self.score_countA = sA
        self.score_countB = sB
        self.score_setup(self.score_countA, self.score_countB)

    def score_setup(self,scoreA, scoreB):
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(0, 180)
        self.score.color("white")
        self.score.pendown()
        self.score_countA = scoreA
        self.score_countB = scoreB
        self.score.write(f"A              B\n{self.score_countA}              {self.score_countB}", False, "center",("Arial", 20))
