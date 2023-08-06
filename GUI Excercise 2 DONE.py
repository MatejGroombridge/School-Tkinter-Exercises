from tkinter import *
from tkinter import ttk

tk = Tk()


def add():
    t3.delete(0, 'end')
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1+num2
    t3.insert(END, str(result))


def sub(event):
    t3.delete(0, 'end')
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1-num2
    t3.insert(END, str(result))


label1 = Label(tk, text='First number')
label2 = Label(tk, text='Second number')
label3 = Label(tk, text='Result')

t1 = Entry(bd=3)
t2 = Entry()
t3 = Entry()

button1 = Button(tk, text='Add')
button2 = Button(tk, text='Subtract')
b1 = Button(tk, text='Add', command=add)
b2 = Button(tk, text='Subtract')

label1.place(x=100, y=50)
t1.place(x=200, y=50)
label2.place(x=100, y=100)
t2.place(x=200, y=100)

b1.place(x=100, y=150)
b2.place(x=200, y=150)
label3.place(x=100, y=200)
t3.place(x=200, y=200)


b2.bind('<Button-1>', sub)

tk.title('Hello Python')
tk.geometry("400x300+10+10")
tk.mainloop()
