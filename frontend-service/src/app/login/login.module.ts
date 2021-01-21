import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { LoginRoutingModule } from './login-routing.module';
import { SignInComponent } from './sign-in/sign-in.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { LoginDashboardComponent } from './login-dashboard/login-dashboard.component';
import { FormDirective } from './form.directive';


@NgModule({
  declarations: [
    SignInComponent,
    SignUpComponent,
    LoginDashboardComponent,
    FormDirective
  ],
  imports: [
    CommonModule,
    LoginRoutingModule,
    FormsModule,
    ReactiveFormsModule,
  ]
})
export class LoginModule { }
