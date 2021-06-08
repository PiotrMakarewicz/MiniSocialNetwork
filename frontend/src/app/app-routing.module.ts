import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UserPageComponent } from './user-page/user-page.component';
import { MainPageComponent} from './main-page/main-page.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { LoginService } from './login.service'

const routes: Routes = [
  // { path: 'user/:id', component: UserPageComponent, canActivate: [LoginService]},
  // { path: '', component: MainPageComponent, canActivate: [LoginService]},
  // { path: 'login', component: LoginPageComponent},
  // { path: '**', redirectTo: ''}
    { path: 'user/:id', component: UserPageComponent},
  { path: '', component: MainPageComponent},
  { path: 'login', component: LoginPageComponent},
  { path: '**', redirectTo: ''}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
