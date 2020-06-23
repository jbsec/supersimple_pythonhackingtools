# Generate a secure password.
# Please run pip install pyperclip.
from tkinter import *
import pyperclip
import random
root = Tk()
root.geometry("400x400")
passstr = StringVar()
passlen = IntVar()
passlen.set(0)

def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B',
            'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W',
            'X', 'Y', 'Z', '1', '2', '3', '4',
            '5', '6', '7', '8', '9', '0', ' ',
            '!', '@', '#', '$', '^', '&', '*',
            '%', '(',')' ] #include any extras here
            #including unicode characters assuming
            #you can import what you need for it.
            #and other languages.

    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passstr.set(password)

def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

Label(root, text="Secure Password Generator",
      font="calibri 20 bold").pack()
Label(root, text="Enter Password Length").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Generate Password",
       command=generate).pack(pady=7)
Entry(root, textvariable=passstr).pack(pady=3)
Button(root, text="Copy To Clipboard",
       command=copytoclipboard).pack()

root.mainloop()
        