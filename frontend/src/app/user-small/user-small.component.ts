import { Component, OnInit, Input, Output } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { backendAddress } from '../global-variables';

@Component({
  selector: 'app-user-small',
  templateUrl: './user-small.component.html',
  styleUrls: ['./user-small.component.css']
})
export class UserSmallComponent implements OnInit {

  @Input() id: any;
  private user: any;
  name: any;
  imageUrl: any;
  address: any;


  constructor() { }

  async getUser() {
    if (this.id) {
      const result = await fetch(backendAddress + this.id);
      const json = await result.json();
      this.user = json['users'][0];
      this.name = this.user['name'];
      this.imageUrl = this.user['imageUrl'];
      this.address = 'user/' + this.id;
      return json['users'][0]
    }
  }

  ngOnInit() {
    this.getUser();
  }

}
