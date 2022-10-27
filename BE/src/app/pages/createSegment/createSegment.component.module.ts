import { CommonModule , } from '@angular/common';
import { NgModule , CUSTOM_ELEMENTS_SCHEMA } from '@angular/core' ;
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { CalendarModule } from 'primeng/calendar';
import {InputTextModule} from 'primeng/inputtext';
import {DropdownModule} from 'primeng/dropdown';
import { createSegmentComponent } from './createSegment.component';
import {InputTextareaModule} from 'primeng/inputtextarea';
import {PrettyJsonPipe} from "./prettyjson.pipe";
import {ButtonModule} from 'primeng/button';

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
        ButtonModule

    ],
    declarations:[createSegmentComponent , PrettyJsonPipe ],
    exports:[
        createSegmentComponent,
        CommonModule
        
    ],
    schemas: [ CUSTOM_ELEMENTS_SCHEMA ]
})
export class createSegment {}