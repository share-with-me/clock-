# use Tkinter to show a digital clock
# tested with Python24    vegaseat    10sep2006
from tkinter import *
import time
root = Tk()
root.title("My_Clock")
root.minsize(width= 300,height = 300)
root.maxsize(width = 400, height = 400)

clock = Label(root, font=('times', 20, 'bold'), bg='white')
clock.pack(fill = BOTH,expand=1)
def tick():
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)
tick()
root.mainloop()