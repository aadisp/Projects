import turtle
import random
class Food:
    def __init__(self):
        self.apple=turtle.Turtle()
        self.apple.shape("circle")
        self.apple.shapesize(0.5)
        self.apple.penup()
        self.apple.color("red")
        self.x=[]
        self.y=[]
        for i in range(-280,300,20):
            self.x.append(i)
            self.y.append(i)
        self.gen_food()
        self.apple.goto(random.choice(self.x), random.choice(self.y))

    def gen_food(self):
        self.apple.goto(random.choice(self.x), random.choice(self.y))
