import { Injectable} from '@angular/core';
import {Http, Response, URLSearchParams, RequestOptions} from '@angular/http';
import * as Rx from "rxjs/Rx";
import {Observable}     from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/publish';
import {Headers} from '@angular/http';

@Injectable()
export class AuthService {

  headers = new Headers({
    'Content-Type': 'application/json'
  });


  constructor(private http:Http) {}

  signUp( user ): Rx.Observable<Response>{
    let body = JSON.stringify({ "name":user.name , "pw":user.pw , "id":user.id , "email":user.email});
    let headers = new Headers({ 'Content-Type': 'application/json' });
    let options = new RequestOptions({ headers: headers});
    return this.http.post('http://127.0.0.1:8080/api/signup', body , options );
  }

  setUser(id:string){
      localStorage.setItem('currentUser',id);
  }
  
  getUser(){
      localStorage.getItem('currentUser');
  }


  login(loginDeta):Rx.Observable<any>{  
    console.log({ "email":loginDeta.email , "pw":loginDeta.pw });
    let body = JSON.stringify({ "email":loginDeta.email , "pw":loginDeta.pw });
    let headers = new Headers({ 'Content-Type': 'application/json' });
    let options = new RequestOptions({ headers: headers});
    return this.http.post('http://localhost:8080/api/login/', body , options ).map(this.extractData).publish().refCount();
  }



  private extractData(res: Response) {
    let body = res.json();
    return body || {};
  }


}
