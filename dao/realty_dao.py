import requests
import json
import sys,os
import logging 

sys.path.append('utils')
import initializer
#c9fdd79584fb8d369a6a579af1a8f681

URL = initializer.getURL()
KEY = initializer.getKey()

def listRealties(fields,page):
	headers = {'Accept': 'application/json', 'Content-type': 'application/json'}

	#Lists all the realties
	pesquisa='{"fields": ["'+fields+'"],"filter":{"ImobiliariaCadastro":"PLANEJAR ASSESSORIA IMOBILIARIA"},"paginacao":{"pagina":'+str(page)+',"quantidade":50}}'
	url = URL+'/imoveis/listar?key='+KEY+'&showtotal=1&pesquisa='+pesquisa

	response = requests.get(url,headers=headers)
	return response.text

def getRealtyDetail(code,fields):
	headers = {'Accept': 'application/json', 'Content-type': 'application/json'}

	url = URL+'/imoveis/detalhes?key='+KEY+'&imovel='+code+'&pesquisa={"fields":['+fields+']}'

	response = requests.get(url,headers=headers)
	return response.text

def updateRealty(code, obsrv):

	headers = {'Accept': 'application/json', 'Content-type': 'application/x-www-form-urlencoded'}
	url = URL+'/imoveis/detalhes?key='+KEY+'&imovel='+code
	cadastro='cadastro={"fields":{"Descricao":"'+obsrv+'"}}'
	logging.info('cadastr='+str(cadastro))
	response = requests.put(url, headers=headers,data=cadastro)
	return response.text

