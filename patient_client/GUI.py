from tkinter import *
from computation import find_donor


ws = Tk()
w = Label(ws,
          justify=LEFT,
          compound=LEFT,
          padx=12,
          text="Please enter your Name and Blood Group",
          ).pack(side="top")
ws.title("Plasma finder")
ws.geometry('400x300')
ws['bg'] = '#ffbf01'

def printValue():
    pname = name.get()
    Label(ws, text=f'{pname}, The search has been completed, please check the console for potential donors.', pady=20, bg='#ffbf00').pack()
    # Label(ws, text= y, pady=20, bg='#ffbf00').pack()
name = Entry(ws)
name.pack(pady=40)
blood_group = Entry(ws)
blood_group.pack(pady=40)
x = blood_group.get()
y = find_donor(x)
Button(
    ws,
    text="Find a donor",
    padx=15,
    pady=10,
    command=printValue
).pack()

ws.mainloop()

print(find_donor(x))
