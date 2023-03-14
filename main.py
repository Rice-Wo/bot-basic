import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = token.get()
	return userInput



root = Tk()

# This is the section of code which creates the main window
root.geometry('460x310')
root.configure(background='#F0F8FF')
root.title('Tittle')


# This is the section of code which creates a text input box
token=Entry(root)
token.place(x=126, y=26)


# This is the section of code which creates the a label
Label(root, text='輸入TOKEN', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=36, y=26)


root.mainloop()
