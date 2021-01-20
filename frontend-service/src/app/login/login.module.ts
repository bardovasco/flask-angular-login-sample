import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LoginRoutingModule } from './login-routing.module';
import { SignInComponent } from './sign-in/sign-in.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { LoginDashboardComponent } from './login-dashboard/login-dashboard.component';


@NgModule({
  declarations: [
    SignInComponent,
    SignUpComponent,
    LoginDashboardComponent
  ],
  imports: [
    CommonModule,
    LoginRoutingModule
  ]
})
export class LoginModule { }
