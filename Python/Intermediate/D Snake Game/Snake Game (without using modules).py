def game():
    import turtle
    from turtle import Turtle
    import time
    import random
    screen=turtle.Screen()
    screen.setup(680,680)
    screen.bgcolor("black")
    screen.tracer(0)
    # grid= turtle.Turtle()
    # grid.penup()
    # grid.pencolor("white")
    # grid.goto(-300,300)
    # grid.pendown()
    # for i in range(-300,301):
    #     screen.update()
    #     time.sleep(0)
    #     if i%20==0:
    #         grid.goto(i,-300)
    #     grid.goto(i,300)
    # grid.goto(300,-300)
    # for i in range(-300,301):
    #     screen.update()
    #     time.sleep(0)
    #     if i%20==0:
    #         grid.goto(-300,i)
    #     grid.goto(300,i)


    x=0
    y=0
    turtle_list=[]
    fruit=Turtle()
    fruit.shape("square")
    fruit.shapesize(0.5)
    fruit.penup()
    fruit.color("white")
    for i in range(1,4):
        turtle = Turtle()
        turtle.speed(100)
        turtle.penup()
        turtle.color("white")
        turtle.goto(x,y)
        turtle.shape("square")
        turtle_list.append(turtle)
        turtle.penup()
        x=x-20
    def grow():
        turtle = Turtle()
        turtle.penup()
        turtle.color("white")
        last_turtle=turtle_list[len(turtle_list)-1]
        if last_turtle.heading()==90:
            x = last_turtle.xcor()
            y = last_turtle.ycor()-20
        elif last_turtle.heading()==0:
            x = last_turtle.xcor()-20
            y = last_turtle.ycor()
        elif last_turtle.heading()==180:
            x = last_turtle.xcor()+20
            y = last_turtle.ycor()
        elif last_turtle.heading()==270:
            x = last_turtle.xcor()
            y = last_turtle.ycor()+20
        turtle.goto(x, y)
        turtle.shape("square")
        turtle_list.append(turtle)

    def mv_forward():
        turtle_list[0].color("red")
        turtle_list[1].color("Orange")
        turtle_list[2].color("yellow")

        # for i in range(len(turtle_list)-1):
        for i in range(len(turtle_list) - 1, 0, -1):
            turtle_list[i].goto(turtle_list[i-1].xcor(),turtle_list[i-1].ycor())
            #print(f"{len(turtle_list)}-{i}-1:{len(turtle_list)-i-1}   {len(turtle_list)}-{i}-2:{len(turtle_list)-i-2}")
        # while type(turtle_list[0].xcor())!=int or type(turtle_list[0].ycor())!=int:
        #     print(turtle_list[0].xcor())
        #     print(turtle_list[0].ycor())
        #     xposs = int(turtle_list[0].xcor())
        #     yposs = int(turtle_list[0].ycor())
        #     if turtle_list[0].xcor()%20!=0 and turtle_list[0].ycor()%20!=0:
        #         turtle_list[0].setx(round(xposs,-1))
        #         turtle_list[0].sety(round(yposs,-1))
        #     elif turtle_list[0].xcor()%20!=0:
        #         turtle_list[0].setx(round(xposs,-1))
        #     else:
        #         turtle_list[0].sety(round(yposs,-1))
        turtle_list[0].forward(20)


    def up():
        if turtle_list[0].heading()!=270:
            turtle_list[0].setheading(90)
    def down():
        if turtle_list[0].heading()!=90:
            turtle_list[0].setheading(270)
    def left():
        if turtle_list[0].heading()!=0:
            turtle_list[0].setheading(180)
    def right():
        if turtle_list[0].heading()!=180:
            turtle_list[0].setheading(0)

    def reset():
        screen.reset()
        game()
        # if not game_on:
        #     # turtle_list[0].goto(0,0)
        #     # turtle_list[0].setheading(0)
        #     # gen_fruit()



    screen.listen()
    screen.onkeypress(grow,"e")
    screen.onkeypress(up,"Up")
    screen.onkeypress(down,"Down")
    screen.onkeypress(left,"Left")
    screen.onkeypress(right,"Right")
    screen.onkeypress(reset,"z")

    border = Turtle()
    border.hideturtle()
    border.penup()
    border.goto(-320, 320)
    border.pendown()
    border.pensize(5)
    border.pencolor("white")
    def draw_border():
        border.goto(320,320)
        border.goto(320,-320)
        border.goto(-320,-320)
        border.goto(-320,320)
    draw_border()

    def border_alert():
        if (-180 > turtle_list[0].xcor() or turtle_list[0].xcor() > 180) or (-180 > turtle_list[0].ycor() or turtle_list[0].ycor() > 180):
            border.pencolor("pink")
            draw_border()
            if (-220 > turtle_list[0].xcor() or turtle_list[0].xcor() > 220) or (-220 > turtle_list[0].ycor() or turtle_list[0].ycor() > 220):
                border.pencolor("yellow")
                draw_border()
                if (-260 > turtle_list[0].xcor() or turtle_list[0].xcor() > 260) or (-260 > turtle_list[0].ycor() or turtle_list[0].ycor() > 260):
                    border.pencolor("orange")
                    draw_border()
        else:
            border.pencolor("white")
            draw_border()

    position_list=[]
    for i in range(-280,281):
        if i%20==0:
            position_list.append(i)
    #print(position_list)

    def gen_fruit():
        xpos=random.choice(position_list)
        ypos=random.choice(position_list)
        #print(xpos)
        #print(ypos)
        fruit.goto(xpos,ypos)
    gen_fruit()





    game_on=True
    while game_on:
        screen.update()
        time.sleep(0.1)
        if -300<turtle_list[0].xcor()<300 and -300<turtle_list[0].ycor()<300:
            mv_forward()
            border_alert()
        else:
            border.pencolor("red")
            draw_border()
            game_on = False

        if fruit.xcor()-20<turtle_list[0].xcor()<fruit.xcor()+20 and fruit.ycor()-20<turtle_list[0].ycor()<fruit.ycor()+20:
            grow()
            gen_fruit()
        for turt in turtle_list:
            if turt.xcor()-20<turtle_list[0].xcor()<turt.xcor()+20 and turt.ycor()-20<turtle_list[0].ycor()<turt.ycor()+20 and turt!=turtle_list[0]:
                game_on=False


    screen.exitonclick()
game()
