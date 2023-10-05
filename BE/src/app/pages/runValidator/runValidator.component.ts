import { Component, OnInit, ViewChild } from "@angular/core";
import { NotificationsComponent } from './../../pages/notifications/notifications.component';
import { MaestrosService } from '../../services/maestro.service';
import { UntypedFormBuilder } from "@angular/forms";
import { ActivatedRoute } from "@angular/router";
import { Table } from "primeng/table";

@Component({
  selector: "app-runValidator",
  templateUrl: "runValidator.component.html",
  styleUrls: ["runValidator.component.scss"]
})
export class runValidatorComponent implements OnInit {
  datasourceLogs: any;
  LogsCampos: any;
  totalRecordsLogs: number;
  Logsview: boolean;
  multiSortSegmento: any;
  loading!: boolean;
  loadingPage:boolean;
  @ViewChild('Logs') Logs: any;
  constructor(
    private notify: NotificationsComponent,
    private formBuilder: UntypedFormBuilder,
    private master: MaestrosService,
    private route: ActivatedRoute
  ) {
    this.loadingPage=false;
    this.LogsCampos = [];
    this.totalRecordsLogs = 0;
    this.Logsview = false;
    this.multiSortSegmento = [];
  }

  ngOnInit() {

  }

  applyFilterGlobalLogst($event: any, stringVal: any){
    this.Logs.filterGlobal($event.target.value, 'contains');

  }

  runSegmentos(){
    this.loadingPage=true;

    this.master.getRun().subscribe({
      next:(result) => {
        this.datasourceLogs = result.respuesta;
        this.totalRecordsLogs = this.datasourceLogs.length;

        if (this.totalRecordsLogs) {
          for (let campo in this.datasourceLogs[0]) {
            this.LogsCampos.push({ field: campo, header: campo });
            if (campo == 'LOG_DATETIME') {
              this.multiSortSegmento.push({ field: 'LOG_DATETIME', order: -1 });
            }
          }

        }
        this.loading = false;
        this.Logsview = true;
        this.loadingPage=false;

      
      },
      error: (e) => {

        this.master.getLogsError().subscribe({
          next:(el:any) =>{
            this.datasourceLogs = el.respuesta;
            this.totalRecordsLogs = this.datasourceLogs.length;
    
            if (this.totalRecordsLogs) {
              for (let campo in this.datasourceLogs[0]) {
                this.LogsCampos.push({ field: campo, header: campo });
                if (campo == 'LOG_DATETIME') {
                  this.multiSortSegmento.push({ field: 'LOG_DATETIME', order: -1 });
                }
              }
    
            }
            this.loading = false;
            this.Logsview = true;
            this.loadingPage=false;
          },
          error: (el) => {
            this.notify.showNotification('top', 'right', 4, 'Error al obtener el registo de logs');
            this.loadingPage=false;
          }
        })




      },
      complete:() =>{

      }
    })
  }
  clear(table: Table) {
    table.clear();
  }

}
