import tkinter as tk
import tkinter.font as tkFont
import json
import os

def readJson(file):	
	file_path = os.path.join(os.path.dirname(__file__), file + '.json')
	with open(file_path, "r", encoding='utf-8') as f:
		data = json.load(f)
	return data

def writeJson(file, item):
	file_path = os.path.join(os.path.dirname(__file__), file + '.json')
	with open(file_path, "w+") as f:
		f.write(json.dumps(item, ensure_ascii=False))

class App:
    def __init__(self, root):
        #setting title
        root.title("輸入token")
        #setting window size
        width=300
        height=150
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_357=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_357["font"] = ft
        GLabel_357["fg"] = "#333333"
        GLabel_357["justify"] = "center"
        GLabel_357["text"] = "label"
        GLabel_357.place(x=110,y=10,width=70,height=25)

        GLineEdit_385=tk.Entry(root)
        GLineEdit_385["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_385["font"] = ft
        GLineEdit_385["fg"] = "#333333"
        GLineEdit_385["justify"] = "center"
        GLineEdit_385["text"] = "Entry"
        GLineEdit_385.place(x=50,y=50,width=200,height=25)

        GButton_467=tk.Button(root)
        GButton_467["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_467["font"] = ft
        GButton_467["fg"] = "#000000"
        GButton_467["justify"] = "center"
        GButton_467["text"] = "Button"
        GButton_467.place(x=110,y=90,width=70,height=25)
        GButton_467["command"] = self.GButton_467_command

    def GButton_467_command(self):
        print("command")

