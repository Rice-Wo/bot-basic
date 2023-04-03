import tkinter as tk
from tkinter import ttk
from tkinter import * 
import json
import os

#定義json檔讀寫函式
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
		tokenJson = readJson('config')
		key = getInputBoxValue()
		tokenJson['token'] = key
		writeJson('config', tokenJson)
		
	else:
		print('error')

tokenInput = Tk()

# This is the section of code which creates the main window
tokenInput.geometry('460x310')
tokenInput.title('Tittle')

# This is the section of code which creates a text input box
button=Entry(tokenInput)
button.place(x=126, y=26)

# This is the section of code which creates the a label
Label(tokenInput, text='輸入TOKEN', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=36, y=26)

# This is the section of code which creates a button
Button(tokenInput, text='a', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=286, y=26)



if os.path.exists("config.json"):    
	pass
else:
    # 創建一個新的設定檔
    config = {
        'token': "",
        'setting2': 'value2',
        'setting3': 'value3'
    }
    with open("config.json", 'w') as f:
        json.dump(config, f)


config = readJson('config')
if config['token']:
	print(config['config'])
else:
	tokenInput.mainloop()