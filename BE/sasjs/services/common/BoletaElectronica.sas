%let dtlog = aeslog_%sysfunc(compress(%sysfunc(putn(%sysfunc(date()),yymmdd7.))))_%sysfunc(compress(%sysfunc(tranwrd(%sysfunc(putn(%sysfunc(time()),time.)),:,))));

proc printto log="/sasdatad/apps/be/nominas/logs/&_METAUSER._&ACTION._apiWeb_&dtlog..log" new; 
run;

options urlencoding="UTF8";

    
%put ---------------> &GRP_CODIGO;
%global GRP_ESQUEMA_VALIDO
        GRP_PERIOCIDAD
        GRP_ESTADO
        GRP_CODIGO
        ACTION
        ErrorEsquema
        mueve
        GRP_PER_ORIGEN
        GRP_PER_DESTINO
        GRP_VIGENCIA_INICIO
        GRP_VIGENCIA_FIN
        grpexist
        groupname
          NEW_GRP_VERSION
        FechaLogs
        UsuarioLogs
        SegmentoLogs 
            p_user 
        p_tabla role_
        ESQUEMA_VALIDO_CHANGE
log 
FECHALOGS_MAX
FECHALOGS_MIN
N_GRP_VERSION;
%PUT _ALL_;
%let p_tabla=users_list;
%let p_user="&_METAPERSON";


/*%let GRP_ESQUEMA_VALIDO = ;
%let GRP_PERIOCIDAD = 1;
%let GRP_ESTADO= 0;
%let GRP_CODIGO =grpctl_01;
%let ACTION =NewRecord;
*/


*# Exponer JSON en webout_ #*;


%macro setMetaperson();
%put _METAPERSON:[&_METAPERSON];
%put _METAUSER:[&_METAUSER];
%put SYSUSERID:[&SYSUSERID];

%if %length(&_METAPERSON) eq 0 %then %do;
    %if %length(&_METAUSER) eq 0 %then %do;
        %IF %LENGTH (&SYSUSERID) eq  0 %THEN %DO;
            %let _METAPERSON =usuario no encontrado;
        %END;
        %else %do;
            %let _METAPERSON =&SYSUSERID;
        %end;
    %end;
    %else %do;
        %let _METAPERSON =&_METAUSER;
    %end;
%end;
%else %do;
%let _METAPERSON =&_METAUSER;
%end;
%mend;



%macro get_user(_user=,_tabla=, role_=);

    proc json out = _webout pretty nosastags ;
        write open object;
        write values "role" "&role_";
        write values "Nombre" &_user;
        write values "info";
        write open object;

        write close;
        write close;
    run;

%mend get_user;

*# Obtener la lista de GRUPOS Y ROLES por usuario en session#*;
%macro get_meta_groups(_user=);
    data users_list_temp;
        length uri name group groupuri desgroup grouptype $256;
        length id MDUpdate $20;
        n=1;


        call missing(uri, name, group, groupuri, desgroup ,grouptype,id ,MDUpdate);

        nobj=metadata_getnobj("omsobj:Person?@Id contains '.'",n,uri);

        if nobj=0 then
            do;
                put '## No Persons available.';
            end;
        else
            do;
                /*#0*/
                put '## Persons available.';

                do while (nobj > 0); /*#1*/
                    rc=metadata_getattr(uri, "Name", Name);
                    put uri=;
                    put Name=;

                    if Name=&_user then  /* #2*/

                        do;
                            put '## Search grupos user.';
                            a=1;
                            grpassn=metadata_getnasn(uri,"IdentityGroups",a,groupuri);

                            if grpassn in (-3,-4) then
                                do;
                                    group="No groups";
                                    output;
                                end;
                            else
                                do ;/*#3*/
                                    do while (grpassn > 0);
                                        _rc=metadata_getattr(groupuri, "Name", group);
                                        _rc=metadata_getattr(groupuri, "Desc", desgroup);
                                        _rc=metadata_getattr(groupuri,"GroupType",grouptype);
                                        a+1;
                                        output;
                                        grpassn=metadata_getnasn(uri,"IdentityGroups",a,groupuri);
                                        put groupuri=;
                                    end;
                                end; /*#3*/
                        end; /*#2*/

                        n+1;
                        nobj=metadata_getnobj("omsobj:Person?@Id contains '.'",n,uri);
                end; /*#1*/
            end;/*#0*/

        keep  name group desgroup grouptype;
    run;

    data _null_;
        set users_list_temp;

        if  group eq 'BEADM' then
            do;
                /*Se excluye los Roles y BD Potsgres*/
                call symput('role_' , group);
            end;
    run;
%put ----------------> &role_;
%mend get_meta_groups;

%macro VerLogs();
%let where =;

%if %length(&FECHALOGS_MAX) ne 0  and %length(&FECHALOGS_MIN) ne 0 %then
    %do;
        %let where =where datepart(LOG_DATETIME) between "&FECHALOGS_MIN"d and  "&FECHALOGS_MAX"d;
    %end;
%ELSE %IF %length(&FECHALOGS_MAX) ne 0  and %length(&FECHALOGS_MIN) EQ 0 %then
    %do;
        %let where= %str(where datepart(LOG_DATETIME)  = "&FECHALOGS_MAX"d );
    %END;
%ELSE %IF %length(&FECHALOGS_MAX) eq 0  and %length(&FECHALOGS_MIN) NE  0 %then
    %do;
        %let where= %str(where datepart(LOG_DATETIME)  = "&FECHALOGS_MIN"d );
    %END;

%if %length(&UsuarioLogs) and "&UsuarioLogs" ne "undefined"  %then
    %do;
        %if %length(&where) ne 0 %then
            %do;
                %let where= %str(&where and LOG_USUARIO = "&UsuarioLogs" );
            %end;
        %else
            %do;
                %let where= %str(where  LOG_USUARIO = "&UsuarioLogs" );
            %end;
    %end;

