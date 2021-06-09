import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PostsInterestingComponent } from './posts-interesting.component';

describe('PostsInterestingComponent', () => {
  let component: PostsInterestingComponent;
  let fixture: ComponentFixture<PostsInterestingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PostsInterestingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PostsInterestingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
