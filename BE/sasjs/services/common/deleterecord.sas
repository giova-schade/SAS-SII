/**
  @file
  @brief Delete the records according to GRP_CODIGO value

  <h4> SAS Macros </h4>
  @li mp_abort.sas
  @li insertevent.sas
  @li deleterecord.sas
  @li messagebe.sas

**/


/* get data from frontend */
%webout(FETCH)

%let GRP_CODIGO=0;
data _null_;
  set work.from_ng;
  call symputx('GRP_CODIGO',GRP_CODIGO);
run;

%mp_abort(iftrue= (&GRP_CODIGO=0)
  ,mac=&_program
  ,msg=%str(Debe ingresar un código de segmento)
)

%let mensaje = "El código &GRP_CODIGO ha sido eliminado";

%InsertEvent(GRP_CODIGO="&GRP_CODIGO",
  LOG_EVENTO=&mensaje,
  LOG_USUARIO="&_METAPERSON",
  LOG_TIPO_EVENTO="005"
)

%DeleteRecord(&GRP_CODIGO)

%webout(OPEN)
%webout(obj,response)
%webout(CLOSE)
