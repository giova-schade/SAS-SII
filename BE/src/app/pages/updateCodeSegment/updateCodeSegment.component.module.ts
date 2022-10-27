import { CommonModule , } from '@angular/common';
import { NgModule , CUSTOM_ELEMENTS_SCHEMA } from '@angular/core' ;
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { CalendarModule } from 'primeng/calendar';
import {InputTextModule} from 'primeng/inputtext';
import {DropdownModule} from 'primeng/dropdown';
import {InputTextareaModule} from 'primeng/inputtextarea';
import {ButtonModule} from 'primeng/button';

import { updateCodeSegmentComponent } from './updateCodeSegment.component';

@NgModule({

    imports:[
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        CalendarModule,
        InputTextModule,
        InputTextareaModule,
        DropdownModule,
        ButtonModule

    ],
    declarations:[updateCodeSegmentComponent  ],
    exports:[
        updateCodeSegmentComponent,
        CommonModule
    ],
    schemas: [ CUSTOM_ELEMENTS_SCHEMA ]
})
export class updateCodeSegment {}
