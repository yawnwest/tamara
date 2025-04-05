import { Component } from '@angular/core';
import { AsyncTaskComponent } from './async-task/async-task.component';

@Component({
  selector: 'app-root',
  imports: [AsyncTaskComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'tamara-frontend';
}
