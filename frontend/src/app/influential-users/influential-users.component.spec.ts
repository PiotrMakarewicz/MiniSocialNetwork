import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InfluentialUsersComponent } from './influential-users.component';

describe('InfluentialUsersComponent', () => {
  let component: InfluentialUsersComponent;
  let fixture: ComponentFixture<InfluentialUsersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InfluentialUsersComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(InfluentialUsersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
