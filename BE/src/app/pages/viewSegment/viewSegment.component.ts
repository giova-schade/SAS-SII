import { Component, OnInit, ViewChild } from "@angular/core";
import { NotificationsComponent } from './../../pages/notifications/notifications.component';
import { MaestrosService } from '../../services/maestro.service';
import { LazyLoadEvent } from 'primeng/api';
import { PrimeNGConfig } from 'primeng/api';
import { Table } from "primeng/table";
import { TableModule } from 'primeng/table';
import { FormControl, Validators, FormGroup, FormBuilder } from '@angular/forms';
import { ConfirmationService } from 'primeng/api';
import { Message } from 'primeng/api';
@Component({
  selector: "app-viewSegment",
  templateUrl: "viewSegment.component.html",
  styleUrls: ["viewSegment.component.scss"],
  providers: [NotificationsComponent, ConfirmationService]
})
export class viewSegmentComponent implements OnInit {


  datasourceSegmentos: any;
  TituloDialog: string;
  displayBasic: boolean;
  SegCampos: any;
  totalRecordsSeg: number;
  Segview: boolean;
  multiSortSegmento: any;
  msgs: Message[] = [];
  position!: string;
  loadingPage: boolean;
  GRP_CODIGO_URL!: string;
  GRP_ESQUEMA_VALIDO!: any;
  columnas!: any;
  @ViewChild('segmentos') segmentos: any;

  segmentoForm = new FormGroup({
    GRP_CODIGO: new FormControl('', Validators.required),
    GRP_ESQUEMA_VALIDO: new FormControl('', Validators.required),
    GRP_PERIOCIDAD: new FormControl('', Validators.required),
    GRP_NOMBRE: new FormControl('', Validators.required),
    GRP_DESCRIPCION: new FormControl('', Validators.required),
    GRP_HABILITADO: new FormControl('', Validators.required),
    GRP_AREA_NEGOCIO: new FormControl('', Validators.required),
    GRP_VIGENCIA_INICIO: new FormControl(''),
    GRP_VIGENCIA_FIN: new FormControl(''),
  });
  loading!: boolean;
  constructor(
    private notify: NotificationsComponent,
    private master: MaestrosService,
    private primengConfig: PrimeNGConfig,
    private confirmationService: ConfirmationService
  ) {
    this.loadingPage = false;
    this.SegCampos = [];
    this.totalRecordsSeg = 0;
    this.Segview = false;
    this.multiSortSegmento = [];
    this.displayBasic = false;
    this.TituloDialog = '';
    this.columnas = [];
  }

  ngOnInit() {
    this.loadingPage = true;

    this.master.getSegmentos().subscribe({
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

          this.datasourceSegmentos = result.respuesta;
          this.totalRecordsSeg = this.datasourceSegmentos.length;

          if (this.totalRecordsSeg) {
            for (let campo in this.datasourceSegmentos[0]) {

              this.SegCampos.push({ field: campo, header: campo });
              if (campo == 'GRP_CODIGO') {
                this.multiSortSegmento.push({ field: 'GRP_CODIGO', order: -1 });
              }
            }

            this.SegCampos.push({ field: '', header: '' });
            this.SegCampos.forEach( (data:any , ) => { 
              if(data.field != ''){
              this.columnas.push(data.field)
            }
             })
            console.log(this.columnas)

          }
          this.loading = false;
          this.Segview = true;
        }
        this.loadingPage = false;

      },
      error: (e) => {
        this.notify.showNotification('top', 'right', 4, 'Error al cargar los segmentos');
        this.loadingPage = false;

      },
      complete: () => {


      }

    })

    this.primengConfig.ripple = true;
  }
  clear(table: Table) {
    table.clear();
  }
  applyFilterGlobalSegment($event: any, stringVal: any) {
    this.segmentos.filterGlobal($event.target.value, 'contains');
  }

  deleteSegmento(segmento: any) {
    this.loadingPage = true;
    this.master.geRemoveSegmentos(segmento).subscribe({
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

          this.datasourceSegmentos = this.datasourceSegmentos.filter((x: any) => x.GRP_CODIGO != segmento.GRP_CODIGO);
          this.msgs = [{ severity: 'info', summary: 'Listo', detail: ' Segmento ' + segmento.GRP_CODIGO + ' Eliminado' }];
        }
        this.loadingPage = false;

      },
      error: (e) => {
        this.notify.showNotification('top', 'right', 4, 'Error al eliminar el segmento');
        this.loadingPage = false;

      },
      complete: () => {


      }
    })
  }
  remove(segmento: any) {
    console.log('segmento')
    console.log(segmento)
    this.position = 'bottomright';

    this.confirmationService.confirm({
      message: 'Se eliminara el segmento: ' + segmento.GRP_CODIGO,
      header: 'Eliminar segmento ',
      icon: 'pi pi-info-circle',
      accept: () => {
        this.deleteSegmento(segmento);

      },
      reject: () => {
        this.msgs = [{ severity: 'info', summary: 'Rejected', detail: 'You have rejected' }];
      },
      key: "positionDialog"
    });
  }
  cargoEsquema(codigo: string) {
    this.master.getEsquema(codigo).subscribe({
      next: (result) => {
        let warning = 0;
        let Mensaje = '';
        this.TituloDialog = codigo;
        this.GRP_ESQUEMA_VALIDO = JSON.stringify(result);
        this.displayBasic = true;
        this.loadingPage = false;
      },
      error: (e) => {
        console.error(e)
        this.notify.showNotification('top', 'right', 4, 'Error al obtener el esquema del segmento  ' + codigo);
        this.segmentoForm.reset();
        this.loadingPage = false;

      },
      complete: () => {


      }
    })
  }
  showDialogEsquema(evento: any) {
    this.loadingPage = true;
    this.cargoEsquema(evento['GRP_CODIGO']);

  }


}
