/*
export const CONFIG = {
  apiUrlLogin: 'http://172.16.60.119:5000/Login',
  apiCreaSegmento: 'http://172.16.60.119:5000/apiCreaSegmento',
  apiListGrpCodigo: 'http://172.16.60.119:5000/listGrpCodigo',
  apiUpdateSegmento: 'http://172.16.60.119:5000/updateSegmento',
  apiGetDatosSegmento: 'http://172.16.60.119:5000/datosSegmento',
  listSegment: 'http://172.16.60.119:5000/listSegment',
  apiRemoveSegmento :'http://172.16.60.119:5000/removeSegmento',
  apiLogs: 'http://172.16.60.119:5000/logs',
  apiRun: 'http://172.16.60.119:5000/run',
  apiGetEsquema: 'http://172.16.60.119:5000/getEsquema',
  GRP_CODIGO_LENGTH: 100,
  GRP_ESQUEMA_VALIDO_LENGTH: 4096,
  GRP_NOMBRE_LENGTH: 50,
  GRP_DESCRIPCION_LENGTH: 100,
  GRP_AREA_NEGOCIO_LENGTH:100

};
*/
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
  apiRun: host+'/SASStoredProcess/do?_action=execute&_program=%2FBoleta%2FPrograms%2FBoletaElectronica&ACTION=Start&output=json',
  apiGetEsquema: host+'/SASStoredProcess/do?_action=execute&_program=%2FBoleta%2FPrograms%2FBoletaElectronica&ACTION=GetEsquema&output=json',
  GRP_CODIGO_LENGTH: 100,
  GRP_ESQUEMA_VALIDO_LENGTH: 4096,
  GRP_NOMBRE_LENGTH: 50,
  GRP_DESCRIPCION_LENGTH: 100,
  GRP_AREA_NEGOCIO_LENGTH:100

};