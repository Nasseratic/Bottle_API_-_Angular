import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'home',
  template:
    `
   <md-card style="background-color: #fbfbfb !important; min-height: 34vw;" layout-align="center center">

  

<md-card class="example-form " layout-align="center center" style="margin: 3%; margin-top:0%; margin-bottom:0%; padding:2%;">
     <h2 style="text-align: center; color:#12a2dd; padding-top:1%;">Digizilla's Task‏ </h2>
</md-card>

<md-card class="example-form " layout-align="center center" style="margin: 3%; margin-bottom:0%; margin-top:0%; padding :2%;">
      <h4> Here is my first task for Digizilla :D </h4>
  </md-card>

<md-card class="example-form " layout-align="center center" style="margin: 3%; margin-top:0%; padding:2%;">

    

</md-card>


<md-card class="example-form " layout-align="center center" style="margin: 3%; margin-top:0%; padding:2%;">
      <table class="example-full-width" cellspacing="0">
      <tr>
        <td>
        </td>
        <td>
          <button  routerLink="/signup"  md-button style="background:#12a2dd; color:#fbfbfb; float: right; "> SIGN UP </button>
        </td>
      </tr>
      
      
          
    </table>
</md-card>
</md-card>

  `
  ,

})
export class Home implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
