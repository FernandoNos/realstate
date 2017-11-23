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
	return realty_api.updateRealty(code,new_obsrv+' \n'+strftime("%Y-%m-%d", gmtime()))

def updateRealties():
	page = 1
	pages = -1
	response = []
	while page!=pages+1:
		resp = getRealtyCodes(page)
		pages = int(resp[0][1])
		page = int(resp[1][1])
		realty_codes = resp[2][1]
		print str(page)+' '+str(pages)
		for elem in realty_codes:
			if str(elem)=='':
				continue
			realty = realty_api.getRealtyDetail(elem)
			custom_logger.logRealty(elem,realty[1],page)
			resp = updateRealty(realty[0],realty[1])
			response.append({'Codigo':resp['Codigo'],'Mensagem':resp['message']})
		page = page + 1
	return str(response)

