import { Component , OnInit} from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './services/auth.services';
import { NotificationsComponent } from './pages/notifications/notifications.component';
import { PrimeNGConfig } from 'primeng/api';
import { Role } from './models/role';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers : [NotificationsComponent]
})
export class AppComponent {
  title = 'SII';
  constructor(
             private router: Router,
             private authService: AuthService,
             private notify: NotificationsComponent,
             private primengConfig: PrimeNGConfig) { }
   
  ngOnInit() {
    this.primengConfig.ripple = true;
    
    this.authService.getUser().subscribe(
      result => {
        this.login(result.role,result.Nombre , result.info );
      },
      error => {
        this.notify.showNotification('top', 'right', 4, 'Error al obtener los datos del usuario  ')
      }

    )
  }
  

  login(role: any, name: string , info: any) {
    this.authService.login(role, name, info);

    if (!this.authService.isAuthorized()){
      this.router.navigate(['access-denied']);
    }else{
      const validRol = Role;
      const rol = this.authService['user'].role  as Role;
      console.log(validRol);
      console.log(rol);
      if (this.authService.existe(rol, validRol)){
        this.router.navigate(['/' + role]);
      }else{
        this.router.navigate(['access-denied']);
      }
      
    }

    
  }

}
