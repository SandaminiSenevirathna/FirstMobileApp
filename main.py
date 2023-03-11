'''
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




root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
'''


'''
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create the display
        self.display = tk.Entry(master, width=20, justify='right', font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # create the buttons
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)

        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)

        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)

        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('C', 4, 2)
        self.create_button('+', 4, 3)

        self.create_button('=', 5, 0, columnspan=4)

        # set up the clear button
        self.clear_flag = False

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 16),
                           command=lambda:self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

    def button_click(self, text):
        if text == '=':
            # evaluate the expression and display the result
            try:
                result = str(eval(self.display.get()))
            except:
                result = 'ERROR'
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
            self.clear_flag = True
        elif text == 'C':
            # clear the display
            self.display.delete(0, tk.END)
        else:
            # add the button's text to the display
            if self.clear_flag:
                self.display.delete(0, tk.END)
                self.clear_flag = False
            self.display.insert(tk.END, text)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
'''

import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create the display
        self.display = tk.Entry(master, width=20, justify='right', font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)






