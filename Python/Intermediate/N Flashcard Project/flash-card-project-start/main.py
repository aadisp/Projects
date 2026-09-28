#Setup
BACKGROUND_COLOR = "#B1DDC6"
import pandas
import tkinter
window=tkinter.Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flash Card")
canvas=tkinter.Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
bg_img=tkinter.PhotoImage(file="images/card_back.png")
canvas.create_image(400,263,image=bg_img)
fg_img=tkinter.PhotoImage(file="images/card_front.png")
canvas_img=canvas.create_image(400,263,image=fg_img)
lang=canvas.create_text(400,150,text="French",font=("Arial",40,"italic"))
word=canvas.create_text(400,263,text="trouve",font=("Arial",60,"bold"))
timer=canvas.create_text(700,50,text=3,font=("Arial",30))
canvas.grid(row=0,column=0,columnspan=2)
wrong_img=tkinter.PhotoImage(file="images/wrong.png")
wrong_bt=tkinter.Button(image=wrong_img,borderwidth=0,bg=BACKGROUND_COLOR)
wrong_bt.grid(row=1,column=0)
right_img=tkinter.PhotoImage(file="images/right.png")
right_bt=tkinter.Button(image=right_img,borderwidth=0,bg=BACKGROUND_COLOR)
right_bt.grid(row=1,column=1)
i=0
pause=False
#If Check Mark
def correct():
    global i,data_dict
    print(data_dict[i])
    data_dict.remove(data_dict[i])
    data2=pandas.DataFrame(data_dict)
    data2.to_csv("data/words_to_learn.csv")
    #Remove Card
    french_words.pop(i)
    english_words.pop(i)
    french()
#If Cross Mark
def wrong():
    global i
    i+=1
    french()
right_bt.config(command=correct)
wrong_bt.config(command=wrong)

#Convert CSV into Dictionary
data=pandas.read_csv("data/french_words.csv")
data_dict=data.to_dict(orient="records")
#Convert Dictionary into List
french_words=data["French"].to_list()
english_words=data["English"].to_list()

def counter(t):
    if t>0:
        canvas.itemconfig(timer, text=t, fill="#D21F3C")
        t-=1
        window.after(1000, counter, t)
    else:
        english()

# Display card in English
def english():
    global i
    canvas.itemconfig(word, text=data_dict[i]["English"], fill="#ffffff")
    canvas.itemconfig(lang, text="English", fill="#ffffff")
    canvas.itemconfig(canvas_img, image=bg_img)
    canvas.itemconfig(timer, text="", fill="#000000")

#If list is not empty
def french():
    global pause, i
    if not len(data_dict) == 0:
        # Display card in French
        try:
            canvas.itemconfig(word, text=data_dict[i]["French"],fill="#000000")
            canvas.itemconfig(lang, text="French",fill="#000000")
            canvas.itemconfig(canvas_img, image=fg_img)
        # Rerun the wrongly guessed words
        except IndexError:
            i=0
            french()
        else:
            #Wait for 3 seconds
            window.after(000,counter,3)
    else:
        # If dictionary is empty
        canvas.itemconfig(word, text="Fine`", fill="#000000")
        canvas.itemconfig(lang, text="", fill="#000000")
        canvas.itemconfig(canvas_img, image=fg_img)

french()

window.mainloop()