%if %length(&GRP_CODIGO) and "&GRP_CODIGO" ne "undefined" %then
    %do;
        %if %length(&where) ne 0 %then
            %do;
                %let where= %str(&where and t1.GRP_CODIGO = "&GRP_CODIGO" );
            %end;
        %else
            %do;
                %let where= %str(where  t1.GRP_CODIGO = "&GRP_CODIGO" );
            %end;
    %end;
proc sql;
create table RESULT as select t2.GRP_NOMBRE , t1.*
from BESASGC.BE_LOG_EVENTO t1 
left join BESASGC.BE_GRUPO_CONTROL t2 on(t1.GRP_CODIGO eq t2.GRP_CODIGO)
&where;
quit;

proc sql noprint; 
select count(*) into :totalLog from RESULT;
quit;
%if &totalLog eq 0 %then %do;
 %MESSAGEBE("No hay registros");
%end;
%mend;
%macro validoSchema(json=);
    %let wpath = %sysfunc(pathname(work));
    %put &wpath;
    filename jsonFile "&wpath./estructura.json";
    data _null_;
        file jsonFile;
        put &json;
    run;
    filename mytmp pipe "cat &wpath./estructura.json | python -m json.tool | grep 'Expecting object:'";
    data _null_;
      length buffer $200;
      infile mytmp dlm="¬";
      input buffer;
      call symput('ErrorEsquema' ,  buffer);
    run;
   

%mend;

%macro validateGroup(username, groupname);
%MDUEXTR(libref=work);
proc sql noprint;
select count(t2.Name) into :grpexist
from person t1 
left join GROUPMEMPERSONS_INFO t2 on (t1.keyid eq  t2.memId)
where t1.name=&username. and t2.Name=&groupname.;
quit;
%put &grpexist;
%mend;

%macro cargaEstrucutra(_programa=);
    /*creo tabla de parametros*/
    %if %sysfunc(exist(CFGJSON.fields)) %then
        %do;
            %if %sysfunc(exist(CFGJSON.fields)) %then
                %do;
                    proc sql;
                        create table parametrosTemp as
                            select "&_programa" as GRP_CODIGO, 
                                upcase(name) as ATR_NOMBRE , 
                                upcase(type) as ATR_VALOR,
                                0 as ATR_PARAM
                            from CFGJSON.fields
                                where name ne 'parametros'
                                    union 
                                select "&_programa" as GRP_CODIGO, 
                                    upcase(name) as ATR_NOMBRE , 
                                    upcase(type) as ATR_VALOR,
                                    1 as ATR_PARAM
                                from CFGJSON.ELEMENTTYPE_FIELDS
                                    where name ne 'parametros';
                    quit;

                %end;
            %else
                %do;

                    proc sql;
                        create table parametrosTemp as
                            select "&_programa" as GRP_CODIGO, 
                                upcase(name) as ATR_NOMBRE , 
                                upcase(type) as ATR_VALOR,
                                0 as ATR_PARAM
                            from CFGJSON.fields where name ne 'name';
                    quit;

                %end;
        %end;
    %else
        %do;
            %put error al cargar el archivo json;

            %return;
        %end;

    %if %sysfunc(exist(parametrosTemp)) %then
        %do;
            /*homologo tipos de datos*/
            PROC SQL;
                delete from BESASGC.BE_GRUPO_ATRIBUTO where GRP_CODIGO =  "&_programa";
                CREATE TABLE parametros AS 
                    SELECT T1.GRP_CODIGO ,
                        T1.ATR_NOMBRE,
                        (
                    CASE 
                        WHEN T2.SAS_DATA_TYPE NE '' THEN T2.SAS_DATA_TYPE
                        ELSE T3.SAS_DATA_TYPE
                    END
                            )
                        AS ATR_VALOR ,
                        ATR_PARAM
                            FROM parametrosTemp T1 
                                LEFT JOIN DICCIONARIOSAS T2 ON (T2.CampoOrigen  EQ T1.ATR_VALOR AND T2.Motor = 'IMPALA')
                                LEFT JOIN DICCIONARIOSAS T3 ON (T3.CampoOrigen  EQ T1.ATR_VALOR AND T3.Motor = 'HIVE')
                ;

            QUIT;
            proc sql;
                    insert into BESASGC.BE_GRUPO_ATRIBUTO  (GRP_CODIGO, ATR_NOMBRE , ATR_VALOR , ATR_PARAM) select GRP_CODIGO, ATR_NOMBRE , ATR_VALOR , ATR_PARAM from parametros;
                drop table parametrosTemp;
                drop table parametros;
            quit;

            libname CFGJSON clear;
        %end;
    %else
        %do;
            %put error al cargar el archivo json;

            %return;
        %end;

    /**/
%mend;
%macro InsertEvent(GRP_CODIGO,LOG_EVENTO,LOG_USUARIO,LOG_TIPO_EVENTO);
data _null_;
    p_fecha=datetime();
    call symputx('fecha_proc',p_fecha);
run;

proc sql noprint;
insert into BESASGC.BE_LOG_EVENTO (
GRP_CODIGO,
LOG_EVENTO,
LOG_DATETIME,
LOG_USUARIO,
LOG_TIPO_EVENTO
)
values(
&GRP_CODIGO,
&LOG_EVENTO,
&fecha_proc,
&LOG_USUARIO,
&LOG_TIPO_EVENTO
);
quit;
%mend;

%macro increasesVersion(GRP_CODIGO=);

