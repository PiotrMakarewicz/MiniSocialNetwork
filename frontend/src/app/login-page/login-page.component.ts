import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { backendAddress } from '../global-variables';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css'],
  providers: [LoginService]
})
export class LoginPageComponent implements OnInit {

  userNameControl = new FormControl('');
  passwordControl = new FormControl('');

  constructor(private loginService: LoginService) { }

  ngOnInit() {
  }
  async onClick() {
    let userName = this.userNameControl.value;
    let password = this.passwordControl.value;
    await this.loginService.loginAs(userName, password);
  }
}
