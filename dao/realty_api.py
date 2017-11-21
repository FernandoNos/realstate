import realty_dao
import json
def listRealtyCodes():
	codes = []
	data = json.loads(realty_dao.listRealties('Codigo'))

	for key, value in data.items():
		codes.append(value['Codigo'])
	return codes

def getRealtyDetail(code):
	data = json.loads(realty_dao.getRealtyDetail(code,'"Codigo","Observacoes"'))
	details = (data['Codigo'],data['Observacoes'])
	return details

def updateRealty(code, obsrv):
	data = json.loads(realty_dao.updateRealty(code,obsrv))
	return data
	