proc sql noprint;
select (GRP_VERSION + 0.01) into :N_GRP_VERSION  from BESASGC.BE_GRUPO_CONTROL where GRP_CODIGO ="&GRP_CODIGO" ;
quit;
proc sql;
update  BESASGC.BE_GRUPO_CONTROL  set GRP_VERSION=&N_GRP_VERSION where GRP_CODIGO ="&GRP_CODIGO";
quit;
%mend;
%macro increasesVersionValida(GRP_CODIGO=);
%local V_GRP_VERSION;
proc sql noprint;
select t2.descripcion , t1.GRP_ESTADO, GRP_VERSION   into :VLD_DIRECTORIO trimmed , :VLD_ESTADO trimmed , :V_GRP_VERSION 
from BESASGC.BE_GRUPO_CONTROL t1 
left join Boleta_Config t2 on ( t1.GRP_PERIOCIDAD eq  input(t2.value, 10.) and t2.name='GRP_PERIOCIDAD')
where GRP_CODIGO="&GRP_CODIGO";
quit;
%put &VLD_DIRECTORIO &VLD_ESTADO &V_GRP_VERSION;
proc sql;
insert into BESASGC.BE_VALIDA_GRUPO (
GRP_CODIGO,
VLD_FILENAME,
VLD_DIRECTORIO,
VLD_USER_CREADO,
VLD_ESTADO,
VLD_VERSION
)
values(
"&GRP_CODIGO",
"",
"&VLD_DIRECTORIO",
"&_METAPERSON",
&VLD_ESTADO.,
&V_GRP_VERSION.
);
quit;
%mend;
%macro MueveArchivo(pathOrigen=,pathdestino=,GRP_CODIGO=);
%let mueve=ok;
%put mv /sasdatad/apps/be/nominas/scheduler/&pathdestino./version/%nrquote(*)grpctl_01.sas  /sasdatad/apps/be/nominas/scheduler/&pathOrigen./version/;
%if %sysfunc(fileexist("/sasdatad/apps/be/nominas/programs/&pathdestino./&GRP_CODIGO..sas")) or 
    %sysfunc(fileexist("/sasdatad/apps/be/nominas/scheduler/&pathdestino./&GRP_CODIGO..sas")) 
        %then %do;
    /*cambio los programas del usuario*/
        %sysexec %str(mv /sasdatad/apps/be/nominas/programs/&pathdestino./&GRP_CODIGO..sas  /sasdatad/apps/be/nominas/programs/&pathOrigen./);
    /*cambio los programas del scheduler*/
        %sysexec %str(mv /sasdatad/apps/be/nominas/scheduler/&pathdestino./&GRP_CODIGO..sas  /sasdatad/apps/be/nominas/scheduler/&pathOrigen./);
    /*cambio las versiones del programa*/
        %sysexec %str(mv /sasdatad/apps/be/nominas/scheduler/&pathdestino./version/&GRP_CODIGO.%nrquote(*).sas  /sasdatad/apps/be/nominas/scheduler/&pathOrigen./version/);
    %let mueve=ok;
%end;
%else %Do;
    %let mueve=nook;
%End;
%mend;
%macro NewRecord;
    
    %if %length(&GRP_ESQUEMA_VALIDO.) ne 0 %then %do;
        proc contents data=BESASGC.BE_GRUPO_CONTROL out=variables noprint; run;
        data _null_ ;
            set variables (where=(NAME='GRP_ESQUEMA_VALIDO'));
            CALL SYMPUT("LARGO_ESQUEMA", LENGTH);
        run;
        PROC SQL NOPRINT; 
            SELECT COUNT(*) INTO :GRP_NOMBRE_EXIST FROM BESASGC.BE_GRUPO_CONTROL WHERE GRP_NOMBRE="&GRP_NOMBRE";
            DROP TABLE variables;
        QUIT;
            /*se vambia a distinto de 0 ya que en el futuro se debe cargar desde un archivo json */
        %IF %length(&GRP_ESQUEMA_VALIDO.) NE  0 %THEN %DO;
            %IF &GRP_NOMBRE_EXIST EQ 0 %THEN %DO ;
                %validoSchema(json="&GRP_ESQUEMA_VALIDO");
                %if %length(&ErrorEsquema) eq 0 %then %do;
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
                %end;
                %else %do;
                    %MESSAGEBE("El esquema esta incorrecto!");
                    %SalidaWeb(Tabla=RESULT);
                %end;
            %END;
            %ELSE %DO;
                    %MESSAGEBE("El nombre &GRP_NOMBRE ya existe!");
                       %SalidaWeb(Tabla=RESULT);
            %END;
            
        %END;
        %ELSE %DO;
            %MESSAGEBE("El esquema es mayor a &LARGO_ESQUEMA  debe quitar los espacio o acortar el esquema!");
            %SalidaWeb(Tabla=RESULT);
        %END;

       
    %end;      

    %if %sysfunc(exist(RESULT)) %then %do;
        %put  --->;
    %end; 
    %else %do;
        %ViewRecord(tabla=BE_GRUPO_CONTROL,reg=&GRP_CODIGO);
    %end;
%mend;
%macro comparoJson(GRP_ESQUEMA_VALIDO=,GRP_CODIGO=);

%let pwdpath = %sysfunc(pathname(work));
    data _null_;
        file "&pwdpath/json1.json";
        json = &GRP_ESQUEMA_VALIDO;
        put json;
        file print;
    run;

    data _null_;
        file "&pwdpath/json2.json";
        set BESASGC.BE_GRUPO_CONTROL (where=(GRP_CODIGO="&GRP_CODIGO"));
        put GRP_ESQUEMA_VALIDO;
        file print;
    run;

    x "cat &pwdpath/json1.json | python -m json.tool >  &pwdpath/jsonCompare1.json";
    x "cat &pwdpath/json2.json | python -m json.tool >  &pwdpath/jsonCompare2.json";

    filename mytmp pipe "diff &pwdpath/jsonCompare1.json &pwdpath/jsonCompare2.json | wc -l";

    data _null_;
        length buffer $200.;
        infile mytmp dlm="¬";
        input buffer;
        call symput('ESQUEMA_VALIDO_CHANGE',compress(input(buffer,10.)));
    run;

