import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { PostComponent } from './post/post.component';
import { UserPageComponent } from './user-page/user-page.component';
import { UserSmallComponent } from './user-small/user-small.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { PostListComponent } from './post-list/post-list.component';
import { UserListComponent } from './user-list/user-list.component';


@NgModule({
  declarations: [
    AppComponent,
    PostComponent,
    UserPageComponent,
    UserSmallComponent,
    LoginPageComponent,
    PostListComponent,
    UserListComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
