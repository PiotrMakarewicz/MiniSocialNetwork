import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UsersIObserveComponent } from './users-iobserve.component';

describe('UsersIObserveComponent', () => {
  let component: UsersIObserveComponent;
  let fixture: ComponentFixture<UsersIObserveComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UsersIObserveComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(UsersIObserveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
