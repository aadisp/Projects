import turtle

class SnakeScore:
    def __init__(self,hs):
        self.score = 0
        self.high_score = hs
        self.score_agent=turtle.Turtle()
        self.score_agent.penup()
        self.score_agent.goto(0,240)
        self.score_agent.hideturtle()
        self.score_display()
    def score_display(self):
        turtle.title(f"Score: {self.score}")
        self.score_agent.write(f"Score: {self.score} High Score: {self.high_score}",False,"center",font=("Arial", 24, "bold"))
    def highscore(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("high_score.txt", mode="w") as high_score:
                high_score.write(str(self.high_score))
    def reset(self):
        with open("high_score.txt", mode="w") as high_score:
            high_score.write("0")
