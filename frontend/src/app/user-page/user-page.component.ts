import { Component, OnDestroy, OnInit, Output } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { UserListComponent } from '../user-list/user-list.component';
import { UserService } from '../user.service';

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

  constructor(private route: ActivatedRoute, private userService: UserService) { }

  ngOnInit() {
    this.sub = this.route.params.subscribe(async params => {
       this.id = + params['id'];
       this.user = await this.userService.getUser(this.id);
       console.log(this.user);
       this.id = this.user['id'];
       this.imageUrl = this.user['avatar'];
       this.description = this.user['description'];
       this.name = this.user['name'];
    });
  }

  ngOnDestroy() {
    this.sub.unsubscribe();
  }

}
