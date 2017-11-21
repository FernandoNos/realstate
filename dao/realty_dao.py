import requests
import json

def listRealties(fields):
	headers = {'Accept': 'application/json', 'Content-type': 'application/json'}

	#Lists all the realties
	pesquisa='{"fields": ["'+fields+'"],"paginacao":{"pagina":1,"quantidade":50}}'
	url = 'http://sandbox-rest.vistahost.com.br/imoveis/listar?key=c9fdd79584fb8d369a6a579af1a8f681&showtotal=1&pesquisa='+pesquisa

	response = requests.get(url,headers=headers)
	return response.text

def getRealtyDetail(code,fields):
	headers = {'Accept': 'application/json', 'Content-type': 'application/json'}

	url = 'http://sandbox-rest.vistahost.com.br/imoveis/detalhes?key=c9fdd79584fb8d369a6a579af1a8f681&imovel='+code+'&pesquisa={"fields":['+fields+']}'

	response = requests.get(url,headers=headers)
	return response.text

def updateRealty(code, obsrv):

	headers = {'Accept': 'application/json', 'Content-type': 'application/x-www-form-urlencoded'}

	url = 'http://sandbox-rest.vistahost.com.br/imoveis/detalhes?key=c9fdd79584fb8d369a6a579af1a8f681&imovel='+code
	cadastro='cadastro={"fields":{"Observacoes":"'+obsrv+'"}}'

	response = requests.put(url, headers=headers,data=cadastro)
	return response.text

