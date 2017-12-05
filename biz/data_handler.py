import re

def removeDate(obsrv):
	return  re.sub(u'\n[0-9][0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]$', u'',obsrv).encode('utf-8')
	