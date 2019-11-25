import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { CarteirasComponent } from './carteiras/carteiras.component';
import { HistoricoListComponent } from './historico-list/historico-list.component';

const routes: Routes = [
  { path: '', pathMatch: 'full' , component: HomeComponent },
  { path: 'carteiras', component: CarteirasComponent },
  { path: 'historicolist', component: HistoricoListComponent },
  { path: 'historicolist/:stock', component: HistoricoListComponent }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { }
