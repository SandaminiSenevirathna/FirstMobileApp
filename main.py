import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create entry widget to display input/output
        self.display = tk.Entry(master, width=25, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        # create buttons for numbers
        self.buttons = [
            tk.Button(master, text=str(i), width=5, height=2, command=lambda x=i: self.append_to_display(x))
            for i in range(10)
        ]

        # place number buttons on grid
        for i in range(1, 10):
            row = ((9 - i) // 3) + 1
            col = ((i - 1) % 3)
            self.buttons[i].grid(row=row, column=col)
            self.buttons[0].grid(row=4, column=1)

            