%mend;
%macro UpdateRecord;
%put actualizo registro;

%put -----------> %length(&GRP_VIGENCIA_INICIO);

data _null_;
    p_fecha=datetime();
    call symputx('fecha_proc',p_fecha);
run;

%let change=0;
%if %length(&GRP_ESQUEMA_VALIDO.) ne 0 %then
    %do;


        proc contents data=BESASGC.BE_GRUPO_CONTROL out=variables noprint;
        run;

        data _null_;
            set variables (where=(NAME='GRP_ESQUEMA_VALIDO'));
            CALL SYMPUT("LARGO_ESQUEMA", LENGTH);
        run;

        PROC SQL;
            DROP TABLE variables;
        QUIT;

        %IF %length(&GRP_ESQUEMA_VALIDO.) NE 0 %THEN
            %DO;
                %let ESQUEMA_VALIDO_CHANGE=0;
                     %put [&GRP_ESQUEMA_VALIDO];
                %comparoJson(GRP_ESQUEMA_VALIDO="&GRP_ESQUEMA_VALIDO",GRP_CODIGO=&GRP_CODIGO);
                      %put ESQUEMA_VALIDO_CHANGE:[&ESQUEMA_VALIDO_CHANGE];
                %if &ESQUEMA_VALIDO_CHANGE ne 0 %then %do;
                %let change=1;
                    %validoSchema(json="&GRP_ESQUEMA_VALIDO");
                            %put ErrorEsquema:[&ErrorEsquema];
                    %if %length(&ErrorEsquema) eq 0 %then
                        %do;
                                       %let change=1;
                            libname CFGJSON JSON  fileref =jsonFile automap=replace;    
    
                            %cargaEstrucutra(_programa=&GRP_CODIGO);
                             %increasesVersion(GRP_CODIGO=&GRP_CODIGO);
                             %increasesVersionValida(GRP_CODIGO=&GRP_CODIGO);
                            proc sql noprint;
                                update BESASGC.BE_GRUPO_CONTROL set GRP_ESQUEMA_VALIDO = "&GRP_ESQUEMA_VALIDO",
                                    GRP_DATE_MODIFICADO = &fecha_proc ,
                                    GRP_USER_MODIFICADO = "&_METAPERSON"
                                where GRP_CODIGO = "&GRP_CODIGO";
                            quit;
                        %InsertEvent(GRP_CODIGO="&GRP_CODIGO",
                                    LOG_EVENTO="Esquema actualizado versión &N_GRP_VERSION.",
                                    LOG_USUARIO="&_METAPERSON",
                                    LOG_TIPO_EVENTO="004");
                        %end;
                        %else %do;
                                   %MESSAGEBE("El esquema esta incorrecto!");
                                    %SalidaWeb(Tabla=RESULT);
                         %end;
                %end;
            %END;
        %ELSE
            %DO;
                %MESSAGEBE("El esquema mayor a  &LARGO_ESQUEMA debe quitar los espacio o acortar el esquema!");
                %SalidaWeb(Tabla=RESULT);
            %END;
    %end;

%if %length(&GRP_PERIOCIDAD.) ne 0 %then
    %do;
        %let GRP_PERIOCIDAD_CHANGE=0;
        data _null_;
            set BESASGC.BE_GRUPO_CONTROL (where=(GRP_CODIGO="&GRP_CODIGO"));
            length periocidadO $30
                   periocidadD $30;
            periodin="&GRP_PERIOCIDAD";
            if periodin eq 0 then do;
                periocidadO = 'No definida';
            end;
            else if periodin eq 1 then do ;
                periocidadO = 'diaria';
            end;
            else if periodin eq 2 then do;
                periocidadO = 'semanal';
            end;
            else if periodin eq 3 then do;
                periocidadO = 'mensual';
            end;
            if GRP_PERIOCIDAD eq 0 then do;
                periocidadD = 'No definida';
            end;
            else if GRP_PERIOCIDAD eq 1 then do ;
                periocidadD = 'diaria';
            end;
            else if GRP_PERIOCIDAD eq 2 then do;
                periocidadD = 'semanal';
            end;
            else if GRP_PERIOCIDAD eq 3 then do;
                periocidadD = 'mensual';
            end;
            if periodin ne GRP_PERIOCIDAD then
                do;
                    call symput('GRP_PERIOCIDAD_CHANGE' , 1 );
                    call symput('GRP_PER_ORIGEN' ,  periocidadO);
                    call symput('GRP_PER_DESTINO' ,  periocidadD);
                end;
        run;

        %if &GRP_PERIOCIDAD_CHANGE EQ 1 %then %do;
        %let change=1;
            proc sql noprint;
                update BESASGC.BE_GRUPO_CONTROL set GRP_PERIOCIDAD = &GRP_PERIOCIDAD. , 
                    GRP_DATE_MODIFICADO = &fecha_proc ,
                    GRP_USER_MODIFICADO = "&_METAPERSON"
                where GRP_CODIGO = "&GRP_CODIGO";
            quit;
            %MueveArchivo(pathOrigen=&GRP_PER_ORIGEN,pathdestino=&GRP_PER_DESTINO,GRP_CODIGO=&GRP_CODIGO);

            %if "&mueve" eq "ok" %then %do;
                %let mensaje ="Periodo Actualizado se mueve el arhivo a la ruta &GRP_PER_DESTINO";
            %end;
            %else %Do;
                %let mensaje ="Periodo Actualizado, el codigo &GRP_CODIGO no se encontró en la ruta &GRP_PER_ORIGEN";
            %end;
            %InsertEvent(GRP_CODIGO="&GRP_CODIGO",
            LOG_EVENTO=&mensaje,
            LOG_USUARIO="&_METAPERSON",
            LOG_TIPO_EVENTO="004");


        %end;
    %end;

