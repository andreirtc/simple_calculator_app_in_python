# 1. Import tkinter for the simple chatbox GUI

import tkinter as tk
from tkinter import messagebox

# 2. Create a class for the simple calculator
# 3. Build the chatbox GUI (height and width, chat frame, enter button, and bind the enter or return key)

class simple_calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calci")
        self.geometry("400x400")

        self.title_label = tk.Label(self, text="CALCI", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        self.chat_frame = tk.Frame(self)
        self.chat_frame.pack(pady=10)

        self.chat_text = tk.Text(self.chat_frame, height=10, width=50)
        self.chat_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.chat_frame, command=self.chat_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_text.config(yscrollcommand=self.scrollbar.set)

        self.input_entry = tk.Entry(self, width=20)
        self.input_entry.pack()

        self.enter_button = tk.Button(self, text="Enter", command=self.send_message)
        self.enter_button.pack()

        self.history = []

        self.initialize_chat()

        self.input_entry.bind("<Return>", self.send_message_enter)

# 4. Define a function to initialize chat

    def initialize_chat(self):
        self.add_message("C: Hi! I'm Calci a simple calculator programmed using Python.")
        self.add_message("C: What operation do you need?")
        self.add_message("(1) Addition")
        self.add_message("(2) Subtraction")
        self.add_message("(3) Multiplication")
        self.add_message("(4) Division")
        
# 5. Define functions to add and send message. Under function send message, use if-else and exception handling in case of wrong input or zero division error.
# 6. Define a function to calculate and output results