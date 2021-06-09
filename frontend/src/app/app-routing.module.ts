import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UserPageComponent } from './user-page/user-page.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { LoginService } from './login.service'
import { TagPageComponent } from './tag-page/tag-page.component';
import { MyProfileComponent } from './my-profile/my-profile.component';
import { UsersIObserveComponent } from './users-iobserve/users-iobserve.component';
import { InfluentialUsersComponent } from './influential-users/influential-users.component';
import { PostsILikeComponent } from './posts-ilike/posts-ilike.component';
import { PostsIDislikeComponent } from './posts-idislike/posts-idislike.component';
import { LatestPostsComponent } from './latest-posts/latest-posts.component';
import { PostsInterestingComponent } from './posts-interesting/posts-interesting.component';
import { UsersIMightWantToObserveComponent } from './users-imight-want-to-observe/users-imight-want-to-observe.component';
import { CreatePostComponent } from './create-post/create-post.component';

const routes: Routes = [
  // { path: 'user/:id', component: UserPageComponent, canActivate: [LoginService]},
  // { path: 'login', component: LoginPageComponent},
  // { path: 'tag/:tagname', component: TagPageComponent, canActivate: [LoginService]}
  { path: 'user/:id', component: UserPageComponent, canActivate: [LoginService]},
  { path: 'login', component: LoginPageComponent},
  { path: 'tag/:tagname', component: TagPageComponent, canActivate: [LoginService]},
  { path: 'myprofile', component: MyProfileComponent, canActivate: [LoginService]},
  { path: 'users-iobserve', component: UsersIObserveComponent, canActivate: [LoginService]},
  { path: 'influential-users', component: InfluentialUsersComponent, canActivate: [LoginService]},
  { path: 'posts-ilike', component: PostsILikeComponent, canActivate: [LoginService]},
  { path: 'posts-idislike', component: PostsIDislikeComponent, canActivate: [LoginService]},
  { path: 'latest-posts', component: LatestPostsComponent, canActivate: [LoginService]},
  { path: 'posts-interesting', component: PostsInterestingComponent, canActivate: [LoginService]},
  { path: 'users-imight-want-to-observe', component: UsersIMightWantToObserveComponent, canActivate: [LoginService]},
  { path: 'tag/:tagname', component: TagPageComponent, canActivate: [LoginService]},
  { path: 'create-post', component: CreatePostComponent, canActivate: [LoginService]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
