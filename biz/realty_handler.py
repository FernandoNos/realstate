import sys, os
import json

sys.path.append('dao')
from time import gmtime, strftime

import realty_api
import data_handler

def getRealtyCodes():
	return realty_api.listRealtyCodes()

def updateRealty(code,obsrv):
	new_obsrv= data_handler.removeDate(obsrv)
	return realty_api.updateRealty(code,new_obsrv+' '+strftime("%Y-%m-%d %H:%M:%S", gmtime()))

def updateRealties():
	realty_codes = getRealtyCodes()
	response = []
	print 'realty_handler - before making the calls'

	for elem in realty_codes:
		realty = realty_api.getRealtyDetail(elem)
		resp = updateRealty(realty[0],realty[1])
		print 'realty_handler - resp:'+str(resp)
		response.append({'Codigo':resp['Codigo'],'Mensagem':resp['message']})
	
	return str(response)


updateRealties()