%if %length(&GRP_ESTADO.) ne 0 %then
    %do;
        %let ESTADO_CHANGE=0;
        data _null_;
            set BESASGC.BE_GRUPO_CONTROL (where=(GRP_CODIGO="&GRP_CODIGO"));
            periodoin="&GRP_ESTADO";

            if periodoin ne GRP_ESTADO then
                do;
                    call symput('ESTADO_CHANGE' , 1 );
                end;
        run;
        %put ESTADO_CHANGE &ESTADO_CHANGE;
        %IF &ESTADO_CHANGE EQ 1 %THEN %DO;
            %let change=1;
            proc sql noprint;
                update BESASGC.BE_GRUPO_CONTROL set GRP_ESTADO = &GRP_ESTADO., 
                    GRP_DATE_MODIFICADO = &fecha_proc ,
                    GRP_USER_MODIFICADO = "&_METAPERSON"
                where GRP_CODIGO = "&GRP_CODIGO";
            quit;
            %if &GRP_ESTADO. eq 0 %then %do;
                %let estado_str = desactivado;
            %end;
            %else %do;
                %let estado_str = activado ;
            %end;
            %InsertEvent(GRP_CODIGO="&GRP_CODIGO",
            LOG_EVENTO="Estado Actualizado a &estado_str.",
            LOG_USUARIO="&_METAPERSON",
            LOG_TIPO_EVENTO="004");
        %END;

    %end;
%let ESTADO_CHANGE=0;
        data _null_;
            set BESASGC.BE_GRUPO_CONTROL (where=(GRP_CODIGO="&GRP_CODIGO"));
            periodoin="&GRP_NOMBRE";

            if periodoin ne GRP_NOMBRE then
                do;
                    call symput('ESTADO_CHANGE' , 1 );
                end;
        run;
        %put ESTADO_CHANGE &ESTADO_CHANGE;
        %IF &ESTADO_CHANGE EQ 1 %THEN %DO;
            %let change=1;
            proc sql noprint;
                update BESASGC.BE_GRUPO_CONTROL set GRP_NOMBRE = "&GRP_NOMBRE.", 
                    GRP_DATE_MODIFICADO = &fecha_proc ,
                    GRP_USER_MODIFICADO = "&_METAPERSON"
                where GRP_CODIGO = "&GRP_CODIGO";
            quit;
            %InsertEvent(GRP_CODIGO="&GRP_CODIGO",
            LOG_EVENTO="Nombre Actualizado ",
            LOG_USUARIO="&_METAPERSON",
            LOG_TIPO_EVENTO="004");
        %END;

        %let ESTADO_CHANGE=0;
        data _null_;
            set BESASGC.BE_GRUPO_CONTROL (where=(GRP_CODIGO="&GRP_CODIGO"));
            periodoin="&GRP_DESCRIPCION";

            if periodoin ne GRP_DESCRIPCION then
                do;
                    call symput('ESTADO_CHANGE' , 1 );
                end;
        run;
        %put ESTADO_CHANGE &ESTADO_CHANGE;
        %IF &ESTADO_CHANGE EQ 1 %THEN %DO;
            %let change=1;
            proc sql noprint;
                update BESASGC.BE_GRUPO_CONTROL set GRP_DESCRIPCION = "&GRP_DESCRIPCION.", 
                    GRP_DATE_MODIFICADO = &fecha_proc ,
                    GRP_USER_MODIFICADO = "&_METAPERSON"
                where GRP_CODIGO = "&GRP_CODIGO";
            quit;
            %InsertEvent(GRP_CODIGO="&GRP_CODIGO",
            LOG_EVENTO="Descripción Actualizada ",
            LOG_USUARIO="&_METAPERSON",
            LOG_TIPO_EVENTO="004");
        %END;



        %let ESTADO_CHANGE=0;
        data _null_;
            set BESASGC.BE_GRUPO_CONTROL (where=(GRP_CODIGO="&GRP_CODIGO"));
            periodoin="&GRP_AREA_NEGOCIO";

            if periodoin ne GRP_AREA_NEGOCIO then
                do;
                    call symput('ESTADO_CHANGE' , 1 );
                end;
        run;
        %put ESTADO_CHANGE &ESTADO_CHANGE;
        %IF &ESTADO_CHANGE EQ 1 %THEN %DO;
            %let change=1;
            proc sql noprint;
                update BESASGC.BE_GRUPO_CONTROL set GRP_AREA_NEGOCIO = &GRP_AREA_NEGOCIO., 
                    GRP_DATE_MODIFICADO = &fecha_proc ,
                    GRP_USER_MODIFICADO = "&_METAPERSON"
                where GRP_CODIGO = "&GRP_CODIGO";
            quit;
            %InsertEvent(GRP_CODIGO="&GRP_CODIGO",
            LOG_EVENTO="Área de negocio Actualizado ",
            LOG_USUARIO="&_METAPERSON",
            LOG_TIPO_EVENTO="004");
        %END;


        %let ESTADO_CHANGE=0;
        data _null_;
            set BESASGC.BE_GRUPO_CONTROL (where=(GRP_CODIGO="&GRP_CODIGO"));
            periodoin=input("&GRP_VIGENCIA_INICIO  0:00:00", datetime20.);

            if periodoin ne GRP_VIGENCIA_INICIO then
                do;
                    call symput('ESTADO_CHANGE' , 1 );
                end;
        run;
        %put ESTADO_CHANGE &ESTADO_CHANGE;
        %IF &ESTADO_CHANGE EQ 1 %THEN %DO;
            %let change=1;
            
            proc sql noprint;
                update BESASGC.BE_GRUPO_CONTROL set GRP_VIGENCIA_INICIO = input("&GRP_VIGENCIA_INICIO  0:00:00", datetime20.), 
                    GRP_DATE_MODIFICADO = &fecha_proc ,
                    GRP_USER_MODIFICADO = "&_METAPERSON"
                where GRP_CODIGO = "&GRP_CODIGO";
            quit;
            %InsertEvent(GRP_CODIGO="&GRP_CODIGO",
            LOG_EVENTO="Vigencia de Inicio Actualizado",
            LOG_USUARIO="&_METAPERSON",
            LOG_TIPO_EVENTO="004");
        %END;
        %let ESTADO_CHANGE=0;
        data _null_;
            set BESASGC.BE_GRUPO_CONTROL (where=(GRP_CODIGO="&GRP_CODIGO"));
            periodoin=input("&GRP_VIGENCIA_FIN  0:00:00", datetime20.);;

            if periodoin ne GRP_VIGENCIA_FIN then
                do;
                    call symput('ESTADO_CHANGE' , 1 );
                end;
        run;
        %put ESTADO_CHANGE &ESTADO_CHANGE;
        %IF &ESTADO_CHANGE EQ 1 %THEN %DO;
            %let change=1;
            proc sql noprint;
                update BESASGC.BE_GRUPO_CONTROL set GRP_VIGENCIA_FIN = input("&GRP_VIGENCIA_FIN  0:00:00", datetime20.), 
                    GRP_DATE_MODIFICADO = &fecha_proc ,
                    GRP_USER_MODIFICADO = "&_METAPERSON"
                where GRP_CODIGO = "&GRP_CODIGO";
            quit;
            %InsertEvent(GRP_CODIGO="&GRP_CODIGO",
            LOG_EVENTO="Vigencia fin Actualizado",
            LOG_USUARIO="&_METAPERSON",
            LOG_TIPO_EVENTO="004");
        %END;

