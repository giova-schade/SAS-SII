/**
  @file
  @brief Delete the records according to GRP_CODIGO value

  <h4> Service Inputs </h4>

  <h5> work.from_ng </h5>

  |GRP_CODIGO:$32.|
  |---|
  |`SOMEVALUE `|


  <h4> SAS Macros </h4>
  @li mp_abort.sas
  @li newrecord.sas
  @li updatecode.sas

**/


/* get data from frontend */
%webout(FETCH)

/* extract variable from input table */
%let GRP_CODIGO=0;
data _null_;
  set work.from_ng;
  call symputx('GRP_CODIGO',GRP_CODIGO);
    call symputx('GRP_DESCRIPCION',GRP_DESCRIPCION);
    call symputx('GRP_NOMBRE',GRP_NOMBRE);
    call symputx('GRP_AREA_NEGOCIO',GRP_AREA_NEGOCIO);
    call symputx('GRP_ESQUEMA_VALIDO',GRP_ESQUEMA_VALIDO);
    call symputx('GRP_HABILITADO',GRP_HABILITADO);
    call symputx('GRP_PERIOCIDAD',GRP_PERIOCIDAD);
    call symputx('GRP_VIGENCIA_FIN',GRP_VIGENCIA_FIN);
    call symputx('GRP_VIGENCIA_INICIO',GRP_VIGENCIA_INICIO);
run;

/* abort if variable not found */
%mp_abort(iftrue= (&GRP_CODIGO=0)
  ,mac=&_program
  ,msg=%str(Debe ingresar un código de segmento)
)

%let CBE_GRUPO_CONTROL=-1;
proc sql noprint;
  select count(*) into :CBE_GRUPO_CONTROL
  from BESASGC.BE_GRUPO_CONTROL
  where GRP_CODIGO="&GRP_CODIGO";

%mp_abort(iftrue= (&CBE_GRUPO_CONTROL>0)
  ,mac=&_program
  ,msg=%str(El código &GRP_CODIGO ya existe!)
)

%NewRecord()

%UpdateCode()

/* return work.response from viewrecord macro */
%webout(OPEN)
%webout(obj,response)
%webout(CLOSE)
