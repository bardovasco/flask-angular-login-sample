import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { Md5 } from 'ts-md5/dist/md5';


@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css']
})
export class SignInComponent implements OnInit {
  userForm: FormGroup;

  constructor(
    private formBuilder: FormBuilder
  ) {
    this.userForm = this.formBuilder.group({
      email: ['', [Validators.email, Validators.required]],
      passPhrase: ['', [Validators.required]]
    })
  }

  ngOnInit(): void {
  }

  onSubmit(userData) {
    userData.passPhrase = Md5.hashStr(userData.passPhrase);
    console.log(userData);
  }
}
