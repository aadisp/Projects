import time
import random
import arena

class Pong:

    def __init__(self,sleep_time,d,stopup,stopdown):
        self.x=0
        self.y=0
        self.angle=0
        self.sleep_time=sleep_time

        self.defender=""

        self.gamep=True
        self.gameb=True

        self.ballpos = (0,0)
        self.ballhead = 0

        self.towards = "Paddle"
        self.game = "New"

        self.arena_setup=arena.Arena(0,0,-20,-20,self.ballpos,self.ballhead)

        self.d=d
        self.stopup=stopup
        self.stopdown=stopdown

        self.arena_setup.screen.clear()
        self.pong(self.arena_setup.score_manager.score_countA,self.arena_setup.score_manager.score_countB,-20,-20)

    def pong(self,scoreA, scoreB, paddleA, paddleB):

        #<Functions
        def towards_paddle():
            self.angle = self.arena_setup.ball_manager.ball.towards(self.x, self.y)
            self.arena_setup.ball_manager.ball.setheading(self.angle)
            # throwing ball
            while self.gamep:
                self.arena_setup.screen.update()
                time.sleep(self.sleep_time)
                self.arena_setup.ball_manager.ball.forward(5)
                if self.defender == "B":
                    # checking if the ball has hit the paddle
                    if self.arena_setup.ball_manager.ball.xcor() >= 380:
                        if self.arena_setup.paddle_setup.paddle_B_list[0].ycor() - 30 <= self.arena_setup.ball_manager.ball.ycor() <= self.arena_setup.paddle_setup.paddle_B_list[-1].ycor() + 30:
                            self.defender = "A"
                            print("Paddle B")
                            paddle_bounce()
                        else:
                            print("Miss B")
                            while self.arena_setup.ball_manager.ball.xcor() < 480:
                                self.arena_setup.screen.update()
                                time.sleep(self.sleep_time)
                                self.arena_setup.ball_manager.ball.forward(5)
                            self.gamep = False
                            self.gameb = False
                            # score.clear()
                            self.arena_setup.score_manager.score_countA += 1
                            reset(self.arena_setup.score_manager.score_countA, self.arena_setup.score_manager.score_countB)
                            # score.write(f"A              B\n{score_countA}              {score_countB}", False, "center",("Arial", 20))
                else:
                    # checking if the ball has hit the paddle
                    if self.arena_setup.ball_manager.ball.xcor() <= -380:
                        if self.arena_setup.paddle_setup.paddle_A_list[0].ycor() - 30 <= self.arena_setup.ball_manager.ball.ycor() <= self.arena_setup.paddle_setup.paddle_A_list[-1].ycor() + 30:
                            self.defender = "B"
                            print("Paddle A")
                            paddle_bounce()
                        else:
                            print("Miss A")
                            while self.arena_setup.ball_manager.ball.xcor() > -480:
                                self.arena_setup.screen.update()
                                time.sleep(self.sleep_time)
                                self.arena_setup.ball_manager.ball.forward(5)
                            self.gamep = False
                            self.gameb = False
                            # score.clear()
                            self.arena_setup.score_manager.score_countB += 1
                            reset(self.arena_setup.score_manager.score_countA, self.arena_setup.score_manager.score_countB)
                            # score.write(f"A              B\n{score_countA}              {score_countB}", False, "center",("Arial", 20))
        def towards_border():
            self.angle = self.arena_setup.ball_manager.ball.towards(self.x, self.y)
            self.arena_setup.ball_manager.ball.setheading(self.angle)
            while self.gameb:
                self.arena_setup.screen.update()
                time.sleep(self.sleep_time)
                self.arena_setup.ball_manager.ball.forward(5)
                if self.y == 240:
                    # if the ball has hit the border
                    if self.arena_setup.ball_manager.ball.ycor() >= 240:
                        border_bounce()
                else:
                    # if the ball has hit the border
                    if self.arena_setup.ball_manager.ball.ycor() <= -240:
                        border_bounce()

        def paddle_bounce():
            # towards paddle
            if random.choice([0, 1]):
                self.x = self.x * -1
                self.y = random.randint(-220, 220)
                # ->*movep*
                self.towards="Paddle"
                towards_paddle()
            # towards border
            else:
                self.x = random.randint(-340, 340)
                self.y = random.choice([-240, 240])
                # *moveb*
                self.towards="Border"
                towards_border()
        def border_bounce():
            if random.choice([0, 1]):
                if self.defender == "A":
                    self.x = -380
                else:
                    self.x = 380
                self.y = random.randint(-220, 220)
                # ->*movep*
                self.towards="Paddle"
                towards_paddle()
            else:
                if self.defender == "A":
                    self.x = -random.randint(-340, self.x)
                else:
                    self.x = -random.randint(self.x, 340)
                # ->*moveb*
                self.towards="Border"
                towards_border()

        def reset(sA, sB):
            self.game="New"
            self.ballpos=(0,0)
            self.towards="Paddle"
            self.ballhead=0

            if sA != 10 and sB != 10:
                self.arena_setup.screen.clear()
                self.pong(sA, sB, self.arena_setup.paddle_setup.paddle_A_list[0].ycor(), self.arena_setup.paddle_setup.paddle_B_list[0].ycor())
            else:
                if sA == 10:
                    self.arena_setup.endgame("Winner: A", sA, sB)
                else:
                    self.arena_setup.endgame("Winner: B", sA, sB)
        def restart():
            self.arena_setup.screen.clear()
            self.pong(0, 0, -20, -20)
        def pause():
            self.arena_setup.screen.textinput("||",
                             "Escape         -     Pause/Play\nSpace          -     End Game\nx                -     Reset Game\n\n        Paddle A    Paddle B\nUp        w           Up Arrow\nDown   s           Down Arrow")
            self.ballpos = self.arena_setup.ball_manager.ball.pos()  # R1
            self.ballhead=self.arena_setup.ball_manager.ball.heading()
            self.game="Resumed"
            self.arena_setup.screen.clear()
            self.pong(self.arena_setup.score_manager.score_countA,self.arena_setup.score_manager.score_countB,self.arena_setup.paddle_setup.paddle_A_list[0].ycor(),self.arena_setup.paddle_setup.paddle_B_list[0].ycor())
        def stop():
            if self.arena_setup.score_manager.score_countB == self.arena_setup.score_manager.score_countA:
                winner = "Tie"
            elif self.arena_setup.score_manager.score_countB < self.arena_setup.score_manager.score_countA:
                winner = "Winner: A"
            else:
                winner = "Winner: B"
            self.arena_setup.endgame(winner, self.arena_setup.score_manager.score_countA, self.arena_setup.score_manager.score_countB)
            self.arena_setup.screen.exitonclick()

        def w():
            if self.arena_setup.paddle_setup.paddle_A_list[-1].ycor() < self.stopup:
                self.arena_setup.paddle_setup.paddle_A_list[-1].forward(self.d)
                for i in range(2, len(self.arena_setup.paddle_setup.paddle_A_list) + 1):
                    self.arena_setup.paddle_setup.paddle_A_list[len(self.arena_setup.paddle_setup.paddle_A_list) - i].goto(-400,
                                                               self.arena_setup.paddle_setup.paddle_A_list[len(self.arena_setup.paddle_setup.paddle_A_list) - i + 1].ycor() - 20)
        def s():
            if self.arena_setup.paddle_setup.paddle_A_list[0].ycor() > self.stopdown:
                self.arena_setup.paddle_setup.paddle_A_list[0].backward(self.d)
                for i in range(1, len(self.arena_setup.paddle_setup.paddle_A_list)):
                    self.arena_setup.paddle_setup.paddle_A_list[i].goto(-400, self.arena_setup.paddle_setup.paddle_A_list[i - 1].ycor() + 20)
        def up():
            if self.arena_setup.paddle_setup.paddle_B_list[-1].ycor() < self.stopup:
                self.arena_setup.paddle_setup.paddle_B_list[-1].forward(self.d)
                for i in range(2, len(self.arena_setup.paddle_setup.paddle_B_list) + 1):
                    self.arena_setup.paddle_setup.paddle_B_list[len(self.arena_setup.paddle_setup.paddle_B_list) - i].goto(400,
                                                               self.arena_setup.paddle_setup.paddle_B_list[len(self.arena_setup.paddle_setup.paddle_B_list) - i + 1].ycor() - 20)
        def down():
            if self.arena_setup.paddle_setup.paddle_B_list[0].ycor() > self.stopdown:
                self.arena_setup.paddle_setup.paddle_B_list[0].backward(self.d)
                for i in range(1, len(self.arena_setup.paddle_setup.paddle_B_list)):
                    self.arena_setup.paddle_setup.paddle_B_list[i].goto(400, self.arena_setup.paddle_setup.paddle_B_list[i - 1].ycor() + 20)
        #-Functions>#

        #<Arena Setup
        self.arena_setup = arena.Arena(scoreA, scoreB,paddleA,paddleB,self.ballpos,self.ballhead)
        #Arena Setup>#

        #<Game Controls
        self.arena_setup.screen.listen()
        self.arena_setup.screen.onkeypress(restart, "x")
        self.arena_setup.screen.onkeypress(pause, "Escape")
        self.arena_setup.screen.onkeypress(stop, "space")
        self.arena_setup.screen.onkeypress(w, "w")
        self.arena_setup.screen.onkeypress(s, "s")
        self.arena_setup.screen.onkeypress(up, "Up")
        self.arena_setup.screen.onkeypress(down, "Down")
        #Game Controls>#

        #<Game Start
        if self.game=="New":
            # II Game Start (CHANGE)
            self.defender = ""
            self.angle = 0
            self.gamep = True
            self.gameb = True
            self.x = random.choice([-380, 380])
            if self.x == -380:
                self.defender = "A"
            else:
                self.defender = "B"
            self.y = random.randint(-220, 220)
            towards_paddle()
        # Game Start>#
        #<Game Resume
        else:
            if self.towards=="Paddle":
                self.towards="Paddle"
                towards_paddle()
            else:
                self.towards="Border"
                towards_border()
        # Game Resume>#

        #<Game Close
        self.arena_setup.screen.exitonclick()
        #Game Close>#
