import { Component, Input, OnInit, Output } from '@angular/core';
import { backendAddress } from '../global-variables'
import { LoginService } from '../login.service';
import { UserService } from '../user.service';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {

  @Input() id: any;
  @Output() authorName: any = 0;
  @Output() authorID: any = 0;
  @Output() authorPhotoUrl: any = "";
  @Output() content: any = ""
  @Output() rating: any = 0;
  @Output() photoUrl: any = "";

  constructor(private userService: UserService, private loginService: LoginService) { }

  async getPost() {
    if (this.id) {
      const result = await fetch(backendAddress + 'post/409');
      const json = await result.json();
      return json['posts'][0]
    }
  }

  async ngOnInit() {
    await this.update();
    
  }

  async update() {
    let post = await this.getPost();
    this.authorID = post['author']
    this.content = post['content']
    this.rating = post['rating']
    let user = await this.userService.getUser(post['author']) 
    
    this.authorName = user['name'];
  }

  async like() {
    let user = await this.loginService.getUserId();
    await fetch(backendAddress + ''+user+'/dislike/'+this.id)
  }
  dislike() {

  }

}
