import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { User } from './user';


@Injectable({
  providedIn: 'root'
})
export class LoginService {
  //userApi = 'http://127.0.0.1:5000/user';
  userApi = 'https://enfvseeir93s3xr.m.pipedream.net';

  constructor(
    private httpClient: HttpClient
  ) { }

  httpHeaders = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }

  addUser(userData: User): Observable<User> {
    return this.httpClient.post<User>(
      this.userApi,
      JSON.stringify(userData),
      this.httpHeaders
    ).pipe(
      retry(1),
      catchError(this.processError)
    )
  }

  processError(err) {
    let message = '';
    if (err.error instanceof ErrorEvent) {
      message = err.error.message;
    }
    else {
      message = `Error code: ${err.status}\nMessage: ${err.message}`
    }
    console.log(message);
    return throwError(message);
  }
}
