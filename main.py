import tkinter as tk
import json
import os
from windows import App
import sys
import subprocess
from fun import readJson, writeJson






if __name__ == "__main__":

	if os.path.exists("config.json"):    
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
		pass
	else:
		root = tk.Tk()
		app = App(root)
		root.mainloop()
