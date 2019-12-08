from tkinter import  filedialog
from tkinter import *
a= Tk()
def mfileopen():
    file1=filedialog.askopenfile()
    label=Label(text=file1).pack()

button=Button(text="open file",width=30,command=mfileopen).pack()

a.mainloop()