%if %length(&GRP_HABILITADO.) ne 0 %then
    %do;
       %let ESTADO_CHANGE=0;
        data _null_;
            set BESASGC.BE_GRUPO_CONTROL (where=(GRP_CODIGO="&GRP_CODIGO"));
            GRP_HABILITADO_=&GRP_HABILITADO.;
            if GRP_HABILITADO ne GRP_HABILITADO_ then
                do;
                    call symput('ESTADO_CHANGE' , 1 );
                end;
        run;
        %IF &ESTADO_CHANGE EQ 1 %THEN %DO;
            %let change=1;
            proc sql noprint;
                update BESASGC.BE_GRUPO_CONTROL set GRP_HABILITADO = &GRP_HABILITADO., 
                    GRP_DATE_MODIFICADO = &fecha_proc ,
                    GRP_USER_MODIFICADO = "&_METAPERSON"
                where GRP_CODIGO = "&GRP_CODIGO";
            quit;
            %if &GRP_HABILITADO. eq 0 %then %do;
                %let estado_str = Desactivado;
            %end;
            %else %do;
                %let estado_str = Activado ;
            %end;
            %InsertEvent(GRP_CODIGO="&GRP_CODIGO",
            LOG_EVENTO="Estado Actualizado a &estado_str",
            LOG_USUARIO="&_METAPERSON",
            LOG_TIPO_EVENTO="004");
        %end;
%end;

%IF &change EQ 1 %THEN %DO;
    
    %ViewRecord(tabla=BE_GRUPO_CONTROL,reg=&GRP_CODIGO);
%END;
%ELSE %DO;
    %MESSAGEBE("No hay cambios realizados");
    %SalidaWeb(Tabla=RESULT);
%END;

 

%mend;
%macro ViewRecord(tabla=, reg=);
%put muesto los registros;
%if %length(&reg) ne 0 %then %do;
proc sql ;
create table response_TEMP as 
    select distinct t1.* , put (max(t2.PROC_DATE_PROCESO), datetime16.) as PROC_DATE_PROCESO , t2.PROC_CANT_REGISTROS 
    from BESASGC.&tabla. t1 
    left join BESASGC.BE_CONTROL_PROCESO t2 on (t1.GRP_CODIGO eq t2.GRP_CODIGO)
where t1.GRP_CODIGO="&reg" 
group by t1.GRP_CODIGO;
quit;
%end;
%else %do;
DATA response_TEMP;
SET BESASGC.&tabla.;
RUN;
%end;


DATA response (RENAME=(TXT_HABILITADO=GRP_HABILITADO TXT_PERIOCIDAD=GRP_PERIOCIDAD txt_VERSION=GRP_VERSION ));
SET response_TEMP;
format GRP_VIGENCIA_FIN ddmmyy10. ;
format grp_vigencia_inicio ddmmyy10.;
FORMAT GRP_DATE_CREADO NLDATMAP32. ;
FORMAT GRP_DATE_MODIFICADO NLDATMAP32. ;
length TXT_PERIOCIDAD $32;
length TXT_HABILITADO $32;
grp_vigencia_inicio = datepart(grp_vigencia_inicio); 
GRP_VIGENCIA_FIN = datepart(GRP_VIGENCIA_FIN); 
GRP_ESQUEMA_VALIDO = "";
if GRP_HABILITADO eq 1 then do;
    TXT_HABILITADO = "Habilitado";
end;
else if GRP_HABILITADO eq 0 then do;
    TXT_HABILITADO = "Deshabilitado";
end;

if GRP_PERIOCIDAD eq 0 then do;
    TXT_PERIOCIDAD = "No definida";
end;
else if GRP_PERIOCIDAD eq 1  then do;
    TXT_PERIOCIDAD = "Diaria";
end;
else if GRP_PERIOCIDAD eq 2  then do;
    TXT_PERIOCIDAD = "Semanal";
end;
else if GRP_PERIOCIDAD eq 3  then do;
    TXT_PERIOCIDAD = "Mensual";
end;
else if GRP_PERIOCIDAD eq 4  then do;
    TXT_PERIOCIDAD = "Otra";
end;
txt_VERSION = put(GRP_VERSION,5.2);
drop GRP_HABILITADO;
drop GRP_PERIOCIDAD;
drop GRP_VERSION;
RUN;

