from tkinter import * 

count = 0

def press():
    global count 
    count = count + 1
    print("you pressed", count, "times")


# create a main screen

m_screen = Tk()

btn = Button(m_screen,
             text= "press me",
             command=press)


btn.pack()



m_screen = mainloop()