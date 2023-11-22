import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.create_widgets()

    def create_widgets(self):
        # Entry for password length
        self.length_label = ttk.Label(self.master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.length_entry = ttk.Entry(self.master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Checkboxes for options
        self.special_char_var = tk.BooleanVar()
        self.special_char_checkbox = ttk.Checkbutton(self.master, text="Include Special Characters", variable=self.special_char_var)
        self.special_char_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.numbers_var = tk.BooleanVar()
        self.numbers_checkbox = ttk.Checkbutton(self.master, text="Include Numbers", variable=self.numbers_var)
        self.numbers_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        # Button to generate password
        self.generate_button = ttk.Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Generate and get entry for selected password
        self.result_var = tk.StringVar()
        self.selected_password_label = ttk.Label(self.master, text="Selected Password:")
        self.selected_password_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

        self.selected_password_entry = ttk.Entry(self.master, state='readonly')
        self.selected_password_entry.grid(row=5, column=1, padx=10, pady=10, sticky=tk.W)

        # Button to exit
        self.exit_button = ttk.Button(self.master, text="Exit", command=self.master.destroy)
        self.exit_button.grid(row=6, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
        except ValueError:
            self.result_var.set("Please enter a valid password length.")
            return

        include_special_char = self.special_char_var.get()
        include_numbers = self.numbers_var.get()

        characters = string.ascii_letters
        if include_special_char:
            characters += string.punctuation
        if include_numbers:
            characters += string.digits

        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        self.result_var.set(f"Generated Password: {generated_password}")
        self.selected_password_entry.configure(state='normal')
        self.selected_password_entry.delete(0, tk.END)
        self.selected_password_entry.insert(0, generated_password)
        self.selected_password_entry.configure(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
