import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'my-footer',
  template:
    `
   <footer class="mdl-mini-footer">
  <div class="mdl-mini-footer__left-section">
    <div class="mdl-logo">
      Digizilla's Task‏
    </div>
  </div>
  <div class="mdl-mini-footer__right-section">
    <button class="mdl-mini-footer__social-btn">  </button>
    <button class="mdl-mini-footer__social-btn">  </button>
    <button class="mdl-mini-footer__social-btn">  </button>
  </div>
  
  </footer>

  `
  ,

})
export class myFooter implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