proc sql noprint;
select count (*) into :countresponse from response;
quit;
%if &countresponse eq 0 %then %do;
    %MESSAGEBE("No hay segmentos creados");
    %SalidaWeb(Tabla=RESULT);
%end;
%else %do;
    %SalidaWeb(Tabla=response);
%end;

%mend;
%macro ViewRecordLog(tabla=);
%put muestro los registros  del log ;
proc sql ;
create table response as 
    select * 
    from BESASGC.&tabla. order by LOG_UID;
quit;
%SalidaWeb(Tabla=response);
%mend;
%macro ViewRecordLogTmp(tabla=);
%put muestro los registros  del log ;
proc sql ;
create table response as 
    select * 
    from &tabla. order by LOG_UID;
quit;
%SalidaWeb(Tabla=response);
%mend;
%macro DeleteRecord;
    proc sql;
        delete from BESASGC.BE_LOG_EVENTO where GRP_CODIGO = compress("&GRP_CODIGO"); 
        delete from BESASGC.BE_CONTROL_PROCESO where GRP_CODIGO = compress("&GRP_CODIGO");
        delete from BESASGC.BE_VALIDA_GRUPO where GRP_CODIGO = compress("&GRP_CODIGO"); 
        delete from BESASGC.BE_GRUPO_ATRIBUTO where GRP_CODIGO = compress("&GRP_CODIGO"); 
        delete from BESASGC.BE_GRUPO_CONTROL where GRP_CODIGO = compress("&GRP_CODIGO");
    quit;
    %ViewRecord(tabla=BE_GRUPO_CONTROL,reg=);
%mend;
/*tabla con mensaje SalidaWeb*/
%macro MESSAGEBE(e);

    data RESULT;
        array MESSAGE_{7} $1000 _TEMPORARY_ (&e.);
        drop n;

        do n = 1 to 1;
            MENSAJE = MESSAGE_{n};
            output;
        end;

        KEEP MENSAJE ESTADO;
    run;

%mend;

%macro SalidaWeb(Tabla=);
/*Envió el resultado por json*/
    %if "&output" eq "json" %then %do;
       proc sql noprint;
            select count(*) into :vcount from WORK.&Tabla. ;
        quit;
        %put ------------->&vcount;
        %if &vcount ne 0 %then %do;
            filename json_m temp encoding='utf-8';
                proc json out=json_m pretty nosastags NOFMTCHARACTER NOSCAN ;
                    write open object;
                    write values "respuesta";
                    write open array;
                    export WORK.&Tabla.;
                    write close;
                    write close;
                run;
    
                data _null_;
                    infile json_m;
                    file _webout;
                    input;
                    put _infile_;
                run;
        %end;
    %end;
    %else %if "&output" eq "Tabla" %then %do;
        %STPBEGIN;
        proc print data=&tabla; run;
        %STPEND;
    %end;
%mend;

%macro UpdateCode ;
LIBNAME BLTCOD BASE "/sasdatad/apps/be/nominas/data";
proc sql ;
DELETE FROM BLTCOD.CODIGOS;
INSERT INTO BLTCOD.CODIGOS (GRP_CODIGO) SELECT GRP_CODIGO FROM BESASGC.BE_GRUPO_CONTROL;
quit;
%mend;
%MACRO GRP_CODIGOS();
PROC SQL;
CREATE TABLE RESULT  AS SELECT GRP_CODIGO FROM BESASGC.BE_GRUPO_CONTROL;
QUIT;
%MEND;

%macro VerLogsError();
%LOCAL TOTALESEGE;
filename mypipe pipe "ls -1 /sasdatad/apps/be/nominas/programs/semanal/*.sas /sasdatad/apps/be/nominas/programs/mensual/*sas /sasdatad/apps/be/nominas/programs/diario/*sas 2>/dev/null | xargs -I {} basename {} ";
data segmentosFail;
infile mypipe;
    length salida_bash $300;
    input salida_bash ;
    salida_bash = tranwrd(upcase(salida_bash),'.SAS','');
run;
filename mypipe clear;


PROC SQL NOPRINT;
SELECT COUNT (*) INTO :TOTALESEGE FROM segmentosFail ;
QUIT;

%IF %LENGTH(&TOTALESEGE) NE 0 %THEN %DO;
proc sql;
create table RESULT as select t2.GRP_NOMBRE , t1.*
from BESASGC.BE_LOG_EVENTO t1 
left join BESASGC.BE_GRUPO_CONTROL t2 on(t1.GRP_CODIGO eq t2.GRP_CODIGO)
WHERE T1.GRP_CODIGO IN (SELECT T4.salida_bash FROM segmentosFail T4  );
quit;
%END;
%ELSE %DO;
 %MESSAGEBE("No se pudo cargar el log");
%END;
%mend;
%macro main(GRP_CODIGO=);


%if "&ACTION" EQ "NewRecord" %THEN %DO;
    %IF %LENGTH(&GRP_CODIGO) NE 0 %THEN %DO;
        proc sql noprint;
        select count(*) into :CBE_GRUPO_CONTROL from BESASGC.BE_GRUPO_CONTROL where GRP_CODIGO="&GRP_CODIGO";
        quit;
        %if &CBE_GRUPO_CONTROL eq 0 %then %do;
            %NewRecord;
            %UpdateCode;
        %end;
        %else %do;
            %MESSAGEBE("El código &GRP_CODIGO ya existe!");
            %SalidaWeb(Tabla=RESULT);
        %end;

    %END;
    %ELSE %DO;
        %MESSAGEBE("Debe ingresar un código de segmento ");
        %SalidaWeb(Tabla=RESULT);
    %END;

