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
		f.write(json.dumps(item, ensure_ascii=False, indent=4))


