import turtle
import logic as game

screen = turtle.Screen()
screen.setup(1000, 600)
screen.bgcolor("black")

difficulty=screen.textinput("Choose difficulty:","Easy (E)\nMedium (M)\nHard(H)")
if difficulty=="E":
    screen.title("Pong - Easy Mode")
    sleep_time=0.01
    d=20
    stopup=240
    stopdown=-240
elif difficulty=="M":
    screen.title("Pong - Normal Mode")
    sleep_time=0.006
    d=40
    stopup=240
    stopdown=-220
else:
    screen.title("Pong - Hard Mode")
    sleep_time=0.003
    d=60
    stopup=220
    stopdown=-200

#call from class
pong=game.Pong(sleep_time,d,stopup,stopdown)
