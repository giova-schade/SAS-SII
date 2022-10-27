import { CommonModule , } from '@angular/common';
import { NgModule , CUSTOM_ELEMENTS_SCHEMA } from '@angular/core' ;
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { viewLogsComponent } from './viewLogs.component';

import { CalendarModule } from 'primeng/calendar';
import {InputTextModule} from 'primeng/inputtext';
import {DropdownModule} from 'primeng/dropdown';
import {InputTextareaModule} from 'primeng/inputtextarea';
import {ButtonModule} from 'primeng/button';
import { TableModule } from 'primeng/table';
import { ProgressBarModule } from 'primeng/progressbar';
import {BlockUIModule} from 'primeng/blockui';
@NgModule({

    imports:[
        ProgressBarModule,
        BlockUIModule,
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        CalendarModule,
        InputTextModule,
        InputTextareaModule,
        DropdownModule,
        ButtonModule,
        TableModule
    ],
    declarations:[viewLogsComponent],
    exports:[
        viewLogsComponent,
        CommonModule,
        FormsModule
    ],
    schemas: [ CUSTOM_ELEMENTS_SCHEMA ]
})
export class viewLogs {}