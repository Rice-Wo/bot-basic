import tkinter as tk
import json
import os
import logging
from tklog import winlogHandler

# 定義json檔讀寫函式
def readJson(file):    
    with open(f"{file}.json", "r", encoding='utf-8') as a:
        f = json.load(a)
    return f

def writeJson(file, item):
    with open(f"{file}.json", "w+") as f:
        f.write(json.dumps(item, ensure_ascii=False))


# this is a function to get the user input from the text input box
def getInputBoxValue():
    user_input = input_box.get()
    return user_input


root = tk.Tk()
root.title('tklogHandler class show')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fmt = logging.Formatter('%(asctime)s: %(message)s')
"""tkhandler = tklogHandler(master=root)
tkhandler.pack(fill='both', expand=True, side=tk.RIGHT)
tkhandler.setFormatter(fmt)
logger.addHandler(tkhandler)"""

winhandler = winlogHandler(root=root,
                        title='winlogHandler class show',
                        withdrawRoot=True,
                        destroyRoot=True)
winhandler.setFormatter(fmt)
logger.addHandler(winhandler)
# this is the function called when the button is clicked
def btnClickFunction():
    if getInputBoxValue():
        tokenJson = readJson('config')
        key = getInputBoxValue()
        tokenJson['token'] = key
        writeJson('config', tokenJson)
        token_input.destroy()
        logger.debug('clicked')
    else:
        print('error')

try:
    config = readJson('config')
    if config['token']:
        print(config['token'])
    else:
        # create and show the token input window
        token_input = tk.Tk()
        token_input.geometry('460x310')
        token_input.title('Tittle')

        input_box = tk.Entry(token_input)
        input_box.place(x=126, y=26)

        tk.Label(token_input, text='輸入TOKEN', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=36, y=26)

        tk.Button(token_input, text='a', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=286, y=26)

        token_input.mainloop()

except FileNotFoundError:
    config = {
        'token': "",
        'setting2': 'value2',
        'setting3': 'value3'
    }
    with open("config.json", 'w') as f:
        json.dump(config, f)

# show the main window
logger.debug('test')
root.mainloop()

