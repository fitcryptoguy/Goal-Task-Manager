from tkinter import *
import pandas
from tkinter import messagebox


TRUE1 = "#EEE3CB"
TRUE2 = "#D7C0AE"
TRUE3 = "#967E76"
FONT_NAME = "Courier"
########################################################  Add Button Functionality #############################################################


def add():

    if len(day_select.get()) == 0 or len(goal_select.get()) == 0 or len(enter_amount.get()) == 0:
        messagebox.showerror(title="Not enough length", message="Please dont leave any field empty")
    else:
        df = pandas.read_csv("week_goals.csv", header=1)
        df[goal_select.get()][day_options[day_select.get()]] = enter_amount.get()          # equivalent to df[column][index] = amount


    day_select.set("")
    goal_select.set("")
    enter_amount.delete(0,2)
    day_label.focus()

















############################################################### UI ###########################################################################
window = Tk()
window.config(pady=70, padx=50, bg=TRUE1)
window.title("Dail tasks")
window.minsize(width=700, height=500)


#Label
title_label = Label(text="weekly goals", font = (FONT_NAME, 45, "bold"), bg=TRUE1, fg="white")
title_label.grid(column=2, row=2, padx=20, pady=20)

select_goal_label = Label(text="Select Goal", width=15, height=2)
select_goal_label.grid(column=1, row=3)

amount_label = Label(text="Amount", width=15, height=2)
amount_label.grid(column=1, row=4)

day_label = Label(text="Day", width=15, height=1, bg=TRUE1, font = (FONT_NAME, 15, "bold"))
day_label.grid(column=1, row=0)

#Drop-Down Menu
goal_select = StringVar()
options = ["Gym", "Meditation", "Python", "Earning", "Crypto", "DA"]
drop = OptionMenu(window, goal_select, *options )
drop["width"] = 18
drop["direction"] = ["above", "below", "flush", "left", "right"][1]
drop["background" ] = TRUE2
drop["activebackground" ] = TRUE3
drop["highlightbackground"] = TRUE2
drop["font"] = 'TkDefaultFont 14'
drop["menu"]["background"] = TRUE2
drop["menu"]["foreground"] = TRUE3
drop["menu"]["font"] = "TkDefaultFont 15"
drop["menu"]["selectcolor"] = TRUE3
drop["menu"]["activeborderwidth"] = '4'
drop.grid(row=3, column=2, pady=20)

day_select = StringVar()

day_options = {"Monday":0, "Tuesday":1, "Wednesday":2,"Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}
day_drop = OptionMenu(window, day_select, *day_options.keys())
day_drop["width"] = 8
day_drop.grid(column=1, row=1)





#eNTRIES
enter_amount = Entry(width=20)
enter_amount.grid(row=4, column=2, pady=20)

#Button
add_button = Button(text="Add", width=10, command=add)
add_button.grid(row=5, column=2)















window.mainloop()