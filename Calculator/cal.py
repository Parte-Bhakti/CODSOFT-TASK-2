import tkinter as tk
from tkinter import ttk

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.configure(bg="#E8F6EF")  # Soft mint background

        # Create display
        self.display_var = tk.StringVar()
        self.display = ttk.Entry(root, textvariable=self.display_var,
                                 font=('Arial', 20), justify='right',
                                 state='readonly')
        self.display.pack(pady=20, padx=10, fill=tk.X)

        # Style for buttons
        button_style = {
            'font': ('Arial', 14),
            'width': 5,
            'height': 2,
            'bd': 0,
            'relief': tk.RAISED
        }

        # Button layout and colors
        buttons = [
            ('7', '#AEDFF7'), ('8', '#AEDFF7'), ('9', '#AEDFF7'), ('/', '#F6BD60'),
            ('4', '#FFDAC1'), ('5', '#FFDAC1'), ('6', '#FFDAC1'), ('*', '#F6BD60'),
            ('1', '#CDB4DB'), ('2', '#CDB4DB'), ('3', '#CDB4DB'), ('-', '#F6BD60'),
            ('C', '#FFB4A2'), ('0', '#B5EAD7'), ('=', '#B4F8C8'), ('+', '#F6BD60')
        ]

        button_frame = tk.Frame(root, bg="#E8F6EF")
        button_frame.pack(padx=10, pady=10)

        for i, (text, color) in enumerate(buttons):
            row = i // 4
            col = i % 4
            btn = tk.Button(button_frame, text=text, bg=color,
                            command=lambda t=text: self.on_button_click(t),
                            **button_style)
            btn.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        current = self.display_var.get()

        if char == 'C':
            self.display_var.set('')
        elif char == '=':
            try:
                result = eval(current)
                self.display_var.set(str(result))
            except:
                self.display_var.set('Error')
        else:
            self.display_var.set(current + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
