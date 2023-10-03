/**
  @file
  @brief Init program
  @details This program runs at the start of every Job and service (if
  configured in the sasjs/sasjsconfig.json)

  <h4> SAS Macros </h4>
  @li mf_mkdir.sas

**/

%let libloc=/tmp/besasgc;

%mf_mkdir(&libloc)

libname besasgc "&libloc";

