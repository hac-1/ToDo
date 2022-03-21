import { Component,Injectable } from '@angular/core';
import {HttpClient,HttpHeaders} from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
@Injectable()
export class AppComponent {
  title = 'TODO';
  constructor(private http: HttpClient){}
  items:any=[];

  ngOnInit(): void {
  }
  get_value(){
    this.http.get('http://localhost:5000/view').subscribe(
      data=>{this.items=data;},
    );
  }

 delete_value(item:any){
  var options = {
    headers: new HttpHeaders({'Content-Type': 'application/json'}),
    body: {"task":item}
  }
    this.http.delete('http://localhost:5000/delete',options).subscribe(
      data => {
      },
      error => {
        alert("COULDN'T DELETE DUE TO SERVER ISSUE")
      },
    );
  }

 add_value(item:any){
  var headers = new HttpHeaders()
  .set('Authorization', 'my-auth-token')
  .set('Content-Type', 'application/json');

  this.http.post('http://localhost:5000/insert', JSON.stringify({"task":item}), {headers: headers}).subscribe(
  data => {
  },
  error => {alert("COULDNT BE CREATED DUE TO SERVER ISSUE")}
  );
 }

}
