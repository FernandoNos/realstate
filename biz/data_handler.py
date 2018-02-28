import re

def removeDate(obsrv):
	return  re.sub(u'\n(Ultima atualizacao:)?[0-9][0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]$', u'',obsrv).replace('"','\\"').replace('\\\\\"','\\\"').replace('\'','\\\'').replace('&#039;','\'').encode('utf-8')
	