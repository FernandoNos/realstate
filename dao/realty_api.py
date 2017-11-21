import realty_dao
import json
def listRealtyCodes():
	codes = []
	resp = []
	pagination = []
	data = json.loads(realty_dao.listRealties('Codigo'))
	for key, value in data.items():
		if 'Codigo' in str(value):
			codes.append(value['Codigo'])
		else:
			if key == 'paginas' or key == 'pagina':
				resp.append((str(key),str(value)))
	resp.insert(2,('codes',codes))
	
	return resp

def getRealtyDetail(code):
	data = json.loads(realty_dao.getRealtyDetail(code,'"Codigo","Observacoes"'))
	details = (data['Codigo'],data['Observacoes'])
	return details

def updateRealty(code, obsrv):
	data = json.loads(realty_dao.updateRealty(code,obsrv))
	return data
	