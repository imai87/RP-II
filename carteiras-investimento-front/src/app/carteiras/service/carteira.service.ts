import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import 'rxjs';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';

const httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  
@Injectable()
export class CarteiraService {
constructor(private http: HttpClient) { }
private url = environment.baseUrl;
page = '/any';
public findAll(codigoany: string, nroany: number, especieany: string, selecao: string): Observable<any> {
    const params = new HttpParams()
      .append('codany', codigoany)
      .append('nroany', nroany.toString())
      .append('especie', especieany)
      .append('selecao', selecao);

    return this.http.get<any[]>(this.url + this.page, { params: params });
}
public findById(codany: number, nroany: number): Observable<any> {
    const params = new HttpParams()
      .append('codany', codany.toString())
      .append('nroany', nroany.toString());

    return this.http.get<any>(this.url + this.page + '/id', { params: params });
  }
  
  public save(any: any): any {
    return this.http.post(this.url + this.page, any, httpOptions);
  }

  public delete(codany: string, nroany: number): any {
    const params = new HttpParams()
    .append('codany', codany)
    .append('nroany', nroany.toString());
    return this.http.delete(this.url + this.page + '/id', { params: params });
  }
}