import { Component, Input, OnInit } from '@angular/core';
import { backendAddress } from '../global-variables'

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {

  @Input() id: any;

  constructor() { }

  async getPost() {
    if (this.id) {
      const result = await fetch(backendAddress + 'post/150');
      const json = await result.json();
      return json['posts'][0]
    }
  }

  ngOnInit() {
   this.getPost().then(res=>console.log(res))
  }

}
