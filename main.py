import tkinter as tk
import json
import os
from bot.cool import App, readJson, writeJson

#定義json檔讀寫函式



# this is a function to get the user input from the text input box


if __name__ == "__main__":

	if os.path.exists("bot/config.json"):    
		pass
	else:
		# 創建一個新的設定檔
		config = {
			'token': "",
			'setting2': 'value2',
			'setting3': 'value3'
		}
		writeJson('config', config)


	config = readJson('config')
	if config['token']:
		print(config['token'])
	else:
		root = tk.Tk()
		app = App(root)
		root.mainloop()
