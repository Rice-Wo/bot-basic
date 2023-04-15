import tkinter as tk
import json
import os
from bot.cool import App, readJson, writeJson
import sys
import subprocess







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
		if os.path.exists("bot.exe"):
			subprocess.Popen("bot/bot.exe")
		else:
			subprocess.Popen(["python", "bot/bot.py"])
	else:
		root = tk.Tk()
		app = App(root)
		root.mainloop()
