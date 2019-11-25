import { Component, ViewChild } from '@angular/core';
import { ActivatedRoute} from '@angular/router';
import { AtivoService } from '../shared/service/ativo.service';
import { HistoricoAtivo, Ativo } from '../shared/model/ativo.model';


@Component({
  selector: 'historico-list-component',
  templateUrl: './historico-list.component.html',
  styleUrls: ['./historico-list.component.css']
})
export class HistoricoListComponent{
  constructor(private route:ActivatedRoute, private ativoService: AtivoService){}
  stock: any;
  ativo: Ativo;
  listHistorico = [];
  page = 0;

  ngOnInit() {
    this.stock = this.route.snapshot.queryParams['stock'];
    this.buscarHistoricoAtivo();
  }

  buscarHistoricoAtivo(){
    this.ativoService.findAtivosHistorico(this.page, this.stock)
    .subscribe(data => {          
      this.listHistorico = data;
    });
    this.ativoService.findAtivoByStock(this.stock)
    .subscribe(ativo => {
      this.ativo = ativo[0]});
  }


     // Botões antes e depois na lista de ativos
  reloadPreviousAtivos(event) {
    if(this.page != 0){
      this.page = this.page - 1;
      this.buscarHistoricoAtivo();
    }
  }      
  reloadNextAtivos(event) {
    this.page = this.page + 1;
    this.buscarHistoricoAtivo();
   }

}
