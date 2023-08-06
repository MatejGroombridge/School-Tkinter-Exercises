from tkinter import *
from tkinter import ttk


def main():
    tk = Tk()
    data = ("one", "two", "three", "four")

    # Radio Buttons
    v0 = IntVar()
    v0.set(1)
    Radiobutton(tk, text="male", variable=v0, value=1).place(x=100, y=50)
    Radiobutton(tk, text="female", variable=v0, value=2).place(x=180, y=50)

    # Check Buttons
    v1 = IntVar()
    v2 = IntVar()
    Checkbutton(tk, text="Cricket", variable=v1).place(x=100, y=100)
    Checkbutton(tk, text="Tennis", variable=v2).place(x=180, y=100)

    # Combobox
    var = StringVar()
    var.set("one")
    cb = ttk.Combobox(tk, values=data)
    cb.place(x=60, y=150)

    # Listbox
    lb = Listbox(tk, height=5, selectmode='multiple')
    for num in data:
        lb.insert(END, num)
    lb.place(x=250, y=150)

    tk.title('Hello Python!')
    tk.geometry("400x300+10+10")

    tk.mainloop()


if __name__ == "__main__":
    main()
