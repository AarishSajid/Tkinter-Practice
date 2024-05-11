from tkinter import *

def subm() :
    print("your sus level is",s_meter.get()) 



screen = Tk()
screen.title("SUS METER")
screen.config(bg="Black")

head = Label(screen,
             text="SUS METER",
             font=("consolas,20"),
             bg="Black",
             fg="#FF00FF")

s_meter = Scale(screen,
                from_=1,
                to=10,
                length=500,
                font=("consolas",20),
                orient=HORIZONTAL,
                troughcolor="#FF00FF",
                bg="Black",
                fg="white")

s_button = Button(screen,text="sure?",
                  command=subm,
                  font=("consolas",13),
                  bg="black",
                  fg="#FF00FF")

head.pack()
s_meter.pack()
s_button.pack()

                



screen = mainloop()