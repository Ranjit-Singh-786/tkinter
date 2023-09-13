from tkinter import *
#function
def click_button():
    pass

def clear_entry():
    pass

def calculate():
    pass




root = Tk()
root.title('calculator')




entry = Entry(root, width=16, font=('Arial', 20), borderwidth=2,)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]


row = 1
column = 0

for button in buttons:
    if row != 4:
        bt = Button(root,text=button)
        bt.grid(row=row,column=column)

        column += 1
        if column >3:
            column = 0
            row += 1
    else:
        Button(root,text='c',command=clear_entry).grid(row=row,column=0)
        Button(root,text='0',command=lambda button = '0':click_button(button)).grid(row=row,column=1)
        Button(root,text='=',command=calculate).grid(row=row,column=2)
        Button(root,text='+',command=lambda button = '+':click_button(button)).grid(row=row,column=3)






root.mainloop()