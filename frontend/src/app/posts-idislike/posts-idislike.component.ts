import { Component, OnInit, Output } from '@angular/core';
import { backendAddress } from '../global-variables';
import { LoginService } from '../login.service';


@Component({
  selector: 'app-posts-idislike',
  templateUrl: './posts-idislike.component.html',
  styleUrls: ['./posts-idislike.component.css']
})
export class PostsIDislikeComponent implements OnInit {

  constructor(private loginService: LoginService) { }
  @Output() posts: any = [];

  async ngOnInit() {
    let userid = this.loginService.getUserId();
    this.posts = (await (await fetch(backendAddress+userid+'/disliked')).json())['posts'];
  }

}