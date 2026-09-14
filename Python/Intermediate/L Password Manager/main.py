import tkinter
from tkinter import messagebox
from password_generator import gen
window=tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=tkinter.Canvas(width=200,height=200)
logo_img=tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_label=tkinter.Label(text="Website: ",pady=20)
website_label.grid(row=1,column=0,sticky='w')
email_label=tkinter.Label(text="Email/         \nUsername: ")
email_label.grid(row=2,column=0,sticky='w')
password_label=tkinter.Label(text="Password: ",pady=20)
password_label.grid(row=3,column=0,sticky='w')


website_input=tkinter.Entry(width=52)
website_input.grid(row=1,column=1,columnspan=2)
email_input=tkinter.Entry(width=52)
email_input.grid(row=2,column=1,columnspan=2)
password_input=tkinter.Entry(width=33)
password_input.grid(row=3,column=1)

def generate():
    password_input.delete(0, tkinter.END)
    password_input.insert(0,gen())

password_button=tkinter.Button(text="Generate Password",command=generate)
password_button.grid(row=3,column=2)

def write_pass():
    question=f"{website_input.get()}\nEmail/Username: {email_input.get()}\nPassword {password_input.get()}\nDo you want to save the password?"
    if len(website_input.get())==0 or len(email_input.get())==0 or len(password_input.get())==0:
       messagebox.showinfo(title="Empty Fields",message="Please fill all three fields before saving.")
    elif messagebox.askokcancel(title="Saving Password",message=question):
        with open ("Passwords.txt","a") as file:
            file.write(f"{website_input.get()}:\n    Email/Username: {email_input.get()}\n    Password: {password_input.get()}\n\n")
        website_input.delete(0, tkinter.END)
        email_input.delete(0, tkinter.END)
        password_input.delete(0, tkinter.END)

add_button=tkinter.Button(text="Add",width=44,command=write_pass)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
