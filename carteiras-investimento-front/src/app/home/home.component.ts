import { Component } from '@angular/core';

import { carteiras } from '../carteiras';

import { AtivoService } from '../shared/service/ativo.service'
import { Ativo } from '../shared/model/ativo.model'

@Component({
  selector: 'home-component',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent {
    listAtivos: Ativo[];
    page = 0;
    constructor(private ativoService: AtivoService) {
      
    }
    ngOnInit() {
      this.loadAtivos();
    }
  
    loadAtivos() {
      this.ativoService.findAtivos(this.page)
        .subscribe(data => {          
          this.listAtivos = data;
          console.log(this.listAtivos)
        });

      this.ativoService.findAtualByStock("FNOR11").subscribe(data => {     
        console.log(data)
      });
    }
      
    // Botões antes e depois na lista de ativos
    reloadPreviousAtivos(event) {
      if(this.page != 0){
        this.page = this.page - 1;
        this.loadAtivos();
      }
    }      
    reloadNextAtivos(event) {
      this.page = this.page + 1;
      this.loadAtivos();
    }
}
