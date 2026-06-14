import turtle
import random
screen=turtle.Screen()
screen.setup(500,500)
bet=screen.textinput("What turtle do you bet on?","Violet|Indigo|Blue|Green|Yellow|Orange|Red").lower()

finishline=turtle.Turtle()
v=turtle.Turtle()
i=turtle.Turtle()
b=turtle.Turtle()
g=turtle.Turtle()
y=turtle.Turtle()
o=turtle.Turtle()
r=turtle.Turtle()

turtlelist=[v,i,b,g,y,o,r]
colorlist=["violet","indigo","blue","green","yellow","orange","red"]
positionlist=[200,200/1.5,200/3,0,-200/3,-200/1.5,-200]

finishline.hideturtle()
finishline.teleport(199,220)
finishline.setheading(270)
finishline.forward(440)

for i in range(0,7):
    turtlelist[i].penup()
    turtlelist[i].color(colorlist[i])
    turtlelist[i].goto(-200,positionlist[i])
    turtlelist[i].shape("turtle")
    turtlelist[i].speed(100)
pos=0
winner="none"
while pos<200:
    for trtle in turtlelist:
        trtle.forward(random.randint(1,10))
        pos=trtle.xcor()
        if pos>=200:
            winner=trtle.pencolor()
            break

if bet==winner:
    print("You win the bet.")
else:
    print("You lose the bet.")

























screen.exitonclick()