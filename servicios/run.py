from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/Login', methods=['GET'])
def Login():
    if(request.method == 'GET'):
        data = {
    "role": "BEADM",
    "Nombre": "sasdemo",
    "roleDescription": "Analista Budget RRHH",
    "info": {
        "sede": [
            {
                "IdCia": "AKDSEDE21",
                "NomSede": "AKD INTERNATIONAL PANAMA CORP."
            },
             {
                "IdCia": "AKDSEDE21",
                "NomSede": "AKD INTERNATIONAL PANAMA CORP."
            }
        ]
    }
}

        return jsonify(data)


@app.route('/apiCreaSegmento', methods=['GET'])
def apiCreaSegmento():
    if(request.method == 'GET'):
        data = {
            "respuesta": [
                {
                    "respuesta": [
                        {
                            "MENSAJE": "El nombre BotillerÃ¬as ya existe!"
                        }
                    ]
                }]
        }
        return jsonify(data)


@app.route('/datosSegmento', methods=['GET'])
def datosSegmento():
    if(request.method == 'GET'):
        data = {
            "respuesta": [
                {
                    "GRP_CODIGO": "grpctl_01",
                    "GRP_NOMBRE": "BOTILLERÍAS",
                    "GRP_DESCRIPCION": "VENTA DE BEBIDAS ALCOHÓLICAS Y NO ALCOHÓLICAS EN COMERCIOS ESPECIALIZADOS",
                    "GRP_DATE_CREADO": "19/04/2022 09:20:13",
                    "GRP_USER_CREADO": "s14325174",
                    "GRP_DATE_MODIFICADO": "19/04/2022 09:22:19",
                    "GRP_USER_MODIFICADO": "s14325174",
                    "GRP_VERSION": 1.01,
                    "GRP_AREA_NEGOCIO": "ÁREA DE RIESGOS ESPECÍFICOS IVA",
                    "GRP_VIGENCIA_INICIO": Null,
                    "GRP_VIGENCIA_FIN": Null,
                    "GRP_ESQUEMA_VALIDO": "",
                    "GRP_ESTADO": 1,
                    "PROC_DATE_PROCESO": "               .",
                    "PROC_CANT_REGISTROS": Null,
                    "GRP_PERIOCIDAD": "Semanal",
                    "GRP_HABILITADO": "Deshabilitado"
                }
            ]
        }
        return jsonify(data)


@app.route('/getEsquema', methods=['GET'])
def getEsquema():
    if(request.method == 'GET'):
        data = {
            "fields": [
                {
                    "metadata": {},
                    "name": "rut",
                    "Nullable": False,
                    "type": "long"
                },
                {
                    "metadata": {},
                    "name": "dv",
                    "Nullable": False,
                    "type": "string"
                },
                {
                    "metadata": {},
                    "name": "email",
                    "Nullable": False,
                    "type": "string"
                },
                {
                    "metadata": {},
                    "name": "fecha",
                    "Nullable": False,
                    "type": "timestamp"
                },
                {
                    "metadata": {},
                    "name": "segmento",
                    "Nullable": False,
                    "type": "string"
                },
                {
                    "name": "parametros",
                    "type": {
                        "elementType": {
                            "fields": [
                                {
                                    "metadata": {},
                                    "name": "DR",
                                    "Nullable": False,
                                    "type": "long"
                                },
                                {
                                    "metadata": {},
                                    "name": "tamanio",
                                    "Nullable": False,
                                    "type": "string"
                                },
                                {
                                    "metadata": {},
                                    "name": "inferior_hora_inicio",
                                    "Nullable": False,
                                    "type": "timestamp"
                                },
                                {
                                    "metadata": {},
                                    "name": "inferior_hora_cierre",
                                    "Nullable": False,
                                    "type": "timestamp"
                                },
                                {
                                    "metadata": {},
                                    "name": "superior_hora_inicio",
                                    "Nullable": False,
                                    "type": "timestamp"
                                },
                                {
                                    "metadata": {},
                                    "name": "superior_hora_cierre",
                                    "Nullable": False,
                                    "type": "timestamp"
                                },
                                {
                                    "metadata": {},
                                    "name": "valor_defecto_1",
                                    "Nullable": False,
                                    "type": "string"
                                },
                                {
                                    "metadata": {},
                                    "name": "valor_defecto_2",
                                    "Nullable": False,
                                    "type": "string"
                                }
                            ],
                            "type": "struct"
                        },
                        "type": "array"
                    }
                }
            ],
            "type": "struct"
        }
        return jsonify(data)


