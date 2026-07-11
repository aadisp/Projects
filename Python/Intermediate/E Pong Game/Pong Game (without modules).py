# import statements
import turtle
import random
import time

#main file
#global values
x=0
y=0
angle=0
defender=""
gamep=True
gameb=True
score = turtle.Turtle()
score_countA=0
score_countB=0
ballpos=(0,0)#R1
ballhead=0#R1
towards="Paddle"#R1
game="New"#R1

screen = turtle.Screen()
screen.setup(1000, 600)
screen.bgcolor("black")

difficulty=screen.textinput("Choose difficulty:","Easy (E)\nMedium (M)\nHard(H)")
print(difficulty)
if difficulty=="E":
    sleep_time=0.01
    d=20
    stopup=240
    stopdown=-240
elif difficulty=="M":
    sleep_time=0.006
    d=40
    stopup=240
    stopdown=-220
else:
    sleep_time=0.003
    d=60
    stopup=220
    stopdown=-200

screen.clear()
#main file END

def pong(scoreA,scoreB,paddleA,paddleB,blpos,blhed,gm,twrds):#R1
    global x,y,gamep,gameb,defender,score,d,stopup,stopdown,ballpos,ballhead,game,towards#R1

    ballpos=blpos#R1
    ballhead=blhed#R1
    game=gm#R1
    towards=twrds#R1

    ##
    # I Arena Setup
    # screen setup
    screen = turtle.Screen()
    screen.setup(1000, 600)
    screen.bgcolor("black")
    screen.tracer(0)

    # border setup
    border = turtle.Turtle()
    border.hideturtle()
    border.penup()
    border.goto(-450, 250)
    border.color("white")
    border.pendown()
    border.goto(450, 250)
    border.goto(450, -250)
    border.goto(-450, -250)
    border.goto(-450, 250)
    border.penup()
    border.goto(0, 250)
    border.pendown()
    border.goto(0, -250)
    # score setup (CHANGE)
    score.hideturtle()
    score.penup()
    score.goto(0, 180)
    score.color("white")
    score.pendown()
    score_countA = scoreA
    score_countB = scoreB
    score.write(f"A              B\n{score_countA}              {score_countB}", False, "center", ("Arial", 20))
    # paddle setup
    py = paddleB
    paddle_B_list = []
    for i in range(4):
        paddle_B = turtle.Turtle()
        paddle_B.shape("square")
        paddle_B.color("white")
        paddle_B.penup()
        paddle_B.goto(400, py)
        paddle_B.setheading(90)
        py += 20
        paddle_B_list.append(paddle_B)
    py = paddleA
    paddle_A_list = []
    for i in range(4):
        paddle_A = turtle.Turtle()
        paddle_A.shape("square")
        paddle_A.color("white")
        paddle_A.penup()
        paddle_A.goto(-400, py)
        paddle_A.setheading(90)
        py += 20
        paddle_A_list.append(paddle_A)
    # ball setup (CHANGE)
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.goto(ballpos)#R1
    ball.setheading(ballhead)#R1

    # screen.tracer(1)
    # I END

    # *movep*
    def movep():
        global x, y, angle, defender, gamep, gameb, score, score_countA, score_countB
        angle = ball.towards(x, y)
        ball.setheading(angle)
        # throwing ball
        while gamep:
            screen.update()
            time.sleep(sleep_time)
            ball.forward(5)
            if defender == "B":
                # checking if the ball has hit the paddle
                if ball.xcor() >= 380:
                    if paddle_B_list[0].ycor() - 30 <= ball.ycor() <= paddle_B_list[-1].ycor() + 30:
                        defender = "A"
                        print("Paddle B")
                        IV()
                    else:
                        print("Miss B")
                        while ball.xcor() < 480:
                            screen.update()
                            time.sleep(sleep_time)
                            ball.forward(5)
                        gamep = False
                        gameb = False
                        # score.clear()
                        score_countA += 1
                        reset(score_countA,score_countB)
                        # score.write(f"A              B\n{score_countA}              {score_countB}", False, "center",("Arial", 20))
            else:
                # checking if the ball has hit the paddle
                if ball.xcor() <= -380:
                    if paddle_A_list[0].ycor() - 30 <= ball.ycor() <= paddle_A_list[-1].ycor() + 30:
                        defender = "B"
                        print("Paddle A")
                        IV()
                    else:
                        print("Miss A")
                        while ball.xcor() > -480:
                            screen.update()
                            time.sleep(sleep_time)
                            ball.forward(5)
                        gamep = False
                        gameb = False
                        # score.clear()
                        score_countB += 1
                        reset(score_countA,score_countB)
                        # score.write(f"A              B\n{score_countA}              {score_countB}", False, "center",("Arial", 20))
    # *movep* END

    # *moveb*
    def moveb():
        global x, y, angle, gameb
        angle = ball.towards(x, y)
        ball.setheading(angle)
        while gameb:
            screen.update()
            time.sleep(sleep_time)
            ball.forward(5)
            if y == 240:
                # if the ball has hit the border
                if ball.ycor() >= 240:
                    V()
            else:
                # if the ball has hit the border
                if ball.ycor() <= -240:
                    V()
    # *moveb* END

    # IV Bounce off paddle
    def IV():
        global x, y, angle,towards#R1
        # towards paddle
        if random.choice([0, 1]):
            x = x * -1
            y = random.randint(-220, 220)
            # ->*movep*
            towards="Paddle"#R1
            movep()
        # towards border
        else:
            x = random.randint(-340, 340)
            y = random.choice([-240, 240])
            # *moveb*
            towards="Border"#R1
            moveb()

    # V Bounce off border
    def V():
        global x, y, angle, defender,towards#R1
        if random.choice([0, 1]):
            if defender == "A":
                x = -380
            else:
                x = 380
            y = random.randint(-220, 220)
            # ->*movep*
            towards="Paddle"#R1
            movep()
        else:
            if defender == "A":
                x = -random.randint(-340, x)
            else:
                x = -random.randint(x, 340)
            # ->*moveb*
            towards="Border"#R1
            moveb()

    def reset(sA,sB):
        if sA!=10 and sB!=10:
            screen.clear()
            pong(sA, sB, paddle_A_list[0].ycor(), paddle_B_list[0].ycor(),(0,0),0,"New","Paddle")#R1
        else:
            if sA==10:
                endgame("A",sA,sB)
            else:
                endgame("B",sA,sB)
    def endgame(winner,sA,sB):
        screen.clear()
        screen.bgcolor("black")
        screen.tracer(0)

        # border setup
        border = turtle.Turtle()
        border.hideturtle()
        border.penup()
        border.goto(-450, 250)
        border.color("white")
        border.pendown()
        border.goto(450, 250)
        border.goto(450, -250)
        border.goto(-450, -250)
        border.goto(-450, 250)
        border.penup()
        score=turtle.Turtle()
        score.hideturtle()
        score.penup()
        score.goto(0, 180)
        score.color("white")
        score.pendown()
        score.write(f"A              B\n{sA}              {sB}", False, "center", ("Arial", 20))
        end_screen = turtle.Turtle()
        end_screen.hideturtle()
        end_screen.penup()
        end_screen.color("white")
        end_screen.pendown()
        end_screen.write(f"Game Over", False, "center", ("Arial", 20))
        end_screen.penup()
        end_screen.goto(0, -50)
        end_screen.pendown()
        end_screen.write(f"Winner: {winner}", False, "center", ("Arial", 15))
        screen.update()

    def restart():
        screen.clear()
        pong(0, 0, -20, -20,(0,0),0,"New","Paddle")#R1
    def pause():
        global ballpos,ballhead,game,towards#R1
        screen.textinput("||","Escape         -     Pause/Play\nSpace          -     End Game\nx                -     Reset Game\n\n        Paddle A    Paddle B\nUp        w           Up Arrow\nDown   s           Down Arrow")
        ballpos=ball.pos()#R1
        ballhead=ball.heading()#R1
        game="Resumed"#R1
        screen.clear()#R1
        pong(score_countA,score_countB,paddle_A_list[0].ycor(), paddle_B_list[0].ycor(),ballpos,ballhead,game,towards)#R1
    def stop():
        if score_countB<score_countA:
            winner="A"
        else:
            winner="B"
        endgame(winner,score_countA,score_countB)
        screen.exitonclick()

    def w():
        if paddle_A_list[-1].ycor() < stopup:
            paddle_A_list[-1].forward(d)
            for i in range(2, len(paddle_A_list)+1):
                paddle_A_list[len(paddle_A_list) - i].goto(-400, paddle_A_list[len(paddle_A_list) - i+1].ycor()-20)
    def s():
        if paddle_A_list[0].ycor() > stopdown:
            paddle_A_list[0].backward(d)
            for i in range(1, len(paddle_A_list)):
                paddle_A_list[i].goto(-400, paddle_A_list[i - 1].ycor()+20)
    def up():
        if paddle_B_list[-1].ycor() < stopup:
            paddle_B_list[-1].forward(d)
            for i in range(2, len(paddle_B_list) + 1):
                paddle_B_list[len(paddle_B_list)-i].goto(400, paddle_B_list[len(paddle_B_list)-i + 1].ycor()-20)
    def down():
        if paddle_B_list[0].ycor() > stopdown:
            paddle_B_list[0].backward(d)
            for i in range(1,len(paddle_B_list)):
                paddle_B_list[i].goto(400, paddle_B_list[i - 1].ycor()+20)

    screen.listen()
    screen.onkeypress(restart,"x")
    screen.onkeypress(pause,"Escape")
    screen.onkeypress(stop,"space")
    screen.onkeypress(w, "w")
    screen.onkeypress(s, "s")
    screen.onkeypress(up, "Up")
    screen.onkeypress(down, "Down")

    if game=="New":#R1
        # II Game Start (CHANGE)
        defender = ""
        angle = 0
        gamep = True
        gameb = True

        # throw the ball to x=-380 or 380 and y = from -220 to 220
        # setting direction
        x = random.choice([-380, 380])
        if x == -380:
            defender = "A"
        else:
            defender = "B"
        y = random.randint(-220, 220)
        towards = "Paddle"#R1
        movep()
    else:#R1
        if towards=="Paddle":#R1
            towards="Paddle"#R1
            movep()#R1
        else:#R1
            towards="Border"#R1
            moveb()#R1
        print(ball.heading())#R1

    screen.exitonclick()
    ##
pong(score_countA,score_countB,-20,-20,ballpos,ballhead,game,towards)#R1

