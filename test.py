from tkinter import *
from tkinter import ttk
root = Tk()

root.minsize(width=600,height=300)
root.maxsize(width=600,height=300)
root.title('first GUI')
root.iconbitmap('twiter.ico')

def func1():
    result = var1.get()
    lb1.config(text=result,background='red')




lb1 = Label(root,text='upflairs',background='green')
lb1.grid(row=40 ,column=20)
lb1.pack()
lb1.place(x=80,y=80)


var1 = StringVar()
ent1 = Entry(root,textvariable=var1)
ent1.pack()

bt1 = Button(root,text='clike me',command=func1)
bt1.pack()

# from tkinter import ttk

var2 = StringVar()
comb = ttk.Combobox(root,font='lucida 20 bold',textvariable=var2)
comb['values'] = ('sunday','monday','tuesday','wednesday','thursday')
comb['state'] = 'readonly'
comb.pack()


bt1 = Checkbutton(root,text='female')
bt2 = Checkbutton(root,text='male')

# grid()
# place()
bt1.pack()
bt2.pack()

rdb = Radiobutton(root,text='accept',value=0)
rdb.pack()



### listbox
lstbox = Listbox(root)
lstbox.pack()
# days = ['sunday','monday','tuesday','wednesday','thursday']
# for day in days:
#     lstbox.insert(END,day)
lstbox.insert(END,'sunday')
lstbox.insert(END,'monday')
lstbox.insert(END,'tuesday')
lstbox.insert(END,'wednesday')
lstbox.insert(END,'thursday')





root.mainloop()