import tkinter as tk
import tkinter.font as tkFont
import os
import subprocess
import sys
from fun import writeJson, readJson






class error_window:
    def __init__(self, root, reason):
        #setting title
        root.title("error")
        #setting window size
        width=640
        height=360
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        tittle=tk.Label(root)
        ft = tkFont.Font(family='Times',size=25)
        Label_width=500
        Label_height=50
        tittle["font"] = ft
        tittle["fg"] = "#333333"
        tittle["justify"] = "center"
        tittle["text"] = "錯誤"
        tittle.place(x=(width - Label_width) / 2,y=(height - Label_height) / 2 - Label_height * 2, width=Label_width,height=Label_height)

        bottom=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        bottom["font"] = ft
        bottom["fg"] = "#333333"
        bottom["justify"] = "center"
        bottom["text"] = '如果一直發生錯誤請至支援Discord回報'
        bottom.place(x=(width - Label_width) / 2,y=(height - Label_height) / 2 + Label_height*2,width=Label_width,height=Label_height)

        words=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        words["font"] = ft
        words["fg"] = "#333333"
        words["justify"] = "center"
        words["text"] = reason
        words['wraplength'] = 500
        Label_width=500
        Label_height=100
        words.place(x=(width - Label_width) / 2,y=(height - Label_height) / 2 ,width=Label_width,height=Label_height)

        
