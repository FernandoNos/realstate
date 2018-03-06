import sys, os
import json


sys.path.append('dao')
sys.path.append('utils')
from time import gmtime, strftime

import realty_api
import data_handler
import logging

def getRealtyCodes(page):
	return realty_api.listRealtyCodes(page)

def updateRealty(code,obsrv):
	new_obsrv= data_handler.removeDate(obsrv)
	return realty_api.updateRealty(u''+code,new_obsrv+' \nUltima atualizacao:'+strftime("%Y-%m-%d", gmtime()))

def updateRealties():
	page = 22
	pages = 1
	response = []

	
	while page<=pages:
		resp = getRealtyCodes(page)
		resp1 = int(resp[0][1])
		resp2 = int(resp[1][1])
		page = resp1 if resp1 <= resp2 else resp2
		pages =  resp1 if resp1 >= resp2 else resp2 
		realty_codes = resp[2][1]
		print str(page)+' '+str(pages)
		logging.info(('Page:'+str(page)+',Total='+str(pages)).encode('utf-8'))
		for elem in realty_codes:
			if str(elem)=='':
				continue
			realty = realty_api.getRealtyDetail(elem)
			logging.info(('Descricao antiga('+realty[0]+':'+realty[1]).encode('utf-8'))
			print('Updating '+realty[0].encode('utf-8'))
			resp = updateRealty(realty[0],realty[1])
			print (('Response: '+str(resp)).encode('utf-8'))
			
			if resp['status']==200:
				print ('-->'+str(resp['Codigo'])+': updated').encode('utf-8')
				logging.info(('Response: '+str(resp)).encode('utf-8'))
				logging.info(('\n\n------------------------------------------------------------------------\n').encode('utf-8'))
				response.append({'Codigo':resp['Codigo'],'Mensagem':resp['message']})
			else:
				print ('-->Error:'+'Request:'+str(realty)+'Response:'+str(resp)).encode('utf-8')
		page = page + 1
		logging.info(('\n\n###################################################################\n\n').encode('utf-8'))

	return str(response)
