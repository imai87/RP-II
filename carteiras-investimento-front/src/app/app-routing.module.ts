import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { CarteirasComponent } from './carteiras/carteiras.component';

const routes: Routes = [
  { path: '', pathMatch: 'full' , component: HomeComponent },
  { path: 'carteiras', component: CarteirasComponent }
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
