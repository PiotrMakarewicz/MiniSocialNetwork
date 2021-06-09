import { Component, OnInit, Output } from '@angular/core';
import { backendAddress } from '../global-variables';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-posts-ilike',
  templateUrl: './posts-ilike.component.html',
  styleUrls: ['./posts-ilike.component.css']
})
export class PostsILikeComponent implements OnInit {

  constructor(private loginService: LoginService) { }
  @Output() posts: any = [];

  async ngOnInit() {
    let userid = this.loginService.getUserId();
    this.posts = (await (await fetch(backendAddress+userid+'/liked')).json())['posts'];
  }

}