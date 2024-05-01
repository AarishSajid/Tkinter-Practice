from tkinter import *

def submit () : 
    username = entry_b.get()
    print("welcome", username) 

def clear() : 
    entry_b.delete(0,END)

screen = Tk()

screen.title("ENTRY BOX PRACTICE")
screen.config(background="black")

t_label = Label(screen,
                text="ENTER YOUR NAME",
                font=("times new roman",35),
                bg="black",
                fg="#FF00FF")

entry_b = Entry(screen,
                font=('times new roman',30),
                bg="black",
                fg="#FF00FF"
                )

submit_btn = Button(screen,
                    text="SUBMIT",
                    command=submit,
                    bg="black",
                    fg="#FF00FF")

clear_btn = Button(screen,
                    text="CLEAR",
                    command=clear,
                    bg="black",
                    fg="#FF00FF")


t_label.pack()
entry_b.pack(side=LEFT)
submit_btn.pack(side=RIGHT)
clear_btn.pack(side=RIGHT)

screen = mainloop()
