import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PostsIDislikeComponent } from './posts-idislike.component';

describe('PostsIDislikeComponent', () => {
  let component: PostsIDislikeComponent;
  let fixture: ComponentFixture<PostsIDislikeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PostsIDislikeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PostsIDislikeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
