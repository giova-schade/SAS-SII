import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { BrowserModule } from "@angular/platform-browser";
import { Routes, RouterModule } from "@angular/router";
import { AdminLayoutComponent } from "./layouts/admin-layout/admin-layout.component";
import { AuthGuard } from './route-routing.guards';
import { AuthService } from './services/auth.services';
import { MaestrosService } from './services/maestro.service';
import { Role } from './models/role';
import { AccessDenied } from "./layouts/access-denied/access-denied.component";
const routes: Routes = [

  {
    path: "",
    component: AdminLayoutComponent,
    canLoad: [AuthGuard],
    canActivate: [AuthGuard],
    data: {
      roles: [
        Role.BEADM,
      ]
    },
    children: [
      {
        path: "BEADM",
        loadChildren: () => import("./layouts/admin-layout/admin-layout.module").then(m => m.AdminLayoutModule)

      }
    ]
  },
  {
    path: "",
    component: AccessDenied,
    children: [
      {
        path: "access-denied",
        loadChildren: () => import("./layouts/access-denied/access-denied.module").then(m => m.AccessDeniedLayoutModule)

      }
    ]
  }

];

@NgModule({
  imports: [
    CommonModule,
    BrowserModule,
    RouterModule.forRoot(routes, {
      useHash: true
    })
  ],
  exports: [RouterModule],
  providers: [
    AuthGuard,
    AuthService,
    MaestrosService
  ]
})
export class AppRoutingModule { }