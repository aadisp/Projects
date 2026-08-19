import turtle
import random

class SnakeBody:
    def __init__(self):
        self.snake_organ_list=[]
        for i in range(0, -60, -20):
            self.snake=turtle.Turtle()
            self.snake.color("white")
            self.snake.penup()
            self.snake.shape("square")
            self.snake.goto(i, 0)
            self.snake_organ_list.append(self.snake)
            self.length=len(self.snake_organ_list)

    def move(self):
        for i in range(self.length-1,0,-1):
            if i!=0:
                x=self.snake_organ_list[i-1].xcor()
                y=self.snake_organ_list[i-1].ycor()
                self.snake_organ_list[i].goto(x,y)
        self.snake_organ_list[0].forward(20)

    def up(self):
        if self.snake_organ_list[0].heading()!=270 and self.snake_organ_list[0].heading()!=90:
            self.snake_organ_list[0].setheading(90)
    def down(self):
        if self.snake_organ_list[0].heading()!=270 and self.snake_organ_list[0].heading()!=90:
            self.snake_organ_list[0].setheading(270)
    def left(self):
        if self.snake_organ_list[0].heading() != 180 and self.snake_organ_list[0].heading() != 0:
            self.snake_organ_list[0].setheading(180)
    def right(self):
        if self.snake_organ_list[0].heading()!=180 and self.snake_organ_list[0].heading()!=0:
            self.snake_organ_list[0].setheading(0)

    def grow(self):
        self.snake = turtle.Turtle()
        self.snake.penup()
        self.snake.goto(self.snake_organ_list[self.length-1].xcor(),self.snake_organ_list[self.length-1].ycor())
        self.snake.color("white")
        self.snake.shape("square")
        self.snake_organ_list.append(self.snake)
        self.length = len(self.snake_organ_list)

    def rainbow(self,life):
        if life!="dead":
            for organ in self.snake_organ_list:
                x = random.uniform(1, 1)
                y = random.uniform(0, 1)
                z = random.uniform(0, 1)
                organ.color(x, y, y)
        else:
            for organ in self.snake_organ_list:
                organ.color("red")