@app.route('/listGrpCodigo', methods=['GET'])
def listGrpCodigo():
    if(request.method == 'GET'):
        data = {
            "respuesta": [
                {
                    "GRP_CODIGO": "grpctl_01"
                },
                {
                    "GRP_CODIGO": "grpctl_b"
                },
                {
                    "GRP_CODIGO": "test01"
                },
                {
                    "GRP_CODIGO": "test025"
                },
                {
                    "GRP_CODIGO": "test05"
                },
                {
                    "GRP_CODIGO": "test07"
                },
                {
                    "GRP_CODIGO": "test_01"
                }
            ]
        }
        return jsonify(data)


@app.route('/listSegment', methods=['GET'])
def listSegment():
    if(request.method == 'GET'):
        data = {
            "respuesta": [
                {
                    "GRP_CODIGO": "TEST01",
                    "GRP_NOMBRE": "TEST01",
                    "GRP_DESCRIPCION": "TEST01",
                    "GRP_HABILITADO": 0,
                    "GRP_DATE_CREADO": "19/04/2022 12:22:12",
                    "GRP_USER_CREADO": "s14325174",
                    "GRP_DATE_MODIFICADO": "19/04/2022 12:22:12",
                    "GRP_USER_MODIFICADO": "s14325174",
                    "GRP_VERSION": 1,
                    "GRP_PERIOCIDAD": 0,
                    "GRP_AREA_NEGOCIO": "TEST01",
                    "GRP_VIGENCIA_INICIO": "19/04/2022",
                    "GRP_VIGENCIA_FIN": "19/04/2022",
                    "GRP_ESQUEMA_VALIDO": "",
                    "GRP_ESTADO": 1
                },
                {
                    "GRP_CODIGO": "GRPCRTL01",
                    "GRP_NOMBRE": "BOTILLERÍAS",
                    "GRP_DESCRIPCION": "VENTA DE BEBIDAS ALCOHÓLICAS Y NO ALCOHÓLICAS EN COMERCIOS ESPECIALIZADOS",
                    "GRP_HABILITADO": 0,
                    "GRP_DATE_CREADO": "19/04/2022 09:20:13",
                    "GRP_USER_CREADO": "s14325174",
                    "GRP_DATE_MODIFICADO": "19/04/2022 09:22:19",
                    "GRP_USER_MODIFICADO": "s14325174",
                    "GRP_VERSION": 1.01,
                    "GRP_PERIOCIDAD": 2,
                    "GRP_AREA_NEGOCIO": "ÁREA DE RIESGOS ESPECÍFICOS IVA",
                    "GRP_VIGENCIA_INICIO": null,
                    "GRP_VIGENCIA_FIN": Null,
                    "GRP_ESQUEMA_VALIDO": "",
                    "GRP_ESTADO": 1
                },
                {
                    "GRP_CODIGO": "GRPCRTL00",
                    "GRP_NOMBRE": "OBLIGADOS",
                    "GRP_DESCRIPCION": "UNIVERSO DE CONTRIBUYENTES OBLIGADOS A ENTREGAR BOLETA ELECTRÓNICA",
                    "GRP_HABILITADO": 1,
                    "GRP_DATE_CREADO": "19/04/2022 08:37:47",
                    "GRP_USER_CREADO": "s14325174",
                    "GRP_DATE_MODIFICADO": "19/04/2022 09:16:41",
                    "GRP_USER_MODIFICADO": "s14325174",
                    "GRP_VERSION": 1.01,
                    "GRP_PERIOCIDAD": 1,
                    "GRP_AREA_NEGOCIO": "ÁREA DE RIESGOS ESPECÍFICOS IVA",
                    "GRP_VIGENCIA_INICIO": "01/03/2022",
                    "GRP_VIGENCIA_FIN": "31/12/2022",
                    "GRP_ESQUEMA_VALIDO": "",
                    "GRP_ESTADO": 1
                }
            ]
        }
        return jsonify(data)


