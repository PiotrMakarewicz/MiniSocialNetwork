import { Component, OnInit } from '@angular/core';
import { backendAddress } from '../global-variables';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }
  onClick() {
    alert(backendAddress);
  }
}
