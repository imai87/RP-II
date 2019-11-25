import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import 'rxjs';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { Ativo, AtivoAtual, HistoricoAtivo } from '../model/ativo.model';

const httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  
@Injectable()
export class AtivoService {
  constructor(private http: HttpClient) { }
  private url = environment.baseUrl;
  pageAtivos = '/ativos/';
  pageAtivosAtuais = '/atual/';
  pageAtivosHistorico = '/historico/';


  public findAtivos(page: number): Observable<Ativo[]> {
    const params = new HttpParams()
    .append('limit', '10')
    .append('offset', (page * 10).toString());
    return this.http.get<Ativo[]>(this.url + this.pageAtivos, { params: params });
  }
  public findAtivosAtuais(page: number): Observable<AtivoAtual[]> {
    const params = new HttpParams()
    .append('limit', '10')
    .append('offset', (page * 10).toString());
    return this.http.get<AtivoAtual[]>(this.url + this.pageAtivosAtuais, { params: params });
  }
  public findAtivosAtuaisLim(): Observable<AtivoAtual[]> {
    const params = new HttpParams()
    .append('limit', '999');
    return this.http.get<AtivoAtual[]>(this.url + this.pageAtivosAtuais, { params: params });
  }
  public findAtivosHistorico(page: number, stock: string): Observable<HistoricoAtivo[]> {
    const params = new HttpParams()
    .append('limit', '10')
    .append('offset', (page * 10).toString())
    .append('stock', stock);
    return this.http.get<HistoricoAtivo[]>(this.url + this.pageAtivosHistorico, { params: params });
  }

  public findAtivoByStock(stock: string): Observable<Ativo> {
    const params = new HttpParams()
    .append('Stock', stock);

    return this.http.get<Ativo>(this.url + this.pageAtivos, { params: params });
  }

  public findAtualByStock(stock: string): Observable<AtivoAtual> {
    const params = new HttpParams()
    .append('stock', stock);

    return this.http.get<any>(this.url + this.pageAtivosAtuais, { params: params });
  }
}