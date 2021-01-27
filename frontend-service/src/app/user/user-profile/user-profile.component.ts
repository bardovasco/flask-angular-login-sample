import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

import { User } from 'src/app/login/user';
import { LoginService } from '../../login/login.service';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {
  public userData: User;

  constructor(
    private loginService: LoginService,
    private location: Location
  ) { }

  ngOnInit(): void {
    if (!this.userData) {
      this.location.back();
    }
    console.log(this.userData)
    //this.loginService.getOne(this.userData)
      //.subscribe(res => {
        //console.log(res);
      //})
  }
}
