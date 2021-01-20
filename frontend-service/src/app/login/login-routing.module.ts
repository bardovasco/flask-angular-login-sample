import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

/* Login Components */
import { LoginDashboardComponent } from './login-dashboard/login-dashboard.component';
import { SignInComponent } from './sign-in/sign-in.component';
import { SignUpComponent } from './sign-up/sign-up.component';

const routes: Routes = [
  { path: '', redirectTo: 'dashboard' },
  { path: 'dashboard', component: LoginDashboardComponent },
  { path: 'signIn', component: SignInComponent },
  { path: 'signUp', component: SignUpComponent }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LoginRoutingModule { }
