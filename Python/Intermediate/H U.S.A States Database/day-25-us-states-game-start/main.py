import turtle
import pandas
screen=turtle.Screen()
image="blank_states_img.gif"
bg=turtle.Turtle()
screen.addshape(image)
bg.shape(image)
states=pandas.read_csv("50_states.csv")
dict_view=states.to_dict()
print(dict_view)
guess_list=[]
score=0
def correct(g):
    state_name = turtle.Turtle()
    state_name.hideturtle()
    state_name.penup()
    xcor = states[states.state == guess].x.item()
    ycor = states[states.state == guess].y.item()
    state_name.goto(xcor, ycor)
    state_name.write(g, align="center")
    global score
    score+=1
def check(guess):
    if guess in states.state.to_list() and guess not in guess_list:
        guess_list.append(guess)
        correct(guess)
while len(guess_list)!=len(states.state):
    guess = screen.textinput(f"             U.S {score}/{len(states)}", "Guess a state").title()
    if guess=="Exit":
        break
    check(guess)

missed_states={
    "Missed":[],
    "Guessed":[],
    "States":[],
    "Guess":[]
}
for st in states.state:
    missed_states["States"].append(st)
    if st not in guess_list:
        missed_states["Missed"].append(st)
        missed_states["Guessed"].append("")
        missed_states["Guess"].append("Missed")
    else:
        missed_states["Guessed"].append(st)
        missed_states["Missed"].append("")
        missed_states["Guess"].append("Correct")
missed=pandas.DataFrame(missed_states)
missed.to_csv("Your Performance.csv")