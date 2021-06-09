import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UsersIMightWantToObserveComponent } from './users-imight-want-to-observe.component';

describe('UsersIMightWantToObserveComponent', () => {
  let component: UsersIMightWantToObserveComponent;
  let fixture: ComponentFixture<UsersIMightWantToObserveComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UsersIMightWantToObserveComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(UsersIMightWantToObserveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
