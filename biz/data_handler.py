import re

def removeDate(obsrv):
	return  re.sub(r'[0-9][0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9][0-9]$', '',obsrv)
	