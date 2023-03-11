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

            # create buttons for operations
            self.operations = [
                tk.Button(master, text='+', width=5, height=2, command=lambda: self.append_to_display('+')),
                tk.Button(master, text='-', width=5, height=2, command=lambda: self.append_to_display('-')),
                tk.Button(master, text='*', width=5, height=2, command=lambda: self.append_to_display('*')),
                tk.Button(master, text='/', width=5, height=2, command=lambda: self.append_to_display('/')),
                tk.Button(master, text='C', width=5, height=2, command=lambda: self.clear_display()),
                tk.Button(master, text='=', width=5, height=2, command=lambda: self.calculate())
            ]

            # place operation buttons on grid
            for i, button in enumerate(self.operations):
                button.grid(row=i + 1, column=3)

        def append_to_display(self, value):
            self.display.insert(tk.END, value)

        def clear_display(self):
            self.display.delete(0, tk.END)

        def calculate(self):
            expression = self.display.get()
            try:
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")