@app.route('/logs', methods=['POST'])
def logs():
    if(request.method == 'POST'):
        data = {"respuesta": [{"GRP_NOMBRE": "RESTAURANTES", "LOG_UID": 408, "GRP_CODIGO": "GRPCTRL03", "LOG_EVENTO": "El codigo GRPCTRL03 ha sido Creado", "LOG_DATETIME": " 09MAY2022:09:39:41.900000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "002"}, {"GRP_NOMBRE": "CARNICERÍA", "LOG_UID": 410, "GRP_CODIGO": "GRPCTRL05", "LOG_EVENTO": "El codigo GRPCTRL05 ha sido Creado", "LOG_DATETIME": " 09MAY2022:09:40:45.600000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "002"}, {"GRP_NOMBRE": "OBLIGADOS", "LOG_UID": 411, "GRP_CODIGO": "GRPCTRL00", "LOG_EVENTO": "El código GRPCTRL00 ha sido consultado", "LOG_DATETIME": " 09MAY2022:09:41:02.700000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "001"}, {"GRP_NOMBRE": "OBLIGADOS", "LOG_UID": 412, "GRP_CODIGO": "GRPCTRL00", "LOG_EVENTO": "Esquema actualizado versión &N_GRP_VERSION.", "LOG_DATETIME": " 09MAY2022:09:41:35.100000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "004"}, {"GRP_NOMBRE": "OBLIGADOS", "LOG_UID": 413, "GRP_CODIGO": "GRPCTRL00", "LOG_EVENTO": "Estado Actualizado", "LOG_DATETIME": " 09MAY2022:09:41:35.200000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "004"}, {"GRP_NOMBRE": "OBLIGADOS", "LOG_UID": 414, "GRP_CODIGO": "GRPCTRL00", "LOG_EVENTO": "Estado Actualizado a Desactivado", "LOG_DATETIME": " 09MAY2022:09:41:35.300000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "004"}, {"GRP_NOMBRE": "OBLIGADOS", "LOG_UID": 415, "GRP_CODIGO": "GRPCTRL00", "LOG_EVENTO": "Esquema actualizado versión &N_GRP_VERSION.", "LOG_DATETIME": " 09MAY2022:09:42:26.000000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "004"}, {
            "GRP_NOMBRE": "OBLIGADOS", "LOG_UID": 417, "GRP_CODIGO": "GRPCTRL00", "LOG_EVENTO": "Estado Actualizado a Activado", "LOG_DATETIME": " 09MAY2022:09:43:39.100000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "004"}, {"GRP_NOMBRE": "OBLIGADOS", "LOG_UID": 405, "GRP_CODIGO": "GRPCTRL00", "LOG_EVENTO": "El codigo GRPCTRL00 ha sido Creado", "LOG_DATETIME": " 09MAY2022:09:37:27.700000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "002"}, {"GRP_NOMBRE": "OBLIGADOS", "LOG_UID": 418, "GRP_CODIGO": "GRPCTRL00", "LOG_EVENTO": "Estado Actualizado a Desactivado", "LOG_DATETIME": " 09MAY2022:09:43:45.900000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "004"}, {"GRP_NOMBRE": "OBLIGADOS", "LOG_UID": 416, "GRP_CODIGO": "GRPCTRL00", "LOG_EVENTO": "El código GRPCTRL00 ha sido consultado", "LOG_DATETIME": " 09MAY2022:09:43:18.000000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "001"}, {"GRP_NOMBRE": "BOTILLERÍAS", "LOG_UID": 406, "GRP_CODIGO": "GRPCTRL01", "LOG_EVENTO": "El codigo GRPCTRL01 ha sido Creado", "LOG_DATETIME": " 09MAY2022:09:38:31.800000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "002"}, {"GRP_NOMBRE": "PANADERÍA Y PASTELERÍA", "LOG_UID": 407, "GRP_CODIGO": "GRPCTRL02", "LOG_EVENTO": "El codigo GRPCTRL02 ha sido Creado", "LOG_DATETIME": " 09MAY2022:09:39:02.200000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "002"}, {"GRP_NOMBRE": "VERDULERÍA", "LOG_UID": 409, "GRP_CODIGO": "GRPCTRL04", "LOG_EVENTO": "El codigo GRPCTRL04 ha sido Creado", "LOG_DATETIME": " 09MAY2022:09:40:23.500000", "LOG_USUARIO": "s14325174", "LOG_TIPO_EVENTO": "002"}]}
        return jsonify(data)


@app.route('/removeSegmento', methods=['GET'])
def removeSegmento():
    if(request.method == 'GET'):
        data = {
            "respuesta": [
                {
                    "respuesta": [
                        {
                            "MENSAJE": "El nombre BotillerÃ¬as ya existe!"
                        }
                    ]
                }]
        }
        return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
