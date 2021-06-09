import { Component, OnDestroy, OnInit, Output, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { UserService } from '../user.service';
import { backendAddress } from '../global-variables';
import { LoginService } from '../login.service';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-create-post',
  templateUrl: './create-post.component.html',
  styleUrls: ['./create-post.component.css']
})
export class CreatePostComponent implements OnInit, OnDestroy {
  @Input() postID: any;

  contentControl = new FormControl('');
  photoControl = new FormControl('');
  tagControl = new FormControl('');
  sub:any;
  params: any;

  ngOnInit(): void {
    this.sub = this.route.params.subscribe(async params => {
      this.params = params;
       
    });
  }
  ngOnDestroy() {
    this.sub.unsubscribe();
  }

  async respondToPost(postFrom: any) {
    console.log('respond-post');
    let address = backendAddress + "post/" + postFrom + "/respond/" + this.postID;
    let response = await fetch(address);
    let json = await response.json();
    console.log(json);
  }

  async addPost(content: string, photoAddress: string, tag: string) {
    console.log('create-post');
    let user = this.loginService.getUserId();
    let address = backendAddress + "user/" + user + "/add/" + content + "/" + photoAddress;
    if (tag) {
      address = address + "/" + tag;
    }
    let response = await fetch(address);
    let json = await response.json();
    let postFrom = json[0]['id'];
    console.log(json);
    if (this.postID) {
      this.respondToPost(postFrom);
    }
  }

  constructor(private route: ActivatedRoute, private userService: UserService, private loginService: LoginService) { }



  async onClick() {
    let content = this.contentControl.value;
    let photo = this.photoControl.value;
    let tag = this.tagControl.value;
    await this.addPost(content, photo, tag);
  }

}
