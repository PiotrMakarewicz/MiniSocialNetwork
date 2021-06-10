import { Component, Input, OnChanges, OnDestroy, OnInit, Output } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { backendAddress } from '../global-variables'
import { LoginService } from '../login.service';
import { UserService } from '../user.service';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit, OnChanges, OnDestroy {

  @Input() @Output() id: any;
  @Output() authorName: any = 0;
  @Output() authorID: any = 0;
  @Output() authorPhotoUrl: any = "";
  @Output() content: any = ""
  @Output() rating: any = 0;
  @Output() photoUrl: any = "";
  @Output() tags: any = [];
  @Output() responses: any = [];
  sub: any;

  constructor(private userService: UserService, private loginService: LoginService, private route: ActivatedRoute) { }

  async getPost() {
    if (this.id) {
      let result = await fetch(backendAddress + 'post/' + this.id);
      let json = await result.json();
      const post = json['posts'][0];
      result = await fetch(backendAddress + 'post/' + this.id + '/tags')
      json = await result.json();
      const tags = json['tags'];
      return {...post, tags: tags};
    }
  }

  async getResponses() {
    if (this.id) {
      let result = await fetch(backendAddress + 'post/' + this.id + '/responses');
      let json = await result.json();
      let posts = json['posts'];
      this.responses = [];
      for (let post of posts){
        this.responses.push(Number(post['id']));
      }
    }
  }

  async ngOnInit() {
    this.sub = this.route.params.subscribe(async params => {
       await this.update();
       await this.getResponses();
    });
    await this.update();
    await this.getResponses();
  }

  async ngOnChanges(){
    await this.update();
    await this.getResponses();
  }

  ngOnDestroy(){
    if (this.sub){
      this.sub.unsubscribe();
    }
  }

  async update() {
    let post = await this.getPost();
    console.log(post);
    console.log("postId: ", this.id);
    this.authorID = post['author']
    this.content = post['content']
    this.rating = post['rating']
    this.tags = post['tags']
    this.photoUrl = post['photo_address']
    let user = await this.userService.getUser(post['author'])

    this.authorName = user['name'];
  }

  async like() {
    let user = await this.loginService.getUserId();
    let result = await fetch(backendAddress +user+'/like/'+this.id);
    let json = await result.json();
    console.log(json);
    console.log('like')
    await this.update();
  }
  async dislike() {
    let user = await this.loginService.getUserId();
    let result = await fetch(backendAddress +user+'/dislike/'+this.id);
    let json = await result.json();
    console.log(json);
    console.log('dislike')
    await this.update();
  }

}
