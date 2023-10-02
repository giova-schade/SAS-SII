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

@app.route('/runs', methods=['GET'])
def runs():
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
    
@app.route('/VerLogsError', methods=['GET'])
def run():
    if(request.method == 'GET'):
        data = {
  "respuesta": [
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 353,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El código GRPCTRL07 ha sido consultado",
      "LOG_DATETIME": "  06SEP2023:18:19:28.000000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "001"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 350,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El codigo GRPCTRL07 ha sido Creado",
      "LOG_DATETIME": "  05SEP2023:10:19:02.400000",
      "LOG_USUARIO": "jose.vera",
      "LOG_TIPO_EVENTO": "002"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 352,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El código GRPCTRL07 ha sido consultado",
      "LOG_DATETIME": "  06SEP2023:18:15:22.300000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "001"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 357,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "3929      +",
      "LOG_DATETIME": "  07SEP2023:08:44:12.700000",
      "LOG_USUARIO": "jose.vera",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 360,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El código GRPCTRL07 ha sido consultado",
      "LOG_DATETIME": "  07SEP2023:10:26:09.200000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "001"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 380,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "Periodo Actualizado, el codigo GRPCTRL07 no se encontró en la ruta diaria",
      "LOG_DATETIME": "  11SEP2023:10:39:55.200000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "004"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 354,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El código GRPCTRL07 ha sido consultado",
      "LOG_DATETIME": "  06SEP2023:19:24:33.700000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "001"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 358,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/semanal/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  07SEP2023:08:44:32.000000",
      "LOG_USUARIO": "jose.vera",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 361,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/semanal/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  07SEP2023:16:48:11.500000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 362,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "  CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  07SEP2023:17:00:37.800000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 356,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/semanal/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  07SEP2023:08:34:10.900000",
      "LOG_USUARIO": "jose.vera",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 359,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "3929      +",
      "LOG_DATETIME": "  07SEP2023:08:51:31.900000",
      "LOG_USUARIO": "jose.vera",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 379,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El código GRPCTRL07 ha sido consultado",
      "LOG_DATETIME": "  11SEP2023:10:37:39.100000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "001"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 539,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  20SEP2023:14:24:12.300000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 573,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  21SEP2023:10:29:08.200000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 577,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  21SEP2023:10:54:06.200000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 578,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  21SEP2023:10:54:08.500000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 579,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  21SEP2023:10:59:55.700000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 580,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  21SEP2023:10:59:58.000000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 581,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  21SEP2023:11:09:31.600000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 582,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  21SEP2023:11:09:34.200000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 583,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  21SEP2023:11:09:56.600000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 584,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  21SEP2023:11:09:59.000000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 585,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  21SEP2023:12:47:10.000000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 586,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  21SEP2023:12:47:16.800000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 587,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  21SEP2023:13:20:59.100000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 588,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  21SEP2023:13:21:06.300000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 603,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  22SEP2023:10:53:42.300000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 604,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  22SEP2023:10:53:49.500000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 625,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  25SEP2023:14:33:18.700000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 546,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "  CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  20SEP2023:16:24:06.400000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 553,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  20SEP2023:17:10:35.100000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 562,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  21SEP2023:08:05:47.100000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 569,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  21SEP2023:10:26:02.900000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 570,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  21SEP2023:10:26:05.900000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 571,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  21SEP2023:10:26:19.800000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 572,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  21SEP2023:10:26:52.100000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 591,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  21SEP2023:15:50:45.700000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 592,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  21SEP2023:15:50:52.400000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 554,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  20SEP2023:17:11:17.200000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 620,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El código GRPCTRL07 ha sido consultado",
      "LOG_DATETIME": "  25SEP2023:13:23:28.600000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "001"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 538,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El código GRPCTRL07 ha sido consultado",
      "LOG_DATETIME": "  20SEP2023:12:42:04.900000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "001"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 540,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "  CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  20SEP2023:14:37:19.500000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 555,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  20SEP2023:17:11:30.800000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 558,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  20SEP2023:17:21:19.600000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 563,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  21SEP2023:08:05:49.600000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 627,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  25SEP2023:14:46:48.300000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 628,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "No se ha podido obtener el código SAS. No ha sido posible abrir los datos de entrada",
      "LOG_DATETIME": "  25SEP2023:14:52:07.200000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 411,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "  CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  11SEP2023:12:57:03.500000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 544,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "  CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  20SEP2023:15:58:08.800000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 549,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  20SEP2023:16:55:09.700000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 550,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  20SEP2023:16:55:12.000000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 551,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  20SEP2023:17:00:02.600000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 552,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  20SEP2023:17:00:05.100000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 564,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  21SEP2023:09:46:02.300000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 565,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  21SEP2023:09:46:04.800000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 566,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  21SEP2023:09:47:33.700000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 594,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  22SEP2023:08:20:24.400000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 595,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  22SEP2023:08:20:31.700000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 597,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  22SEP2023:08:37:08.000000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 598,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "&syserrortext_",
      "LOG_DATETIME": "  22SEP2023:08:37:15.600000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 601,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  22SEP2023:10:42:39.000000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 602,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "&syserrortext_",
      "LOG_DATETIME": "  22SEP2023:10:42:46.500000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 412,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/diaria/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  11SEP2023:13:24:49.700000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 413,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "  CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  11SEP2023:13:37:14.800000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 542,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "  CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  20SEP2023:15:31:17.900000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 545,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  20SEP2023:16:11:41.600000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 556,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  20SEP2023:17:18:39.900000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 557,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  20SEP2023:17:18:42.200000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 559,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  20SEP2023:17:25:46.600000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 560,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  20SEP2023:17:25:49.000000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 575,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1):",
      "LOG_DATETIME": "  21SEP2023:10:35:10.500000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 599,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  22SEP2023:10:13:18.800000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 600,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "&syserrortext_",
      "LOG_DATETIME": "  22SEP2023:10:13:26.200000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 462,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El código GRPCTRL07 ha sido consultado",
      "LOG_DATETIME": "  12SEP2023:17:00:27.700000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "001"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 463,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "Periodo Actualizado, el codigo GRPCTRL07 no se encontró en la ruta mensual",
      "LOG_DATETIME": "  12SEP2023:17:01:45.100000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "004"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 464,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "Descripción Actualizada",
      "LOG_DATETIME": "  12SEP2023:17:01:45.300000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "004"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 465,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "Vigencia de Inicio Actualizado",
      "LOG_DATETIME": "  12SEP2023:17:01:45.500000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "004"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 541,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  20SEP2023:15:01:19.300000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 567,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  21SEP2023:09:48:37.300000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 574,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  21SEP2023:10:30:46.400000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 589,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  21SEP2023:13:40:05.000000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 590,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1): generic failure: GSSAPI Error: Unspecified GSS failure.  Minor",
      "LOG_DATETIME": "  21SEP2023:13:40:11.700000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 596,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  22SEP2023:08:28:11.700000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 626,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "No se ha podido obtener el código SAS. No ha sido posible abrir los datos de entrada",
      "LOG_DATETIME": "  25SEP2023:14:38:40.900000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 410,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/diaria/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  11SEP2023:12:41:29.400000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 543,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  20SEP2023:15:35:38.300000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 547,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  20SEP2023:16:49:02.400000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 548,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El usuario no valido la tabla creada, debe agregar la macro validaTablaUsuario al proceso GRPCTRL07",
      "LOG_DATETIME": "  20SEP2023:16:49:02.600000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 568,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  21SEP2023:10:22:48.900000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 576,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "CLI error trying to establish connection: [unixODBC][Cloudera][ImpalaODBC] (100) Error from the Impala Thrift API: SASL(-1):",
      "LOG_DATETIME": "  21SEP2023:10:35:25.700000",
      "LOG_USUARIO": "&_METAPERSON",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 605,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa /sasdatad/apps/be/nominas/scheduler/mensual/version/GRPCTRL07_1.00.sas es el primero",
      "LOG_DATETIME": "  22SEP2023:11:03:40.300000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    },
    {
      "GRP_NOMBRE": "MINIMARKET",
      "LOG_UID": 606,
      "GRP_CODIGO": "GRPCTRL07",
      "LOG_EVENTO": "El programa del usuario no creo la tabla GRPCTRL07",
      "LOG_DATETIME": "  22SEP2023:11:03:47.600000",
      "LOG_USUARIO": "ricardo.quezada",
      "LOG_TIPO_EVENTO": "007"
    }
  ]
}
        return jsonify(data)    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
