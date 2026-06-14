import turtle
import random
tommy=turtle.Turtle()

k=-200
tommy.teleport(-300,k)
tommy.hideturtle()
for i in range(10):
    for j in range(10):
        tommy.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        if random.randint(0,8)!=0:
            tommy.dot(20)
        else:
            pass
        tommy.penup()
        tommy.forward(50)
    k=k+50
    tommy.teleport(-300, k)







screen=turtle.Screen()
screen.exitonclick()