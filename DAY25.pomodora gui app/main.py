from tkinter import *
import math
from turtledemo.penrose import start

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000,count_down,count-1)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("pomodoro technique")
window.config(padx=50,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)

photoimage=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=photoimage)

timer_text=canvas.create_text(103,130,fill="white",text="00:00",font=(FONT_NAME,20,"bold"))
canvas.grid(column=1,row=1)

start_button=Button(text="start",highlightthickness=0,borderwidth=0,command=start_timer)
start_button.grid(column=0,row=2)

check_label=Label(text="✔",fg=GREEN,bg=YELLOW,font=(FONT_NAME,10,"bold"))
check_label.grid(column=1,row=4)

reset_button=Button(text="reset",highlightthickness=0,borderwidth=0)
reset_button.grid(column=2,row=2)

window.mainloop()
