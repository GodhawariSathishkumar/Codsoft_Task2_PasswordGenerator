import tkinter as tk
import random
import string

def generate_password():
    password = ""

    if var.get() == "Weak":
        password = ''.join(random.choices(string.ascii_lowercase, k=6))
    elif var.get() == "Strong":
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    elif var.get() == "Very Strong":
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=15))

    password_var.set(password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")

frame = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
frame.pack(fill=tk.BOTH, expand=True)

var = tk.StringVar(root, "Weak")

weak_radio = tk.Radiobutton(frame, text="Weak", variable=var, value="Weak", bg="#f0f0f0")
weak_radio.grid(row=0, column=0, sticky="w", pady=(0, 5))

strong_radio = tk.Radiobutton(frame, text="Strong", variable=var, value="Strong", bg="#f0f0f0")
strong_radio.grid(row=1, column=0, sticky="w", pady=5)

very_strong_radio = tk.Radiobutton(frame, text="Very Strong", variable=var, value="Very Strong", bg="#f0f0f0")
very_strong_radio.grid(row=2, column=0, sticky="w", pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white")
generate_button.pack(pady=10)

password_var = tk.StringVar(root, "")
password_label = tk.Label(root, textvariable=password_var, font=("Arial", 12), padx=10, pady=5, borderwidth=2, relief="solid", bg="#f0f0f0")
password_label.pack(fill=tk.X, padx=10)

root.mainloop()
