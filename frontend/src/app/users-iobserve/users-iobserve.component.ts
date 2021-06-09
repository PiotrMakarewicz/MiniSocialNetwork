import { Component, OnInit } from '@angular/core';
import { LoginService } from '../login.service';
import { backendAddress} from '../global-variables';

@Component({
  selector: 'app-users-iobserve',
  templateUrl: './users-iobserve.component.html',
  styleUrls: ['./users-iobserve.component.css']
})
export class UsersIObserveComponent implements OnInit {

  users: any[] = [];
  constructor(private loginService: LoginService) { }

  async ngOnInit() {
    const userid = this.loginService.getUserId();
    const response = await fetch(backendAddress+userid+'/observed');
    const json = await response.json();
    this.users = json['observed']
  }

}
