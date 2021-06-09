import { Component, OnInit, Output } from '@angular/core';
import { backendAddress } from '../global-variables';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-latest-posts',
  templateUrl: './latest-posts.component.html',
  styleUrls: ['./latest-posts.component.css']
})
export class LatestPostsComponent implements OnInit {
  constructor(private loginService: LoginService) { }
  @Output() posts: any = [];

  async ngOnInit() {
    let userid = this.loginService.getUserId();
    this.posts = (await (await fetch(backendAddress+'last-posts')).json())['posts'];
  }

}
