import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { LoginService } from '../login.service';
import { User } from '../user';


@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent implements OnInit {
  @Output() userData = new EventEmitter();
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

  onSubmit() {
    // POST Http Request
    return this.loginService.addUser(this.userForm.value)
      .subscribe(res => {
        // emit event
        this.userData.emit({
          email: this.userForm.get('email').value,
          passPhrase: this.userForm.get('passPhrase').value
        })
        // Redirect to User profile
        this.router.navigateByUrl('/user')
      })
  }
}
