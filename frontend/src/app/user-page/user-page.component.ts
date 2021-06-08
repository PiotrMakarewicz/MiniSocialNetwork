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
  private id: any;
  private sub: any;
  private imageUrl: any;
  private name: any;
  private description: any;
  @Output() private user: any;

  constructor(private route: ActivatedRoute, private userService: UserService) { }

  ngOnInit() {
    this.sub = this.route.params.subscribe(async params => {
       this.id = +params['id'];
       this.user = await this.userService.getUser(this.id);
    });
  }

  ngOnDestroy() {
    this.sub.unsubscribe();
  }

}
