import json
import tkinter
from tkinter import messagebox
from password_generator import gen
import pyperclip
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


website_input=tkinter.Entry(width=33)
website_input.grid(row=1,column=1)
website_input.focus()
email_input=tkinter.Entry(width=52)
email_input.grid(row=2,column=1,columnspan=2)
password_input=tkinter.Entry(width=33)
password_input.grid(row=3,column=1)

def generate():
    password_input.delete(0, tkinter.END)
    password_input.insert(0,gen())
def search():
    try:
        with open ("Password.json","r") as file:
            pass_dict=json.load(file)
    except:
        messagebox.showinfo(title="Missing", message="Password for this website has not been saved.")
    else:
        if website_input.get() in pass_dict:
            email_input.delete(0, tkinter.END)
            password_input.delete(0, tkinter.END)
            email_input.insert(0,pass_dict[website_input.get()]["Email"])
            password_input.insert(0,pass_dict[website_input.get()]["Password"])
            messagebox.showinfo(title=website_input.get(),message=f"Email: {pass_dict[website_input.get()]["Email"]}\nPassword: {pass_dict[website_input.get()]["Password"]}\nPassword has been copied to your clipboard.")
            pyperclip.copy(pass_dict[website_input.get()]["Password"])
        else:
            messagebox.showinfo(title="Missing",message="Password for this website has not been saved.")

website_button=tkinter.Button(text="Search",padx=34,command=search)
website_button.grid(row=1,column=2,sticky='w')
password_button=tkinter.Button(text="Generate Password",command=generate)
password_button.grid(row=3,column=2)

def write_pass():
    pass_dict={website_input.get():{"Email":email_input.get(),"Password":password_input.get(),}}
    question=f"{website_input.get()}\nEmail/Username: {email_input.get()}\nPassword {password_input.get()}\nDo you want to save the password?"
    if len(website_input.get())==0 or len(email_input.get())==0 or len(password_input.get())==0:
       messagebox.showinfo(title="Empty Fields",message="Please fill all three fields before saving.")
    elif messagebox.askokcancel(title="Saving Password",message=question):
        try:
            with open ("Password.json","r") as file:
                pass_file=json.load(file)
        except:
            with open("Password.json","w") as file:
                json.dump(pass_dict,file,indent=4)
        else:
            pass_file.update(pass_dict, indent=4)
            with open("Password.json", "w") as file:
                json.dump(pass_file, file, indent=4)
        finally:
            website_input.delete(0, tkinter.END)
            email_input.delete(0, tkinter.END)
            password_input.delete(0, tkinter.END)

add_button=tkinter.Button(text="Add",width=44,command=write_pass)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
