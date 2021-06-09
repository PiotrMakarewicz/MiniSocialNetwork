import { Component, OnInit } from '@angular/core';
import { LoginService } from '../login.service';
import { backendAddress} from '../global-variables';
@Component({
  selector: 'app-influential-users',
  templateUrl: './influential-users.component.html',
  styleUrls: ['./influential-users.component.css']
})
export class InfluentialUsersComponent implements OnInit {

  users: any[] = [];
  constructor(private loginService: LoginService) { }

  async ngOnInit() {
    const userid = this.loginService.getUserId();
    const response = await fetch(backendAddress+'ranking');
    const json = await response.json();
    console.log(json)
    this.users = json['ranking']
  }

}
