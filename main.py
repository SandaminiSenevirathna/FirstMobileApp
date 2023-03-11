
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
                           command=lambda: self.button_click(text))
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







