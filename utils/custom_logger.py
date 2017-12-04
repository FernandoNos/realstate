import os
from time import gmtime, strftime

def logRealty(code, obsrv, page):
	createFolder(page)
	upsertFile(page,code,obsrv)

def createFolder(page):
	date_folder = strftime("%Y-%m-%d", gmtime())
	page_file = '/page_'+str(page)
	if not os.path.exists('log'):
		os.makedirs('log')
	if not os.path.exists('log/'+date_folder):
		os.makedirs('log/'+date_folder)

def alreadyRun():
	date_folder = strftime("%Y-%m-%d", gmtime())
	return os.path.exists('log/'+date_folder)

def upsertFile(page,code,obsrv):
	f=open('log/'+strftime("%Y-%m-%d", gmtime())+'/page_'+str(page)+'.log', 'a+')
	f.write(str(code)+' - Descricao antiga:'+obsrv)
	f.write('\n--------------------------------------------------------------------------\n')
	f.close()

