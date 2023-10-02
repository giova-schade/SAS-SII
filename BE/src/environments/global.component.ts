/*
export const CONFIG = {
  apiUrlLogin: 'http://10.34.134.138:5000/Login',
  apiCreaSegmento: 'http://10.34.134.138:5000/apiCreaSegmento',
  apiListGrpCodigo: 'http://10.34.134.138:5000/listGrpCodigo',
  apiUpdateSegmento: 'http://10.34.134.138:5000/updateSegmento',
  apiGetDatosSegmento: 'http://10.34.134.138:5000/datosSegmento',
  listSegment: 'http://10.34.134.138:5000/listSegment',
  apiRemoveSegmento :'http://10.34.134.138:5000/removeSegmento',
  apiLogs: 'http://10.34.134.138:5000/logs',
  apiRun: 'http://10.34.134.138:5000/run',
  apiVerLogsError: 'http://10.34.134.138:5000/VerLogsError',
  apiGetEsquema: 'http://10.34.134.138:5000/getEsquema',
  GRP_CODIGO_LENGTH: 100,
  GRP_ESQUEMA_VALIDO_LENGTH: 4096,
  GRP_NOMBRE_LENGTH: 50,
  GRP_DESCRIPCION_LENGTH: 100,
  GRP_AREA_NEGOCIO_LENGTH:100

};*/


var host = window.location.origin;
export const CONFIG = {
  apiUrlLogin: host+'/SASStoredProcess/do?_action=execute&_program=%2FBoleta%2FPrograms%2FBoletaElectronica&ACTION=Login',
  apiCreaSegmento: host+'/SASStoredProcess/do?_action=execute&_program=%2FBoleta%2FPrograms%2FBoletaElectronica&ACTION=NewRecord&output=json',
  apiListGrpCodigo: host+'/SASStoredProcess/do?_action=execute&_program=%2FBoleta%2FPrograms%2FBoletaElectronica&ACTION=GRP_CODIGOS&output=json',
  apiUpdateSegmento: host+'/SASStoredProcess/do?_action=execute&_program=%2FBoleta%2FPrograms%2FBoletaElectronica&ACTION=UpdateRecord&output=json',
  apiGetDatosSegmento: host+'/SASStoredProcess/do?_action=execute&_program=%2FBoleta%2FPrograms%2FBoletaElectronica&ACTION=ViewRecord&output=json',
  listSegment: host+'/SASStoredProcess/do?_action=execute&_program=%2FBoleta%2FPrograms%2FBoletaElectronica&ACTION=ViewRecord&output=json',
  apiRemoveSegmento : host+'/SASStoredProcess/do?_action=execute&_program=%2FBoleta%2FPrograms%2FBoletaElectronica&ACTION=DeleteRecord&output=json',
  apiLogs: host+'/SASStoredProcess/do?_action=execute&_program=%2FBoleta%2FPrograms%2FBoletaElectronica&ACTION=VerLogs&output=json',
  apiVerLogsError: '/SASStoredProcess/do?_action=execute&_program=%2FBoleta%2FPrograms%2FBoletaElectronica&ACTION=VerLogsError&output=json',
  apiRun: host+'/SASStoredProcess/do?_action=execute&_program=%2FBoleta%2FPrograms%2FBoletaElectronica&ACTION=Start&output=json',
  apiGetEsquema: host+'/SASStoredProcess/do?_action=execute&_program=%2FBoleta%2FPrograms%2FBoletaElectronica&ACTION=GetEsquema&output=json',
  GRP_CODIGO_LENGTH: 100,
  GRP_ESQUEMA_VALIDO_LENGTH: 4096,
  GRP_NOMBRE_LENGTH: 50,
  GRP_DESCRIPCION_LENGTH: 100,
  GRP_AREA_NEGOCIO_LENGTH:100

};