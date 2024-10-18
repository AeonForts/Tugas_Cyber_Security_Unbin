import tkinter as tk
from tkinter import filedialog, messagebox, Menu

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def save_file():
    text = text_area.get("1.0", tk.END)
    shift = int(shift_entry.get())
    # Check if the user wants to encrypt or decrypt
    if encrypt_mode.get():
        processed_text = encrypt(text, shift)
    else:
        processed_text = decrypt(text, shift)
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(processed_text)
        messagebox.showinfo("Success", "File saved successfully!")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete("1.0", tk.END)  # Clear current text
            text_area.insert(tk.END, file.read())  # Insert file content

def new_file():
    text_area.delete("1.0", tk.END)  # Clear current text

app = tk.Tk()
app.title("Text File Encryptor")

# Menu Bar
menu_bar = Menu(app)
app.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Shift Entry
shift_label = tk.Label(app, text="Enter Shift Value:")
shift_label.pack()

shift_entry = tk.Entry(app)
shift_entry.pack()

# Add a variable to track mode
encrypt_mode = tk.BooleanVar(value=True)  # Default to encrypt mode

# Add radio buttons for mode selection
encrypt_radio = tk.Radiobutton(app, text="Encrypt", variable=encrypt_mode, value=True)
encrypt_radio.pack()

decrypt_radio = tk.Radiobutton(app, text="Decrypt", variable=encrypt_mode, value=False)
decrypt_radio.pack()

# Text Area
text_area = tk.Text(app, height=20, width=60)
text_area.pack()

app.mainloop()
