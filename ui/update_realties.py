import sys
import json
sys.path.append('../biz')
import realty_handler

def test():
	data = json.loads(realty_handler.updateRealties())
	