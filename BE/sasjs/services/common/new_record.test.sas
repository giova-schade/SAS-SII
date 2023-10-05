/**
  @file
  @brief testing getrawdata service

  <h4> SAS Macros </h4>
  @li mp_assert.sas
  @li mx_testservice.sas

**/


%let _program=&appLoc/services/common/new_record;

data work.from_ng;
  GRP_CODIGO='TEST';
  GRP_DESCRIPCION='TEST';
  GRP_NOMBRE='TEST';
  GRP_AREA_NEGOCIO='TEST';
  GRP_ESQUEMA_VALIDO='{"test":"test"}';
  GRP_HABILITADO=1;
  GRP_PERIOCIDAD=1;
  GRP_VIGENCIA_FIN='26Oct2023';
  GRP_VIGENCIA_INICIO='26Oct2023';
  output;
  stop;
run;

%mx_testservice(&_program,
  inputdatasets=from_ng,
  outref=webout,
  mdebug=1
)

/*
  Whatever the above returns, you can actually capture it and test it properly
  DM me when ready
*/
data _null_;
  infile webout;
  input;
  putlog _infile_;
run;


%mp_assert(
  iftrue=(&syscc=0),
  desc=Checking final err condition,
  outds=work.test_results
)


%webout(OPEN)
%webout(OBJ, TEST_RESULTS)
%webout(CLOSE)