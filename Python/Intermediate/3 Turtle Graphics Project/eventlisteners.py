import turtle as trtl
tommy=trtl.Turtle()
screen=trtl.Screen()
screen.setup(200,300)

def forwards():
    tommy.forward(10)
def left():
    tommy.left(10)
def back():
    tommy.backward(10)
def right():
    tommy.right(10)
screen.listen()
def clear():
    tommy.teleport(0,0)
    tommy.setheading(0)
    tommy.clear()

screen.onkey(forwards,"w")
screen.onkey(left,"a")
screen.onkey(back,"s")
screen.onkey(right,"d")
screen.onkey(clear,"BackSpace")














screen.exitonclick()