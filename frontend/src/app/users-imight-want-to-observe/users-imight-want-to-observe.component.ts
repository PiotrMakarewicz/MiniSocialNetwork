import { Component, OnInit } from '@angular/core';
import { LoginService } from '../login.service';
import { backendAddress } from '../global-variables';

@Component({
  selector: 'app-users-imight-want-to-observe',
  templateUrl: './users-imight-want-to-observe.component.html',
  styleUrls: ['./users-imight-want-to-observe.component.css']
})
export class UsersIMightWantToObserveComponent implements OnInit {

  users: any[] = [];
  constructor(private loginService: LoginService) { }

  async ngOnInit() {
    const userid = this.loginService.getUserId();
    const response = await fetch(backendAddress+userid+'/recommended-users');
    const json = await response.json();
    this.users = json['observed']
  }

}
