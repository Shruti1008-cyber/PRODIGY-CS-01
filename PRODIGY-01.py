import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift, encrypt=True):
    if not encrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def encrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        result = caesar_cipher(text, shift, encrypt=True)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    except ValueError:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a valid integer for the shift.")

def decrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        result = caesar_cipher(text, shift, encrypt=False)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    except ValueError:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a valid integer for the shift.")

# Create the main application window
root = tk.Tk()
root.title("Caesar Cipher")

# Input Label and Text
ttk.Label(root, text="Input Text:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
input_text = tk.Text(root, height=5, width=50)
input_text.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# Shift Label and Entry
ttk.Label(root, text="Shift:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
shift_entry = ttk.Entry(root)
shift_entry.grid(row=2, column=1, pady=5, sticky="w")

# Buttons
encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=2, column=2, padx=5, pady=5, sticky="w")

decrypt_button = ttk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=2, column=3, padx=5, pady=5, sticky="w")

# Output Label and Text
ttk.Label(root, text="Output Text:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
output_text = tk.Text(root, height=5, width=50)
output_text.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
