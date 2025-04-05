import { HttpClient } from '@angular/common/http';
import { Injectable, signal } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private webSocket: WebSocket | null = null;

  private baseUrl = 'http://localhost:8000';

  // Signal to hold the value
  value = signal<number>(0);

  constructor(private http: HttpClient) {}

  start(): Observable<any> {
    console.log('Starting async task...');
    return this.http.post(`${this.baseUrl}/start`, {}).pipe(
      catchError((error) => {
        console.error('Error occurred:', error);
        return throwError(error);
      })
    );
  }

  stop() {
    return this.http.post(`${this.baseUrl}/stop`, {}).pipe(
      catchError((error) => {
        console.error('Error occurred:', error);
        return throwError(error);
      })
    );
  }

  pause() {
    return this.http.post(`${this.baseUrl}/pause`, {}).pipe(
      catchError((error) => {
        console.error('Error occurred:', error);
        return throwError(error);
      })
    );
  }

  restart() {
    return this.http.post(`${this.baseUrl}/restart`, {}).pipe(
      catchError((error) => {
        console.error('Error occurred:', error);
        return throwError(error);
      })
    );
  }

  // Connect to the WebSocket server
  connectSocket(): void {
    console.log('Connecting to WebSocket...');
    this.webSocket = new WebSocket('ws://localhost:8000/ws');

    this.webSocket.onopen = () => {
      console.log('WebSocket connection established.');
    };

    this.webSocket.onmessage = (event) => {
      console.log('Message received from server:', event.data);
      const data = event.data;
      if (data !== undefined) {
        this.value.set(data); // Update the signal
      }
    };

    this.webSocket.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    this.webSocket.onclose = () => {
      console.log('WebSocket connection closed.');
    };
  }

  // Send a message to the WebSocket server
  sendMessage(message: any): void {
    if (this.webSocket && this.webSocket.readyState === WebSocket.OPEN) {
      this.webSocket.send(JSON.stringify(message));
      console.log('Message sent to server:', message);
    } else {
      console.error('WebSocket is not connected.');
    }
  }

  // Disconnect from the WebSocket server
  disconnectSocket(): void {
    if (this.webSocket) {
      this.webSocket.close();
      this.webSocket = null;
      console.log('WebSocket connection closed.');
    }
  }
}
