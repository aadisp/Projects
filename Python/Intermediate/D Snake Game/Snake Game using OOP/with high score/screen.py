import turtle
import score

class Display:
    def __init__(self):
        self.disp=turtle.Screen()
        self.disp.clear()
        self.disp.bgcolor(1.0, 0.7607843137254902, 0.25098039215686274)
        self.disp.setup(640,640)
        self.border=turtle.Turtle()
        self.create_border("white")
        self.disp.tracer(0)
    def update(self):
        self.disp.update()
    def close(self):
        msg = turtle.Turtle()
        msg.penup()
        msg.write("Press z to restart\nPress x to reset", False, "center",font=("Arial", 20, "normal"))
        msg.hideturtle()
        self.disp.exitonclick()
    def create_border(self,clr):
        self.border.color(clr)
        self.border.speed(0)
        self.border.pensize(5)
        self.border.penup()
        self.border.hideturtle()
        self.border.goto(-300,300)
        self.border.pendown()
        self.border.goto(300,300)
        self.border.goto(300,-300)
        self.border.goto(-300,-300)
        self.border.goto(-300,300)
