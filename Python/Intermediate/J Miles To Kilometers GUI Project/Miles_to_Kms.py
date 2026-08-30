import tkinter
window=tkinter.Tk()
window.minsize(width=300,height=200)
window.title("Miles to Km Converter")
window.config(padx=40,pady=40)

miles_input=tkinter.Entry()
miles_input.grid(column=1,row=0)

miles_label=tkinter.Label(text="miles",padx=15,pady=15)
miles_label.grid(column=2,row=0)

equals_label=tkinter.Label(text="is equal to",padx=15,pady=15)
equals_label.grid(column=0,row=1)

result_label=tkinter.Label(text=0,padx=20,pady=20)
result_label.grid(column=1,row=1)

km_label=tkinter.Label(text="Km")
km_label.grid(column=2,row=1)

def convert():
    result_label["text"]=float(miles_input.get())*1.609

calc=tkinter.Button(text="Calculate",command=convert)
calc.grid(column=1,row=2)

window.mainloop()
