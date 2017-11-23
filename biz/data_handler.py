import re

def removeDate(obsrv):
	return  re.sub(r'\n[0-9][0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]$', '',obsrv)
	