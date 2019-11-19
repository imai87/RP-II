import { Component } from '@angular/core';

import { carteiras } from '../carteiras';

@Component({
  selector: 'carteiras-component',
  templateUrl: './carteiras.component.html',
  styleUrls: ['./carteiras.component.css']
})
export class CarteirasComponent {
  carteiras = carteiras;
  ativos = null;

}
