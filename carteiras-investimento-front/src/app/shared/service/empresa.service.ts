import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import 'rxjs';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { Empresa } from '../model/empresa.model';

const httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  
@Injectable()
export class EmpresaService {
constructor(private http: HttpClient) { }
private url = environment.baseUrl;
page = '/empresa';
public findAll(codigoEmpresa: string, nroEmpresa: number, especieEmpresa: string, selecao: string): Observable<any> {
    const params = new HttpParams()
      .append('codEmpresa', codigoEmpresa)
      .append('nroempresa', nroEmpresa.toString())
      .append('especie', especieEmpresa)
      .append('selecao', selecao);

    return this.http.get<Empresa[]>(this.url + this.page, { params: params });
}
public findById(codEmpresa: number, nroempresa: number): Observable<Empresa> {
    const params = new HttpParams()
      .append('codEmpresa', codEmpresa.toString())
      .append('nroempresa', nroempresa.toString());

    return this.http.get<Empresa>(this.url + this.page + '/id', { params: params });
  }
  
  public save(Empresa: Empresa): any {
    return this.http.post(this.url + this.page, Empresa, httpOptions);
  }

  public delete(codEmpresa: string, nroempresa: number): any {
    const params = new HttpParams()
    .append('codEmpresa', codEmpresa)
    .append('nroempresa', nroempresa.toString());
    return this.http.delete(this.url + this.page + '/id', { params: params });
  }
}