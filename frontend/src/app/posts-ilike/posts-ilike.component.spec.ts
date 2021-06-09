import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PostsILikeComponent } from './posts-ilike.component';

describe('PostsILikeComponent', () => {
  let component: PostsILikeComponent;
  let fixture: ComponentFixture<PostsILikeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PostsILikeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PostsILikeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
