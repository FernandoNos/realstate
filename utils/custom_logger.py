import os
from time import gmtime, strftime
import io

def logRealty(code, obsrv, page):
	createFolder(page)
	upsertFile(page,code,obsrv)

def createFolder(page):
	date_folder = strftime("%Y-%m-%d", gmtime())
	page_file = '/page_'+str(page)
	print os.getcwd()
	if not os.path.exists('log'):
		os.makedirs('log')
	if not os.path.exists('log/'+date_folder):
		os.makedirs('log/'+date_folder)

def alreadyRun():
	date_folder = strftime("%Y-%m-%d", gmtime())
	return os.path.exists('log/'+date_folder)

def upsertFile(page,code,obsrv):
	f=io.open('log/'+strftime("%Y-%m-%d", gmtime())+'/page_'+str(page)+'.log', 'a+',encoding='utf8')
	f.write(str(code)+' - Descricao antiga:'+obsrv)
	f.write('\n--------------------------------------------------------------------------\n')
	f.close()

