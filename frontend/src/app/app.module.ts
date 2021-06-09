import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { LoginPageComponent } from './login-page/login-page.component';
import { PostComponent } from './post/post.component';
import { UserSmallComponent } from './user-small/user-small.component';
import { UserPageComponent } from './user-page/user-page.component';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { TagPageComponent } from './tag-page/tag-page.component';
import { UsersIObserveComponent } from './users-iobserve/users-iobserve.component';
import { MyProfileComponent } from './my-profile/my-profile.component';
import { UsersIMightWantToObserveComponent } from './users-imight-want-to-observe/users-imight-want-to-observe.component';
import { InfluentialUsersComponent } from './influential-users/influential-users.component';
import { PostsILikeComponent } from './posts-ilike/posts-ilike.component';
import { PostsIDislikeComponent } from './posts-idislike/posts-idislike.component';
import { LatestPostsComponent } from './latest-posts/latest-posts.component';
import { PostsInterestingComponent } from './posts-interesting/posts-interesting.component';


@NgModule({
  declarations: [
    AppComponent,
    LoginPageComponent,
    PostComponent,
    UserSmallComponent,
    UserPageComponent,
    TagPageComponent,
    UsersIObserveComponent,
    MyProfileComponent,
    UsersIMightWantToObserveComponent,
    InfluentialUsersComponent,
    PostsILikeComponent,
    PostsIDislikeComponent,
    LatestPostsComponent,
    PostsInterestingComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
