import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule ,JsonpModule } from '@angular/http';
import { MaterialModule } from '@angular/material';
import { AppComponent } from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations'
import 'hammerjs';
import { myFooter } from './components/footer';
import { NavbarComponent,DialogResultExampleDialog1 } from './components/navbar/navbar.component';
import {AppRoutingModule} from './routers.module';
import {SignUp} from './components/signup';
import { AuthService } from './services/auth.service';
import { ProfileComponent } from './components/profile/profile.component';
import { Home } from './components/home';


@NgModule({
  declarations: [
    AppComponent,
    myFooter ,
    NavbarComponent,
    DialogResultExampleDialog1,
    SignUp,
    ProfileComponent,
    Home
  ],
  entryComponents: [DialogResultExampleDialog1] ,
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    JsonpModule,
    [MaterialModule] ,
    BrowserAnimationsModule,
    AppRoutingModule
  ],
  providers: [AuthService],
  bootstrap: [AppComponent],
  
})

export class AppModule {}
