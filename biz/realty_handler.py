import sys, os
import json

sys.path.append('dao')
from time import gmtime, strftime

import realty_api
import data_handler

def getRealtyCodes(page):
	return realty_api.listRealtyCodes(page)

def updateRealty(code,obsrv):
	new_obsrv= data_handler.removeDate(obsrv)
	return realty_api.updateRealty(code,new_obsrv+' '+strftime("%Y-%m-%d %H:%M:%S", gmtime()))

def updateRealties():

	page = 3
	pages = -1

	while page != pages:
		resp = getRealtyCodes(page)
		pages = int(resp[0][1])
		page = int(resp[1][1])
		print str(pages) + ' ' + str(page)
		realty_codes = resp[2][1]
		response = []
		for elem in realty_codes:
			if str(elem)=='':
				continue
			print elem
			realty = realty_api.getRealtyDetail(elem)
			resp = updateRealty(realty[0],realty[1])
			response.append({'Codigo':resp['Codigo'],'Mensagem':resp['message']})
		print 'updating page'
		page = page + 1
		print 'page updated = '+str(page)
	return str(response)