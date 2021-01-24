import { Component, OnInit, Input } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Md5 } from 'ts-md5/dist/md5';

import { LoginService } from '../login.service';


@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent implements OnInit {
  userForm: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private loginService: LoginService,
    private router: Router,
  ) {
    this.userForm = this.formBuilder.group({
      username: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      passPhrase: ['', [Validators.required, Validators.minLength(8)]]
    })
  }

  ngOnInit(): void {
  }

  onSubmit(userData) {
    // Encrypt password
    userData.passPhrase = Md5.hashStr(userData.passPhrase);
    console.log(userData);
    // POST Http Request
    //return this.loginService.addUser(userData)
      //.subscribe(res => console.log(res))
  }
}
