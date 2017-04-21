import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Home } from './components/home';
import {SignUp} from './components/signup';
const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: Home },  
  { path: 'signup', component: SignUp },  
  { path: '**', redirectTo: '/home' }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}