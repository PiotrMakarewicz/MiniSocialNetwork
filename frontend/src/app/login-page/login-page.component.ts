import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import { backendAddress } from '../global-variables';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {

  userNameControl = new FormControl('');
  passwordControl = new FormControl('');

  constructor(private loginService: LoginService, private router: Router) { }

  ngOnInit() {
  }
  async onClick() {
    let userName = this.userNameControl.value;
    let password = this.passwordControl.value;
    await this.loginService.loginAs(userName, password);
  }
}
