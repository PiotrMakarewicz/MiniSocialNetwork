import { Injectable } from '@angular/core';
import { MD5 } from './md5'
import { backendAddress} from './global-variables'
import { CanActivate, Router } from '@angular/router';

@Injectable(
  {providedIn: 'root'}
)
export class LoginService implements CanActivate {

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
      this.router.navigate(['/user/'+ this.userId])
    }
    else{
      alert("Failed to sign in.");
      this.loggedIn = false;
    }
    localStorage.setItem('loggedIn', String(this.loggedIn));
    localStorage.setItem('userName', String(this.userName));
    localStorage.setItem('userId', String(this.userId));
    localStorage.setItem('passwordHash', String(this.passwordHash));
    return Boolean(json['id'])
  }

  canActivate() {
    this.loggedIn = Boolean(localStorage.getItem('loggedIn') == "true");
    this.userName = String(localStorage.getItem('userName'))
    this.passwordHash = String(localStorage.getItem('passwordHash'));
    this.userId = Number(localStorage.getItem('userId'))

    let loggedIn = this.isLoggedIn()
    console.log("Trying to activate. logged in? ", loggedIn)
    if (!loggedIn){
      this.router.navigate(['/login']);
      return false;
    }
    else return true;
  }

  getUserId(){
    return this.userId;
  }

  isLoggedIn() {
    return this.loggedIn;
  }
}
