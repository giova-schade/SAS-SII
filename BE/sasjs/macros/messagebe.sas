/**tabla con mensaje SalidaWeb*/
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

%mend MESSAGEBE;