/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { UserSmallComponent } from './user-small.component';

describe('UserSmallComponent', () => {
  let component: UserSmallComponent;
  let fixture: ComponentFixture<UserSmallComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UserSmallComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UserSmallComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
