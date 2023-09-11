from tkinter import *
from tkinter import ttk
root = Tk()

root.title('Twiter')
root.iconbitmap('twiter.ico')

def func():
    x = var.get()
    lb.config(text=x,bg='green')
    
lb = Label(root,text="Hello, World !",background='black',foreground='white',border='50')
lb.place(x='50',y='120')

var = StringVar()
entr = Entry(root,textvariable=var)
entr.place(x='50',y='80')

#>>> placing the label according to your choice
# lb.grid(row=3,column=2)
# lb.place(x=200,y=300)

# >>>> control the window size

# root.geometry('600x600')
# root.minsize(width=600,height=300)
# root.maxsize(width=600,height=300)

# >>>>>>>>> creating button

button = Button(root, text='click here', width=25,command=func)
button.pack()
button.place(y='10')


### >>>> combo- box
## from tkinter import ttk

def func2():
    comb_value = comb_var.get()
    lb.config(text=comb_value)


comb_var = StringVar()
comb = ttk.Combobox(root,font='lucida 40 bold',textvariable=comb_var)
comb['values'] = ('jan','fab','march','april')
comb.pack()


button = Button(root, text='for comb value', width=25,command=func2)
button.pack()


root.mainloop()


