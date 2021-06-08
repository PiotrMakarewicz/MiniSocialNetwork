import { Injectable } from '@angular/core';
import { CanActivate } from '@angular/router'
import { LoginService } from './login.service';
import { UserService } from './user.service';
import { Router} from '@angular/router'

@Injectable({
  providedIn: 'root'
})
export class LoginGuardService implements CanActivate {

  constructor(private loginService: LoginService, private router: Router) { }

  canActivate() {
    if (!this.loginService.isLoggedIn()){
      this.router.navigateByUrl('/login');
      return false;
    }
    else return true;
  }
}