%END;
%ELSE %IF "&ACTION" EQ "UpdateRecord" %THEN %DO;
    %IF %LENGTH(&GRP_CODIGO) NE 0 %THEN %DO;
        proc sql noprint;
        select count(*) into :CBE_GRUPO_CONTROL from BESASGC.BE_GRUPO_CONTROL where GRP_CODIGO="&GRP_CODIGO";
        quit;
        %if &CBE_GRUPO_CONTROL ne 0 %then %do;
            %UpdateRecord;

        %end;
        %else %do;
            %MESSAGEBE("El código &GRP_CODIGO No existe!");
            %SalidaWeb(Tabla=RESULT);
        %end;
    %END;
    %ELSE %DO;
        %MESSAGEBE("Debe ingresar un código de segmento ");
        %SalidaWeb(Tabla=RESULT);
    %END;

%END;
%ELSE %IF "&ACTION" EQ "UpdateCode" %THEN %DO;
    %UpdateCode;
    %MESSAGEBE("Codigos actualizados");
    %SalidaWeb(Tabla=RESULT);

%END;
%ELSE %IF "&ACTION" EQ "DeleteRecord" %THEN  %DO;
    %IF %LENGTH(&GRP_CODIGO) NE 0 %THEN %DO;
                %let mensaje = "El código &GRP_CODIGO ha sido eliminado";
            %InsertEvent(GRP_CODIGO="&GRP_CODIGO",
            LOG_EVENTO=&mensaje,
            LOG_USUARIO="&_METAPERSON",
            LOG_TIPO_EVENTO="005");
             %DeleteRecord;   
    %END;
    %ELSE %DO;
        %MESSAGEBE("Debe ingresar un código de segmento ");
        %SalidaWeb(Tabla=RESULT);
    %END;
%END;
%ELSE %IF "&ACTION" EQ "ViewRecord" %THEN  %DO;
     %if %length(&GRP_CODIGO) ne 0 %then %do;
        %let mensaje = "El código &GRP_CODIGO ha sido consultado";
            %InsertEvent(GRP_CODIGO="&GRP_CODIGO",
            LOG_EVENTO=&mensaje,
            LOG_USUARIO="&_METAPERSON",
            LOG_TIPO_EVENTO="001");
     %end;

    %ViewRecord(tabla=BE_GRUPO_CONTROL,reg=&GRP_CODIGO);
%END;
%ELSE %IF "&ACTION" EQ "Start" %THEN  %DO;
    %include "/sasdatad/apps/be/nominas/deploy/valida_programa.sas";
    proc sql noprint;
        select count(*) into :log from BESASGC.BE_LOG_EVENTO where LOG_TIPO_EVENTO = "007";
         select count(*) into :logTotal from BE_LOG_EVENTO;
    quit;
    %put log:&log;
      %put logTotal:&logTotal;
    %if &log eq 0 %then %do;
         %MESSAGEBE("No se encontraron archivos a procesar.");
         %SalidaWeb(Tabla=RESULT);
    %end;
    %else %do; 
        %if &logTotal eq 0 %then %do; 
            %MESSAGEBE("No se encontraron archivos a procesar.");
            %SalidaWeb(Tabla=RESULT);
            %end;
        %else %do;
            %ViewRecordLogTmp(tabla=BE_LOG_EVENTO);
        %end;
    %end;

%END;
%ELSE %IF "&ACTION" EQ "VerLogs" %THEN  %DO;
    %VerLogs();
    %SalidaWeb(Tabla=RESULT);
%END;
%ELSE %IF "&ACTION" EQ "VerLogsError" %THEN  %DO;
    %VerLogsError();
    %SalidaWeb(Tabla=RESULT);
%END;
%ELSE %IF "&ACTION" EQ "GRP_CODIGOS" %THEN  %DO;
    %GRP_CODIGOS();
     proc sql noprint;
        select count (*) into :totalcode from RESULT ;
     quit;
     %if &totalcode eq 0 %then %do;
            %MESSAGEBE("No hay segmentos creados.");
     %end;
    %SalidaWeb(Tabla=RESULT);
%END;
%ELSE %IF "&ACTION" EQ "Login" %THEN  %DO;
    %get_meta_groups(_user=&p_user);
    %get_user(_user="&_METAUSER",_tabla=&p_tabla,role_=&role_ );
%END;
%ELSE %IF "&ACTION" EQ "GetEsquema" %THEN  %DO;
    %IF %LENGTH(&GRP_CODIGO) NE 0 %THEN %DO;
             %GetEsquema;   
    %END;
    %ELSE %DO;
        %MESSAGEBE("Debe ingresar un código de segmento ");
        %SalidaWeb(Tabla=RESULT);
    %END;
%END;
%mend;
%macro GetEsquema;
%let pwdpath = %sysfunc(pathname(work));

data _null_;
set BESASGC.BE_GRUPO_CONTROL (where=(GRP_CODIGO="&GRP_CODIGO."));
file "&pwdpath/temporal.json";
put GRP_ESQUEMA_VALIDO;
run;

x "cat &pwdpath/temporal.json | python -m json.tool > &pwdpath/setting.json";

DATA _NULL_;
            INFILE "&pwdpath/setting.json";
            FILE _WEBOUT;
            INPUT;
            PUT _INFILE_;
RUN;


%mend;
%macro noaccess;

    data _NULL_;
        file _webout;

        put "<html><body> 
                <h1>Sin acceso..</h1>
                 <p><b>&_METAPERSON</b>, Usted no tiene permiso para ver este contenido.</p>
                   
        </body></html>";
        
    run;
%mend;
%macro validaGrip;
%let groupname="BEADM";
%validateGroup(username="&_METAPERSON", groupname=&groupname);
%if &grpexist ne  0 %then %do;
	%setMetaperson;
    %include "/sasdatad/apps/be/nominas/utils/libnames.sas";
    %main(GRP_CODIGO=&GRP_CODIGO);
%end;
%else %do;
    %noaccess;
%end;
%mend;
%validaGrip;