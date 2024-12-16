import random 
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import *


def main():
    global root
    # Creating the GUI
    root = tk.Tk()
        
    # GUI size
    root.geometry("300x350")

    # Not resizable
    root.resizable(width=False, height=False)

    # GUI name
    root.title("Password Generator")

    root.frame = tk.Frame(root)

    # Choice for what characters the user wants to use
    root.low, root.up, root.special, root.num = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()
    root.optionsFrame = tk.LabelFrame(root.frame, text="Options")
    root.lowercase = tk.Checkbutton(root.optionsFrame, text="Lowercase letters", onvalue=1, offvalue=0, variable=root.low)
    root.uppercase = tk.Checkbutton(root.optionsFrame, text="Uppercase letters", onvalue=1, offvalue=0, variable=root.up)
    root.specialChar = tk.Checkbutton(root.optionsFrame, text="Special Characters", onvalue=1, offvalue=0, variable=root.special)
    root.number = tk.Checkbutton(root.optionsFrame, text="Number", onvalue=1, offvalue=0, variable=root.num)

    # Creating the choice of lengths
    root.length = tk.IntVar()
    root.lengthFrame = tk.LabelFrame(root.frame, text="Password Length")
    root.radioButton1 = tk.Radiobutton(root.lengthFrame, text="10", value=10, variable=root.length)
    root.radioButton2 = tk.Radiobutton(root.lengthFrame, text="12", value=12, variable=root.length)
    root.radioButton3 = tk.Radiobutton(root.lengthFrame, text="16", value=16, variable=root.length)
    root.length.set(10)

    # Other buttons and text box
    root.genPassword = tk.Button(root, text="Generate Password", width=25, command=generate_password)
    root.viewHistory = tk.Button(root, text="View History", width=25, command=get_history)
    root.textBox = tk.Text(root, width=25, height=8, relief="solid")

    # Packing the choices
    root.widgetsInFrame = [root.lowercase, root.uppercase, root.specialChar, root.number]
    for item in root.widgetsInFrame:
        item.pack(pady=5, anchor="w")

    root.radioButtons = [root.radioButton1, root.radioButton2, root.radioButton3]
    for radioButton in root.radioButtons:
        radioButton.pack(pady=5, anchor="w")

    root.optionsFrame.grid(row=0, column=0)
    root.lengthFrame.grid(row=0, column=1)

    root.mainWidgets = [root.frame, root.genPassword, root.viewHistory, root.textBox]
    for widget in root.mainWidgets:
        widget.pack(pady=5)

    root.mainloop()


def generate_password():
    # Lowercase option
    if root.low.get() == 1:
        randomLower = random.choices(string.ascii_lowercase, k=16)
    else:
        randomLower = []

    # Uppercase option
    if root.up.get() == 1:
        randomUpper = random.choices(string.ascii_uppercase, k=16)
    else:
        randomUpper = [] 

    # Special characters option
    if root.special.get() == 1:
        randomSpecial = random.choices(string.punctuation, k=16)
    else:
        randomSpecial = []

    # Numbers option
    if root.num.get() == 1:
        randomNumber = random.choices(string.digits, k=16)
    else:
        randomNumber = []

    # Combining the choices together
    randomGen = random.sample(randomLower + randomUpper + randomSpecial + randomNumber, k=int(root.length.get()))
    root.textBox.config(state="normal")
    root.textBox.insert(1.0, f"{''.join(randomGen)}\n")
    root.textBox.config(state="disabled")
    # Open a file called password and "a" means append to add passwords generated to this file
    with open('password', 'a') as file:
        file.write(f"{''.join(randomGen)}\n")

def get_history():
    root.textBox.config(state="normal")
    root.textBox.delete(1.0, "end")
    root.textBox.insert(1.0, open("password", "r").read())
    root.textBox.config(state="disabled")

main()