import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create entry widget to display input/output
        self.display = tk.Entry(master, width=25, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, pady=10)


