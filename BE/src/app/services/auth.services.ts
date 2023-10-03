import { Injectable } from '@angular/core';
import { User } from '../models/user';
import { Role, BEADM } from '../models/role';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CONFIG } from '../../environments/global.component';
import { MenuItem } from 'primeng/api';
import { UrlSerializer } from '@angular/router';
import SASjs, { SASjsConfig } from '@sasjs/adapter';



export const alllinks: MenuItem[] = [
    
    {
        label: 'Procesos de boleta electrónica',
        icon: '',
        items: [
            {
                routerLink: "/",
                label: "Inicio",
                icon: "pi pi-home"
            },
            {
                routerLink: "createSegment",
                label: "Crear segmento",
                icon: "pi pi-file"
            },
            {
                routerLink: "updateSegment",
                label: "Actualizar segmento",
                icon: "pi pi-pencil"
            },                        
            {
                routerLink: "viewSegment",
                label: "Ver Segmentos",
                icon: "pi pi-search-plus"
            },
            {
                routerLink: "viewLogs",
                label: "Ver Logs",
                icon: "pi pi-search"
            },
            {
                routerLink: "runValidator",
                label: "Ejecutar validador",
                icon: "pi pi-play"
            }
        ]
    }
];
export const links: MenuItem[] = []

export interface Area {
    AREA: string
}
export interface StartupData {
    SYSDATE: string
    SYSTIME: string
    areas: Area[]
    login: boolean
    MF_GETUSER: string
}

@Injectable()

export class AuthService {
    private user: User = new User;
    private adapter: SASjs

    constructor(private http: HttpClient) {
        this.adapter = new SASjs(window.sasjsConfigInput)
    }
    isAuthorized() {
        return !!this.user;
    }

    hasRole(role: Role) {
        return this.isAuthorized() && this.user.role === role;
    }

    existe(role:string , roles: any){
        for (let rol in roles){
            if (rol == role){
                return true;
            }
        }
        return false;
    }

    login(role: Role, name: any, info: any) {
        this.user = { role: role, name: name, info: info };
    }
    GetuserInfo() {
        return this.user;
    }
    GetUserOptions(role: any) {
        alllinks.forEach((link) => {
            this.pushlink(role, link);
        })
        return links;
    }

    getStartupData(url: string, data?: any, config?: SASjsConfig): any {
        // host and path (app loc) are automatically added
        // by adapter based on configuration in the index.html
        url = 'services/' + url

        return new Promise((resolve, reject) => {
            this.adapter
            .request(url, data, config, () => {
              //Needs log in in callback
            })
            .then(
              (res: StartupData) => {
                if (res.login === false) {
                  //not logged in
                }
    
                this.user.name = res.MF_GETUSER

                resolve(res)
              },
              (err: any) => {
                reject(err)
              }
            )
        })
    }

    getUser(): Observable<any> {
        return this.http.get(CONFIG.apiUrlLogin);
    }

    pushlink(role: string, link: any) {
        if (role == "BEADM") {            
            let roleConfig = BEADM;   

            if (this.ValidaUrl(link, roleConfig)) {
                link.routerLink=role+'/'+link.routerLink;
                links.push(link);
                
            }
            let subrl = this.PushSuburl(link,roleConfig,role); 
            if(subrl.hasOwnProperty('items')){   
                if(subrl.items.length){
                 links.push(subrl);                    
                }              
            };
        }


    }
    PushSuburl(link: any, roleConfig : any, role : string){
        var  suburl = [];
        if (link.hasOwnProperty('items')){
            for ( let subitem in link.items ){
                if(link.items[subitem].routerLink.indexOf('/') > 0){
                    for(let sub in roleConfig){
                        if (sub == link.items[subitem].routerLink.split('/')[1] && roleConfig[sub] == 'Yes'  ){
                            link.items[subitem].routerLink=role+'/'+link.items[subitem].routerLink;
                            suburl.push(link.items[subitem]);
                        }
                    }
                }else{
                    for(let sub in roleConfig){
                        if (sub == link.items[subitem].routerLink && roleConfig[sub] == 'Yes'  ){
                            link.items[subitem].routerLink=role+'/'+link.items[subitem].routerLink;
                            suburl.push(link.items[subitem]);
                        }
                    }
                }
            }
            link.items=suburl;
        }

        return link;
    }
    ValidaUrl(pagina: any, paginas: any) {
        for (let valor in paginas) {
            if (valor == pagina.routerLink && paginas[valor] == 'Yes') {
                return true;
            }
        }

        return false;
    }


}
