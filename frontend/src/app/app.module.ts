import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { PostComponent } from './post/post.component';
import { UserPageComponent } from './user-page/user-page.component';
import { UserSmallComponent } from './user-small/user-small.component';


@NgModule({
  declarations: [
    AppComponent,
    PostComponent,
    UserPageComponent,
    UserSmallComponent
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
