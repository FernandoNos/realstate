import sys, os
import json


sys.path.append('dao')
sys.path.append('utils')
from time import gmtime, strftime

import custom_logger
import realty_api
import data_handler

def getRealtyCodes(page):
	return realty_api.listRealtyCodes(page)

def updateRealty(code,obsrv):
	new_obsrv= data_handler.removeDate(obsrv)
	return realty_api.updateRealty(u''+code,new_obsrv+' \n'+strftime("%Y-%m-%d", gmtime()))

def alreadyRun():
	return custom_logger.alreadyRun()

def updateRealties():
	page = 4
	pages = 4
	response = []

	if not alreadyRun():
		print 'starting page'
		while page<=pages:
			resp = getRealtyCodes(page)
			resp1 = int(resp[0][1])
			resp2 = int(resp[1][1])
			page = resp1 if resp1 <= resp2 else resp2
			pages =  resp1 if resp1 >= resp2 else resp2 
			realty_codes = resp[2][1]
			print str(page)+' '+str(pages)
			for elem in realty_codes:
				if str(elem)=='':
					continue
				realty = realty_api.getRealtyDetail(elem)
				custom_logger.logRealty(elem,realty[1],page)
				resp = updateRealty(realty[0],realty[1])
				response.append({'Codigo':resp['Codigo'],'Mensagem':resp['message']})
				print response
			page = page + 1
			return ''
		return ''
	print response
	return str(response)

