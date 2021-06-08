import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UserPageComponent } from './user-page/user-page.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { LoginService } from './login.service'
import { TagPageComponent } from './tag-page/tag-page.component';
import { CreatePostComponent } from './create-post/create-post.component';

const routes: Routes = [
  // { path: 'user/:id', component: UserPageComponent, canActivate: [LoginService]},
  // { path: 'login', component: LoginPageComponent},
  // { path: 'tag/:tagname', component: TagPageComponent, canActivate: [LoginService]}
  { path: 'user/:id', component: UserPageComponent},
  { path: 'login', component: LoginPageComponent},
  { path: 'tag/:tagname', component: TagPageComponent},
  { path: 'user/:id/create-post', component: CreatePostComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
