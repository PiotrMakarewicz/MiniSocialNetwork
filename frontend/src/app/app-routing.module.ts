import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UserPageComponent } from './user-page/user-page.component';
import { MainPageComponent} from './main-page/main-page.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { LoginGuardService } from './login-guard.service';

const routes: Routes = [
  { path: 'user/:id', component: UserPageComponent, canActivate: [LoginGuardService]},
  { path: 'main', component: MainPageComponent, canActivate: [LoginGuardService]},
  { path: 'login', component: LoginPageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
