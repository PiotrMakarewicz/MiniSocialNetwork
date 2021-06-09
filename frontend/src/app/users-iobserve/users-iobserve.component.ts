import { Component, OnInit } from '@angular/core';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-users-iobserve',
  templateUrl: './users-iobserve.component.html',
  styleUrls: ['./users-iobserve.component.css']
})
export class UsersIObserveComponent implements OnInit {

  constructor(private loginService: LoginService) { }

  ngOnInit(): void {

  }

}
