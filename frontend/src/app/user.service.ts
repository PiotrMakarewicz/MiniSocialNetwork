import { stringify } from '@angular/compiler/src/util';
import { Injectable } from '@angular/core';
import { backendAddress } from './global-variables'

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor() { }

  public async getUser(id: number){
    const results = await fetch(backendAddress+String(id));
    const json = await results.json();
    if (json['users'].length > 0)
      return json['users'][0];
    else return null;
  }
}
