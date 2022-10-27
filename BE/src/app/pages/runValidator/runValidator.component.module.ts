import { CommonModule , } from '@angular/common';
import { NgModule , CUSTOM_ELEMENTS_SCHEMA } from '@angular/core' ;
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { runValidatorComponent } from './runValidator.component';

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
        CommonModule,
        FormsModule,
        CalendarModule,
        InputTextModule,
        InputTextareaModule,
        DropdownModule,
        ButtonModule,
        FormsModule,
        ReactiveFormsModule,
        TableModule
    ],
    declarations:[runValidatorComponent],
    exports:[
        runValidatorComponent,
        CommonModule
        
    ],
    schemas: [ CUSTOM_ELEMENTS_SCHEMA ]
})
export class runValidator {}