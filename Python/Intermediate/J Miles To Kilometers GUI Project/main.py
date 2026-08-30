import tkinter
window=tkinter.Tk()
window.title("Project J")#To change the titel of the window
window.minsize(width=700,height=300)#To set the size of the window
label_1=tkinter.Label(text="Home")#To declare a label
label_1.grid(column=0,row=0)#Initializes the label and by defualt centers it on the screen
label2=tkinter.Label(text="Hero",font=("Courier",30,"italic"))
label2.place(x=200,y=200)
label_1.config(padx=20,pady=20)
label_1.config(text="Logo",font=("Courier",20,"bold"))
label2["text"]="Home"
button_1=tkinter.Button(text="Click")
button_1.grid(column=5,row=1)
def click():
    label_1["text"]="Button got clicked"
    if button2["text"]=="Hello":
        button2["text"]="Hi"
    else:
        button2["text"]="Hello"
button2=tkinter.Button(text="Hi",command=click)
button2.grid(column=2,row=1)
def click2():
    label2["text"]=input1.get()
input1=tkinter.Entry()
input1.grid(column=1,row=1)
button_1["command"]=click2
window.mainloop()
