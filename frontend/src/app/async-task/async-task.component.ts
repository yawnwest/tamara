import { Component, OnDestroy, OnInit, signal } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-async-task',
  templateUrl: './async-task.component.html',
  styleUrls: ['./async-task.component.css'],
})
export class AsyncTaskComponent implements OnInit, OnDestroy {
  constructor(public apiService: ApiService) {}

  ngOnInit(): void {
    this.apiService.connectSocket();
  }

  ngOnDestroy(): void {
    this.apiService.disconnectSocket();
  }

  startAsyncTask() {
    console.log('Starting async task...');
    this.apiService.start().subscribe({
      next: (response) => {
        console.log('Task started successfully:', response);
      },
      error: (error) => {
        console.error('Error starting task:', error);
      },
    });
  }

  stopAsyncTask() {
    this.apiService.stop().subscribe({
      next: (response) => {
        console.log('Task started successfully:', response);
      },
      error: (error) => {
        console.error('Error starting task:', error);
      },
    });
  }

  pauseAsyncTask() {
    this.apiService.pause().subscribe({
      next: (response) => {
        console.log('Task started successfully:', response);
      },
      error: (error) => {
        console.error('Error starting task:', error);
      },
    });
  }

  restartAsyncTask() {
    this.apiService.restart().subscribe({
      next: (response) => {
        console.log('Task started successfully:', response);
      },
      error: (error) => {
        console.error('Error starting task:', error);
      },
    });
  }
}
