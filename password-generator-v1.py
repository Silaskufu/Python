import random
import tkinter as tk

charList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", ".", "+", "%", "*"]
password = ""
password_length = 0
i = 0
passwordLabel = None
clipboardLabel = None

def on_submit():
    global password_length, passwordLabel

    password_length = int(entry.get())
    gen_password(charList, i, password)
    
def gen_password(charList, i, password):
    global passwordLabel
    global clipboardLabel
    if passwordLabel:
        passwordLabel.destroy()
    if clipboardLabel:
        clipboardLabel.destroy()
    while i < password_length:
        i += 1
        char = random.choice(charList)
        password += char
    
    clipboardLabel = tk.Label(text="Password Copied to Clipboard!")
    clipboardLabel.pack(pady=10)
    passwordLabel = tk.Label(text=password)
    passwordLabel.pack(pady=10)
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update


root = tk.Tk()
root.title("Password Generator")
root.geometry("500x200")
titlefont = ("Arial", 20)
title = tk.Label(text="PASSWORD GENERATOR", font=titlefont)
title.pack()

entry = tk.Entry(root)
entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

root.mainloop()