import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { MenuComponent } from './menu/menu.component';
import { CarteirasComponent } from './carteiras/carteiras.component';
import { AtivoService } from './shared/service/ativo.service';
import { CarteiraService } from './carteiras/service/carteira.service';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { HistoricoListComponent } from './historico-list/historico-list.component';
import { CurrencyMaskModule } from 'ng2-currency-mask'
import { LOCALE_ID } from '@angular/core';


@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    HomeComponent,
    CarteirasComponent,
    HistoricoListComponent
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule,
    CurrencyMaskModule
  ],
  providers: [AtivoService, CarteiraService,{provide: LOCALE_ID, useValue: 'pt-BR'}],
  bootstrap: [AppComponent]
})
export class AppModule { }
