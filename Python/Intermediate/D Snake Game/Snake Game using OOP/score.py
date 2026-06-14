import turtle

class SnakeScore:
    def __init__(self):
        self.score = 0
        self.score_agent=turtle.Turtle()
        self.score_agent.penup()
        self.score_agent.goto(0,240)
        self.score_agent.hideturtle()
        self.score_display()
    def score_display(self):
        turtle.title(f"Score: {self.score}")
        self.score_agent.write(f"Score: {self.score}",False,"center",font=("Arial", 24, "bold"))
