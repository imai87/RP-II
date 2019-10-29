import { Component } from '@angular/core';

import { carteiras } from '../carteiras';

@Component({
  selector: 'home-component',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  carteiras = carteiras;
  ativos = null;

}
