import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=1
timer=None
import math
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer,rep
    check["text"] += ""
    pomodoro.config(text="Timer",fg=RED)
    canvas.itemconfig(time_text, text="00:00")
    window.after_cancel(timer)
    rep=1
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    if rep<8:
        if rep%2 == 0:
            count_down(SHORT_BREAK_MIN*60-1)
            check["text"] += "✔"
            pomodoro.config(text="Break",fg=PINK)
        else:
            count_down(WORK_MIN*60-1)
            pomodoro.config(text="Work",fg=GREEN)
        rep += 1
    else:
        count_down(LONG_BREAK_MIN*60-1)
        rep=1
        check["text"] = ""
        pomodoro.config(text="Break",fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    global timer
    if math.floor(seconds / 60) < 10:
        minute=f"0{math.floor(seconds / 60)}"
    else:minute=f"{math.floor(seconds / 60)}"
    if seconds % 60 < 10:
        second=f"0{seconds % 60}"
    else:second=f"{seconds % 60}"
    if seconds>=0:
        canvas.itemconfig(time_text,text=f"{minute}:{second}")
        timer=window.after(1000,count_down,seconds-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=50,pady=50,bg=YELLOW)

canvas=tkinter.Canvas(width=210,height=224)
canvas.config(bg=YELLOW,highlightthickness=0)

tomato=tkinter.PhotoImage(file="tomato.png")
canvas.create_image(105,112,image=tomato)
time_text=canvas.create_text(105,130,text=f"00:00",fill="white",font=(FONT_NAME,20,"bold"))
canvas.grid(column=1,row=1)

pomodoro=tkinter.Label(text="Timer",bg=YELLOW,fg=RED,font=(FONT_NAME,50))
pomodoro.grid(row=0,column=1)

start=tkinter.Button(text="Start",borderwidth=0,command=start_timer)
start.grid(column=0,row=2)

reset=tkinter.Button(text="Reset",borderwidth=0,command=reset_timer)
reset.grid(column=2,row=2)

check=tkinter.Label(text="",bg=YELLOW,fg=GREEN,font=(FONT_NAME,10))
check.grid(column=1,row=3)

window.mainloop()
