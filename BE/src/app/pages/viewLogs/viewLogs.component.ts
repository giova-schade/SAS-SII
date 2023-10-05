import { Component, OnInit, ViewChild } from "@angular/core";
import { Table } from "primeng/table";
import { NotificationsComponent } from './../../pages/notifications/notifications.component';
import { MaestrosService } from '../../services/maestro.service';
import { LazyLoadEvent } from 'primeng/api';
import { PrimeNGConfig } from 'primeng/api';
import { TableModule } from 'primeng/table';
import { UntypedFormControl, Validators, UntypedFormGroup, FormBuilder } from '@angular/forms';
import { ConfirmationService } from 'primeng/api';
import { Message } from 'primeng/api';
interface Codigos {
  name: string,
  code: number
}
@Component({
  selector: "app-viewLogs",
  templateUrl: "viewLogs.component.html",
  styleUrls: ["viewLogs.component.scss"],
  providers: [NotificationsComponent, ConfirmationService]

})


export class viewLogsComponent implements OnInit {

  datasourceLogs: any;
  LogsCampos: any;
  totalRecordsLogs: number;
  Logsview: boolean;
  multiSortSegmento: any;
  msgs: Message[] = [];
  position!: string;
  loading!: boolean;
  codigos!: Codigos[];
  loadingPage:boolean;
  @ViewChild('Logs') Logs: any;
  logsForm = new UntypedFormGroup({
    FECHALOGS_MIN: new UntypedFormControl(''),
    FECHALOGS_MAX: new UntypedFormControl(''),
    USUARIOLOGS: new UntypedFormControl(''),
    GRP_CODIGO: new UntypedFormControl('')
  });
  constructor(
    private notify: NotificationsComponent,
    private master: MaestrosService,
    private primengConfig: PrimeNGConfig,
    private confirmationService: ConfirmationService
  ) {
    this.loadingPage=false;
    this.LogsCampos = [];
    this.totalRecordsLogs = 0;
    this.Logsview = false;
    this.multiSortSegmento = [];
    this.codigos = [];
  }

  ngOnInit() {
    this.loadingPage=true;

    this.master.getlistSegmento().subscribe({
      next: (result) => {
        let warning = 0;
        let Mensaje = '';
        result.respuesta.forEach(function (dato: any) {
          if (dato.hasOwnProperty('MENSAJE')) {
            warning = 1;
            Mensaje = dato['MENSAJE'];
          }
        })

        if (warning == 1) {
          this.notify.showNotification('top', 'right', 3, Mensaje);
        } else {

          result['respuesta'].forEach((element: any) => {
            this.codigos.push({ name: element['GRP_CODIGO'], code: element['GRP_CODIGO'] })
          });
        }
      this.loadingPage=false;

      },
      error: (e) => {
        this.notify.showNotification('top', 'right', 4, 'Error al listar los datos');
      this.loadingPage=false;

      },
      complete: () => {


      }
    })

  }
  OnChange(event: any) {
  }

  Viewlog(form:any){    
    if (this.logsForm.controls['FECHALOGS_MIN'] != undefined && this.logsForm.controls['FECHALOGS_MIN'].value != null && this.logsForm.controls['FECHALOGS_MIN'].value != '' ){
      if(this.logsForm.controls['FECHALOGS_MAX'] != undefined && this.logsForm.controls['FECHALOGS_MAX'].value != null && this.logsForm.controls['FECHALOGS_MAX'].value != ''){
        if(this.logsForm.controls['FECHALOGS_MIN'].value > this.logsForm.controls['FECHALOGS_MAX'].value){
          this.notify.showNotification('top', 'right', 4, 'La fecha de inicio no puede ser mayor que la fecha de termino');
        }else{
          this.getLogs();
        }
      }else{
        this.getLogs();        
      }
    }else{
      this.getLogs();
    }


  }
  getLogs() {
    this.loadingPage=true;

    this.master.geLogs(this.logsForm).subscribe({
      next: (result) => {

        let warning = 0;
        let Mensaje = '';
        result.respuesta.forEach(function (dato: any) {
          if (dato.hasOwnProperty('MENSAJE')) {
            warning = 1;
            Mensaje = dato['MENSAJE'];
          }
        })

        if (warning == 1) {
          this.notify.showNotification('top', 'right', 3, Mensaje);
        } else {
          this.datasourceLogs = result.respuesta;
          this.totalRecordsLogs = this.datasourceLogs.length;

          if (this.totalRecordsLogs) {
            for (let campo in this.datasourceLogs[0]) {
              this.LogsCampos.push({ field: campo, header: campo });
              if (campo == 'LOG_UID') {
                this.multiSortSegmento.push({ field: 'LOG_UID', order: -1 });
              }
            }

          }
          this.loading = false;
          this.Logsview = true;
        }
        this.loadingPage=false;

      },
      error: (e) => {
        this.notify.showNotification('top', 'right', 4, 'Error al obtener los datos de logs');
        this.loadingPage=false;

      },
      complete: () => {


      }

    })

  }

  clear(table: Table) {
    table.clear();
  }

  applyFilterGlobalLogst($event: any, stringVal: any){
    this.Logs.filterGlobal($event.target.value, 'contains');

  }
}
