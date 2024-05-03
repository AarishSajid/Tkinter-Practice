from tkinter import *

khana = ["pizza","burger","chai"]

screen = Tk()
screen.title("Radio Buttons")
screen.config(bg="Black")

def order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered a burger!")
    elif(x.get()==2):
        print("You ordered a chai!")
    else:
        print("huh?")
        
x = IntVar()

for food in range(len(khana)):
    r_button = Radiobutton(screen,
                           text=khana[food],
                           variable=x,
                           value=food,
                           padx=30,
                           pady=10,
                           font=("Poppins",35),
                           command=order)
    r_button.pack(anchor=W)

screen = mainloop()
