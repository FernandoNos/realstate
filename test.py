# coding=utf-8
import requests
import json

headers = {'Accept': 'application/json', 'Content-type': 'application/json'}

#Lists all the realties
pesquisa='{"fields": ["Cidade", "Codigo"]}'
url = 'http://sandbox-rest.vistahost.com.br/imoveis/listar?key=c9fdd79584fb8d369a6a579af1a8f681&pesquisa='+pesquisa

response = requests.get(url,headers=headers)
parsed = json.loads(response.text)
print json.dumps(parsed, indent=4, sort_keys=True)
############################################################################
#Updates one realty
url = 'http://sandbox-rest.vistahost.com.br/imoveis/detalhes?key=c9fdd79584fb8d369a6a579af1a8f681&imovel=5170'
headers = {'Accept': 'application/json', 'Content-type': 'application/x-www-form-urlencoded'}

cadastro='cadastro={"fields":{"Endereco":"Anita Gariboaldi","Numero":"553"}}'

response = requests.put(url,headers=headers,data=cadastro)
parsed = json.loads(response.text)
print json.dumps(parsed, indent=4, sort_keys=True, )

############################################################################
#Creates one realty
url = 'http://sandbox-rest.vistahost.com.br/imoveis/detalhes?key=c9fdd79584fb8d369a6a579af1a8f681'
cadastro='{"cadastro":{"fields":{"Categoria":"Apartamento","Endereco":"Rua Victor Meirelles","Complemento":"901","Bairro":"Campinas","Cidade":"São José","UF":"SC","CEP":"88101170","Situacao":"Novo","Ocupacao":"Ocupado"}}}'

#response = requests.post(url,headers=headers,data=cadastro)
#parsed = json.loads(response.text)
#print json.dumps(parsed, indent=4, sort_keys=True, )

############################################################################
#Shows the details of a given realty
url = 'http://sandbox-rest.vistahost.com.br/imoveis/detalhes?key=c9fdd79584fb8d369a6a579af1a8f681&imovel=83&pesquisa={"fields":[{"Anexo":["Anexo","Descricao"]},"Codigo"]}'

response = requests.get(url,headers=headers)
parsed = json.loads(response.text)
print json.dumps(parsed, indent=4, sort_keys=True)


