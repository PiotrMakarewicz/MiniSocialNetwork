import { Component, OnDestroy, OnInit, Output } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { UserService } from '../user.service';

@Component({
  selector: 'app-user-page',
  templateUrl: './user-page.component.html',
  styleUrls: ['./user-page.component.css']
})
export class UserPageComponent implements OnInit {
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
       this.id = this.user['id'];
       this.imageUrl = this.user['avatar'];
       this.description = this.user['description'];
       this.name = this.user['name'];
    });
  }

  ngOnDestroy() {
    if (this.sub)
      this.sub.unsubscribe();
  }

}
