import tkinter as tk
import tkinter.font as tkFont
import os
import subprocess
import sys
from fun import writeJson, readJson



class App:
    def __init__(self, root):
        self.root = root
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

        tokenLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        tokenLabel["font"] = ft
        tokenLabel["fg"] = "#333333"
        tokenLabel["justify"] = "center"
        tokenLabel["text"] = "label"
        tokenLabel.place(x=110,y=10,width=70,height=25)

        global tokenInput
        tokenInput=tk.Entry(root)
        tokenInput["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        tokenInput["font"] = ft
        tokenInput["fg"] = "#333333"
        tokenInput["justify"] = "center"
        tokenInput["text"] = "Entry"
        tokenInput.place(x=50,y=50,width=200,height=25)

        startButton=tk.Button(root)
        startButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        startButton["font"] = ft
        startButton["fg"] = "#000000"
        startButton["justify"] = "center"
        startButton["text"] = "Button"
        startButton.place(x=110,y=90,width=70,height=25)
        startButton["command"] = self.startButton_command

    def startButton_command(self):
        config = readJson('config')
        config['token'] = tokenInput.get()
        writeJson('config', config)
        if os.path.exists("bot.exe"):
            subprocess.Popen("bot/bot.exe")
        else:
            subprocess.Popen(["python", "bot/bot.py"])
        
        self.root.after(3000, self.root.destroy)
        sys.exit()



class error_window:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=300
        height=150
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        tokenLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        tokenLabel["font"] = ft
        tokenLabel["fg"] = "#333333"
        tokenLabel["justify"] = "center"
        tokenLabel["text"] = "label"
        tokenLabel.place(x=110,y=10,width=70,height=25)

        GLabel_249=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_249["font"] = ft
        GLabel_249["fg"] = "#333333"
        GLabel_249["justify"] = "center"
        GLabel_249["text"] = "label"
        GLabel_249.place(x=110,y=60,width=70,height=25)
