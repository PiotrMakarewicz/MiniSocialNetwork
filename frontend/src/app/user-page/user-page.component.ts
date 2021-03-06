import { Component, OnDestroy, OnInit, Output } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { UserService } from '../user.service';
import { backendAddress } from '../global-variables';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-user-page',
  templateUrl: './user-page.component.html',
  styleUrls: ['./user-page.component.css'],
  providers: [ UserService]
})
export class UserPageComponent implements OnInit, OnDestroy {
  @Output() id: any;
  private sub: any;
  @Output() imageUrl: any;
  @Output() name: any;
  @Output() description: any;
  @Output() user: any;
  observeLink: any;
  unobserveLink: any;
  @Output() observed: boolean = false;
  @Output() posts: any;
  params: any;
  @Output() isNotLoggedInUser: any = false;

  constructor(private route: ActivatedRoute, private userService: UserService, private loginService: LoginService) { }

  ngOnInit() {
    this.sub = this.route.params.subscribe(async params => {
      this.params = params;
       await this.update();
    });
  }

  ngOnDestroy() {
    this.sub.unsubscribe();
  }


  async update(){
    this.id = + this.params['id'];
    this.user = await this.userService.getUser(this.id);
    this.id = this.user['id'];
    this.imageUrl = this.user['avatar'];
    this.description = this.user['description'];
    this.name = this.user['name'];
    this.observeLink = backendAddress + this.loginService.getUserId() + "/observe/" + this.id;
    this.unobserveLink = backendAddress + this.loginService.getUserId() + "/observe/" + this.id;
    this.posts = (await (await fetch(backendAddress+this.id+'/posts')).json())['posts'];
    let observed_users = (await (await fetch(backendAddress+this.loginService.getUserId()+'/observed')).json())['observed'];
    this.observed = false;
    this.isNotLoggedInUser = !(this.id == this.loginService.getUserId());
    for (let user of observed_users){
      if (user['id'] == this.id){
        this.observed = true; break;
      }
    } 
  }


  async observe() {
    let result = await fetch(this.observeLink);

    console.log('observe');
    await this.update();
  }
  async unobserve() {
    let result = await fetch(this.unobserveLink);
    console.log('unobserve');
    await this.update();
  }

}
