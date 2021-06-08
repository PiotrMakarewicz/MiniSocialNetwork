import { Injectable } from '@angular/core';
import { MD5 } from './md5'
import { backendAddress} from './global-variables'
import { Router } from '@angular/router';

@Injectable()
export class LoginService {

  loggedIn: boolean = false;
  userName: string = "";
  userId: any = null;
  passwordHash: string = "";

  constructor(private router: Router) { }

  async loginAs(userName: string, password: string){
    console.log(userName, MD5(password));
    let response = await fetch(backendAddress + 'password_check/' + userName + '/' + MD5(password))
    let json = await response.json();
    console.log(json);
    if (json['id']){
      this.loggedIn = true;
      this.userName = userName;
      this.userId = json['id'];
      this.passwordHash = MD5(password);
      alert("Logged in as " + this.userName + ".");
      return true;
    }
    else{
      alert("Failed to sign in.");
      return false;
    }
  }
  

  isLoggedIn() {

    return this.loggedIn;
  }
}
