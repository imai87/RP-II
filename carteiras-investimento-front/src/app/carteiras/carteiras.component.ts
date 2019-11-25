import { Component } from '@angular/core';
import { AtivoService } from '../shared/service/ativo.service';

@Component({
  selector: 'carteiras-component',
  templateUrl: './carteiras.component.html',
  styleUrls: ['./carteiras.component.css']
})
export class CarteirasComponent {
  constructor(private ativoService: AtivoService){}
  listAtivos = [];

  ngOnInit() {
    this.buscarHistoricoAtivo();
  }
  
  buscarHistoricoAtivo(){
    this.ativoService.findAtivosAtuaisLim()
    .subscribe(data => {          
      this.listAtivos = data;
    });
  }

}
