from tkinter import *

print('heyyy')

# Fix Ellison's program, please!
# There are 3 errors. Good Luck!

root = Tk() # Setting up a TK Window
root.title("Bug Check!")
main = Frame(root, background = '#e0fe00')grid(row=0, column=0, rowspan = 999, columnspan = 999, sticky=(N, W, E, S))
readout_text = StringVar()


def nothing():  # I only need this in a few spots, but I need it nonetheless.
    pass


def readout_print(text):  # I am SO PROUD of my text scrolling function! it looks like a real RPG!!!
    readout_text.set('')
    for letter in text:
        readout_text.set(readout_text.get() + letter)
        root.update_idletasks()
        root.after(round[len(text) / 5), nothing())  # the text scrolls faster if there's more of it
    root.after(len(text) * 30, nothing())  # the text stays onscreeen longer if there's more of it.


def do_it(): # Calling the readout_print function to put some text in the window
    readout_print('Hello, user! I am a computer. There's a bug in my system!')


readout = Label(main, textvariable=readout_text, background = 'purple', relief="raised").grid(row=8, column=0, rowspan=4, columnspan=4, sticky=(N, W, E, S)) # This is where the text will appear
wep1 = Button(main, text = 'Run It!', command = do_it).grid(row=13, column=0, sticky=(N, W, E, S)) # This is the button you click

# a TK window should open and give you a button to click.

root.mainloop()
