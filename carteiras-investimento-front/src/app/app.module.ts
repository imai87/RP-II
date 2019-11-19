import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { MenuComponent } from './menu/menu.component';
import { CarteirasComponent } from './carteiras/carteiras.component';
import { EmpresaService } from './shared/service/empresa.service';
import { CarteiraService } from './carteiras/service/carteira.service';
import { AppRoutingModule } from './app-routing.module';

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    HomeComponent,
    CarteirasComponent
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [EmpresaService, CarteiraService],
  bootstrap: [AppComponent]
})
export class AppModule { }
