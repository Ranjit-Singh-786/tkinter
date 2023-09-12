from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()

root.title('Twiter')
root.iconbitmap('twiter.ico')

def show_box():
    inpt = input_var.get()
    if inpt == "":
        messagebox.showwarning('Warning','please enter something')
    else:
        messagebox.showinfo('you written',inpt)

def func():
    x = var.get()
    lb.config(text=x,bg='green')


def get_check1():
    bt_value = bt1.get()
    lb_for_check.config(text=bt_value)

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

button = Button(root, text='click for entry value', width=25,command=func)
button.pack()
button.place(y='10')


### >>>> combo- box
## from tkinter import ttk

def func2():
    comb_value = comb_var.get()
    lb.config(text=comb_value)


comb_var = StringVar()
comb = ttk.Combobox(root,font='lucida 40 bold',textvariable=comb_var)
comb['state']= 'readonly'
comb['values'] = ('jan','fab','march','april','may','jun')
comb.current(0)
comb.pack()


button = Button(root, text='for comb value', width=25,command=func2)
button.pack()


### >>>>>>>>>>> check button



bt1 = IntVar()
bt2 = IntVar()


btn1 = Checkbutton(root,text="Male",variable=bt1,onvalue=0,offvalue=1)
btn2 = Checkbutton(root,text="Female" , variable=bt2,onvalue=1,offvalue=0)
btn2.pack()
btn1.pack()

lb_for_check = Label(root,text='check values')
lb_for_check.pack()

chek_bton = Button(root,text='get check result',command=get_check1)
chek_bton.pack()


### >>>>>>>>>>> radio button



rdb1 = Radiobutton(root,text="accept",value=0)
rdb2 = Radiobutton(root,text="accept",value=1)

rdb1.pack()
rdb2.pack()



### >>>>> frame

top_frame = Frame(root)
bottom_frame = Frame(root)

top_frame.pack(side=TOP)
bottom_frame.pack(side=BOTTOM)

Label(top_frame,text='Top label in top frame',font='arial 28 bold',background='red').pack()
Label(bottom_frame,text='bottom label in bottom frame',font='arial 28 bold',bg='green').pack()



### >>>>>>>>>>messagebox

# from tkinter import messagebox
# 1.showinfo()
# 2.showwarning()
# 3.showerror()
# 4.askretrycancel()
# 5.askquestion()
# 6.askokcancel()
# 7.askyesno()

input_var = StringVar()
en = Entry(root,textvariable=input_var)
en.pack()

Button(root,text='Click Me for message box',command=show_box).pack()


## >>>>>>>> Listbox
# lst.delete(ANCHOR)  also create a button to delet selected from a list

lstbox = Listbox(root,)
lstbox.pack()
months = ['jan','fab','march','april','may','jun']

for month in months:
    lstbox.insert(END,month,)



root.mainloop()


