import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UserPageComponent } from './user-page/user-page.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { LoginService } from './login.service'

const routes: Routes = [
  { path: 'user/:id', component: UserPageComponent, canActivate: [LoginService]},
  { path: 'login', component: LoginPageComponent},
  { path: '**', redirectTo: 'login'}
  //   { path: 'user/:id', component: UserPageComponent},
  // { path: 'login', component: LoginPageComponent},
  // { path: '**', redirectTo: 'login'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
