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

    def add_message(self, message):
        self.chat_text.insert(tk.END, message + "\n")
        self.chat_text.see(tk.END)

    def send_message(self, event=None):
        user_input = self.input_entry.get()
        self.history.append(user_input)

        if len(self.history) == 1:  # Choose operation
            try:
                choice = int(user_input)
                if choice not in range(1, 5):
                    raise ValueError("Invalid choice")
                self.operation = choice
                self.add_message(f"U: {user_input}")
                self.add_message("C: Enter your first number:")
                self.input_entry.delete(0, tk.END)
            except ValueError:
                self.add_message("C: Invalid choice. Please enter a number from 1 to 4.")
        elif len(self.history) == 2:  # First number
            try:
                self.num1 = float(user_input)
                self.add_message(f"U: {user_input}")
                self.add_message("C: Enter your second number:")
                self.input_entry.delete(0, tk.END)
            except ValueError:
                self.add_message("C: Invalid input. Please enter a valid number.")
        elif len(self.history) == 3:  # Second number
            try:
                self.num2 = float(user_input)
                self.add_message(f"U: {user_input}")
                self.calculate_result()
                self.input_entry.delete(0, tk.END)  # Clear input after calculation
            except ValueError:
                self.add_message("C: Invalid input. Please enter a valid number.")
        elif len(self.history) == 4:  # Try again prompt
            if user_input.lower() == 'y':
                self.history = []  # Reset chat history
                self.initialize_chat()  # Restart the conversation
                self.input_entry.delete(0, tk.END)
            elif user_input.lower() == 'n':
                self.add_message(f"U: {user_input}")
                self.add_message("C: Thank you for using Calci!")
                self.input_entry.config(state=tk.DISABLED)
            else:
                self.add_message("C: Invalid input. Please enter 'y' or 'n'.")
                self.add_message("C: Do you want to try again? (y/n)")
            self.input_entry.delete(0, tk.END)

    def send_message_enter(self, event):
        self.send_message()

# 6. Define a function to calculate and output results

    def calculate_result(self):
        result = None
        if self.operation == 1:
            result = self.num1 + self.num2
        elif self.operation == 2:
            result = self.num1 - self.num2
        elif self.operation == 3:
            result = self.num1 * self.num2
        elif self.operation == 4:
            try: 
                result = self.num1 / self.num2
            except ZeroDivisionError: 
                self.num2 == 0
                self.add_message("C: Division by zero is not allowed.") 

        self.add_message(f"C: The result is {result}!")
        self.add_message("C: Do you want to try again? (y/n)")
        
if __name__ == "__main__":
    app = simple_calculator()
    app.mainloop()
    