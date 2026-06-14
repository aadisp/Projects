from turtle import Turtle,Screen
import random

tommy=Turtle()
tommy.shape("turtle")
tommy.color("chartreuse4")
tim=Turtle()
tim.shape("turtle")
tim.color("chartreuse4")
# def color():
#     return random.uniform(0,1)
# for i in range(3,11):
#     color1=color()
#     color2=color()
#     color3=color()
#     tommy.pencolor(color1,color2,color3)
#     for j in range(i):
#         tommy.forward(100)
#         tommy.right(360 / i)

# tommy.speed(1000)
# tommy.pensize(10)
# tommy.color("red")
# tim.speed(1000)
# tim.pensize(10)
# def color():
#     return random.uniform(0,1)
# def direction():
#     return random.choice([90,0,180,270])
# while True:
#     tommy.left(direction())
#     tommy.forward(20)
#     # color1 = color()
#     # color2 = color()
#     # color3 = color()
#     # tommy.pencolor(color1, color2, color3)
#     tim.setheading(direction())
#     tim.forward(20)
#     color1 = color()
#     color2 = color()
#     color3 = color()
#     tim.pencolor(color1, color2, color3)


tommy.speed(100)

for i in range (361):
    if i%5==0:
        tommy.setheading(i)
        tommy.circle(100)
        tommy.pencolor(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))














screen=Screen()
screen.exitonclick()
