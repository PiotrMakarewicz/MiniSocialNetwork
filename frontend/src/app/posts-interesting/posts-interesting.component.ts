import { Component, OnInit, Output } from '@angular/core';
import { backendAddress } from '../global-variables';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-posts-interesting',
  templateUrl: './posts-interesting.component.html',
  styleUrls: ['./posts-interesting.component.css']
})
export class PostsInterestingComponent implements OnInit {
  constructor(private loginService: LoginService) { }
  @Output() posts: any = [];

  async ngOnInit() {
    let userid = this.loginService.getUserId();
    this.posts = (await (await fetch(backendAddress+'')).json())['posts'];
  }

}
