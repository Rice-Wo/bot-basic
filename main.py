import tkinter as tk
from tkinter import ttk
from tkinter import * 
import json


def readJson(file):	
	with open(f"{file}.json", "r", encoding='utf-8') as a:
		f = json.load(a)
	return f

def writeJson(file, item):
	with open(f"{file}.json", "w+") as f:
		f.write(json.dumps(item, ensure_ascii=False))

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = button.get()
	return userInput


# this is the function called when the button is clicked
def btnClickFunction():
	if getInputBoxValue():
		tokenJson = readJson('token')
		key = getInputBoxValue()
		tokenJson['TOKEN'] = key
		writeJson('token', tokenJson)
		
	else:
		print('error')



root = Tk()

# This is the section of code which creates the main window
root.geometry('460x310')
root.configure(background='#F0F8FF')
root.title('Tittle')


# This is the section of code which creates a text input box
button=Entry(root)
button.place(x=126, y=26)


# This is the section of code which creates the a label
Label(root, text='輸入TOKEN', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=36, y=26)


# This is the section of code which creates a button
Button(root, text='a', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=286, y=26)
token = readJson('token')

if 'TOKEN' in token:
	if token['TOKEN']:
		print(token['TOKEN'])
else:
	root.mainloop()
