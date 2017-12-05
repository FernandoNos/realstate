import re

def removeDate(obsrv):
	return  re.sub(u'\n[0-9][0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]$', u'',obsrv).replace('"','\\"').encode('utf-8')
	