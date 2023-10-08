/**
  @file
  @brief WORK NEEDED
  @details All the invoked macros need to be listed below

  <h4> SAS Macros </h4>
  @li cargaestrucutra.sas
  @li increasesversionvalida.sas
  @li insertevent.sas
  @li messagebe.sas
  @li mf_getvarlen.sas
  @li mp_abort.sas
  @li salidaweb.sas
  @li validoschema.sas
  @li viewrecord.sas

**/
%macro NewRecord();

  %let LARGO_ESQUEMA=%mf_getvarlen(BESASGC.BE_GRUPO_CONTROL,GRP_ESQUEMA_VALIDO);

  %mp_abort(iftrue= (%length(&GRP_ESQUEMA_VALIDO.) gt &LARGO_ESQUEMA)
    ,mac=&_program
    ,msg=%str(
      El esquema es mayor a &LARGO_ESQUEMA  debe quitar los espacio o acortar el
      esquema!
    )
  )

  PROC SQL NOPRINT;
  SELECT COUNT(*) INTO :GRP_NOMBRE_EXIST
    FROM BESASGC.BE_GRUPO_CONTROL
    WHERE GRP_NOMBRE="&GRP_NOMBRE";

  %mp_abort(iftrue= (&GRP_NOMBRE_EXIST gt 0)
    ,mac=&_program
    ,msg=%str(El nombre &GRP_NOMBRE ya existe!)
  )

  /*
    se vambia a distinto de 0 ya que en el futuro se debe cargar desde un
    archivo json
  */
  %validoSchema(json="&GRP_ESQUEMA_VALIDO")
  %mp_abort(iftrue= (%length(&ErrorEsquema) ne 0)
    ,mac=&_program
    ,msg=%str(El esquema esta incorrecto!)
  )

  libname CFGJSON JSON  fileref =jsonFile automap=replace;
  data _null_;
    p_fecha=datetime();
    VIGENCIA_INICIO=input("&GRP_VIGENCIA_INICIO  0:00:00", datetime20.);
    VIGENCIA_FIN=input("&GRP_VIGENCIA_FIN  0:00:00", datetime20.);
    codigo = compress("&GRP_CODIGO");
    call symputx('fecha_proc',p_fecha);
    call symputx('GRP_CODIGO',codigo);
    call symput('VIGENCIA_INICIO', VIGENCIA_INICIO);
    call symput('VIGENCIA_FIN', VIGENCIA_FIN);
  run;
  proc sql  noprint;
    insert into BESASGC.BE_GRUPO_CONTROL(
                  GRP_CODIGO,
                  GRP_NOMBRE,
                  GRP_DESCRIPCION,
                  GRP_HABILITADO,
                  GRP_USER_CREADO,
                  GRP_USER_MODIFICADO,
                  GRP_VERSION,
                    GRP_ESTADO,
                  GRP_AREA_NEGOCIO,
                  GRP_ESQUEMA_VALIDO,
                  GRP_PERIOCIDAD,
                  GRP_VIGENCIA_INICIO,
                  GRP_VIGENCIA_FIN)
    values (
      "&GRP_CODIGO",
      "&GRP_NOMBRE",
      "&GRP_DESCRIPCION",
      &GRP_HABILITADO,
      "&_METAPERSON",
      "&_METAPERSON",
      1.00,
              0,
      "&GRP_AREA_NEGOCIO",
      "&GRP_ESQUEMA_VALIDO",
      &GRP_PERIOCIDAD.,
      &VIGENCIA_INICIO,
      &VIGENCIA_FIN
    ) ;
  quit;
  %increasesVersionValida(GRP_CODIGO=&GRP_CODIGO);
  %InsertEvent(GRP_CODIGO="&GRP_CODIGO",
  LOG_EVENTO="El codigo &GRP_CODIGO ha sido Creado",
  LOG_USUARIO="&_METAPERSON",
  LOG_TIPO_EVENTO="002");
  %cargaEstrucutra(_programa=&GRP_CODIGO);

  %ViewRecord(tabla=BE_GRUPO_CONTROL,reg=&GRP_CODIGO)

%mend NewRecord;