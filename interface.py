from tkinter import font
import customtkinter as ctk
import tkinter as tk
import generator as gen
import pyperclip as pc




ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("1200x800")

ipadding = {'ipadx': 12, 'ipady': 10}
isize = {'width': 200, 'height': 40}


W_WIDTH = 200
W_HEIGHT = 40
RED_MAIN = "#CE2029"
RED_HOVER = "#560319"

def displayResult():
    plaintext = gen.extend(entry1.get())
    result = gen.encrypt(plaintext,"", siteselect.get())
    encryptedbox.delete(0, 'end')
    encryptedbox.insert(0,result)

def copy():
    pc.copy(encryptedbox.get())
    spam = pc.paste()
    print("copied")

result = "Encrypted Password"
frame = ctk.CTkFrame(master = root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master = frame, text = "Password Generator")
label.grid(row = 2, column = 1, pady = 12, padx = 10)


entry1 = ctk.CTkEntry(master = frame, placeholder_text = "Password", width=W_WIDTH, height=W_HEIGHT)
entry1.grid(row = 2, column = 2, pady = 12, padx = 10)

siteselect = ctk.CTkComboBox(master = frame,values=["Value 1", "Value 2", "Value Long....."], width=W_WIDTH, height=W_HEIGHT)
siteselect.set("Enter a website")
siteselect.grid(row = 3, column = 2, pady = 12, padx = 10)

button = ctk.CTkButton(master = frame, text = "Generate Password", command = displayResult, fg_color = RED_MAIN, hover_color = RED_HOVER, width=W_WIDTH, height=W_HEIGHT)
button.grid(row = 4, column = 1, pady = 20, padx = 10)

encryptedbox = ctk.CTkEntry(master = frame, placeholder_text = "Encrypted Password", **isize)
encryptedbox.grid(row = 5, column = 1, pady = 12, padx = 10)

button = ctk.CTkButton(master = frame, text = "Copy to clipboard", command = copy, fg_color = RED_MAIN, hover_color = RED_HOVER, **isize)
button.grid(row = 5, column = 2, pady = 20, padx = 10)


root.mainloop()