import { Component, Input, OnInit, Output } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { backendAddress} from '../global-variables'

@Component({
  selector: 'app-tag-page',
  templateUrl: './tag-page.component.html',
  styleUrls: ['./tag-page.component.css']
})
export class TagPageComponent implements OnInit {

  constructor(private route: ActivatedRoute) { }

  @Output() tagname: string = ""; 
  @Output() postids: any[] = [];
  private sub: any;

  async ngOnInit() {
    this.sub = this.route.params.subscribe(async params => {
       this.tagname = params['tagname'];
       let result = await fetch(backendAddress + 'tag/' + this.tagname);
       let json = await result.json();
       let posts = json['posts'];
       this.postids = [];
       for (let post of posts){
         this.postids.push(Number(post['id']));
       }
    });
  }

  ngOnDestroy() {
    if (this.sub)
      this.sub.unsubscribe();
  }

}
