import { Component, OnInit  } from '@angular/core';
import {MdDialog, MdDialogRef} from "@angular/material";
import { AppShellModule } from '@angular/app-shell';
import {ActivatedRoute} from '@angular/router'
import { AppRoutingModule } from '../../routers.module';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router'

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
  providers: [AppShellModule],
  
})


export class NavbarComponent implements OnInit {
  
  userName ="";

  constructor(public dialog: MdDialog , private route:ActivatedRoute , private router: Router , private auth:AuthService) {}

  openLoginDialog() {
    this.dialog.open(DialogResultExampleDialog1);

  }

  logout(){
    this.auth.setUser("");
    this.router.navigate(["/"]);
  }

  ngOnInit() {
    this.router.events.subscribe(
      () => {
      //this.userName=this.auth.getUser();
      if(localStorage.getItem("currentUser") !== null ){
      this.userName=localStorage.getItem("currentUser");
      }
      console.log(this.userName);
              
      }
    );

    
    /*this.route
      .queryParams
      .subscribe(params => {
        // Defaults to 0 if no query param provided.
        this.userName = params['user'] || "";
        console.log(params['user']);
        //this.router.navigate(['/home'], { queryParams: {} });

      });
    */

  }


  

}



@Component({
  selector: 'dialog-result-example-dialog1',
  templateUrl: 'login-form.html',
  styles:[ `

.example-full-width {
  width: 100%;
  margin: 3px;
  min-width: 210px;
  
}
`]
})

export class DialogResultExampleDialog1 {

  constructor(public dialog: MdDialog,public dialogRef: MdDialogRef<DialogResultExampleDialog1> , private router:AppRoutingModule ) {
  

   }



    close() {
    this.dialog.closeAll();
      }
    
}


