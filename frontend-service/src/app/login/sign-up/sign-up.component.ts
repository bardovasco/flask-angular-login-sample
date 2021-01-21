import { Component, OnInit, Input } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { LoginService, User } from '../login.service';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent implements OnInit {
  userForm: FormGroup;

  @Input() userData: User = {
    username: '',
    email: '',
    passPhrase: ''
  }

  constructor(
    private formBuilder: FormBuilder,
    private loginService: LoginService
  ) {
    this.userForm = this.formBuilder.group({
      username: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      passPhrase: ['', [Validators.required, Validators.minLength(8)]]
    })
  }

  ngOnInit(): void {
  }

  onSubmit() {
    return this.loginService.addUser(this.userData)
      .subscribe(res => console.log(res))
  }
}
