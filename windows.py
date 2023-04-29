import tkinter as tk
import tkinter.font as tkFont
import os
import subprocess
import sys
from fun import writeJson, readJson






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
