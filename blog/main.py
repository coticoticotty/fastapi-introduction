from os import stat
from fastapi import FastAPI, Depends, status, Response, HTTPException
from .schemas import Blog
from .models import Base
from . import models
from .database import engine, sessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
  db = sessionLocal()

  try:
    yield db
  finally:
    db.close()

Base.metadata.create_all(engine)

@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(blog: Blog, db: Session = Depends(get_db)):
  new_blog = models.Blog(title=blog.title, body=blog.body)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog

@app.get('/blog', status_code=status.HTTP_200_OK)
def all_fetch(db: Session = Depends(get_db)):
  blogs = db.query(models.Blog).all()
  return blogs

@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def show(id: int, response: Response, db: Session = Depends(get_db)):
  blog = db.query(models.Blog).filter(models.Blog.id == id).first()
  if not blog:
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f'Blog with the id {id} is not available')
  return blog

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
  blog = db.query(models.Blog).filter(models.Blog.id == id)
  if not blog.first():
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f'Blog with the id {id} is not available')
  blog.delete(synchronize_session=False)
  db.commit()
  return 'Delete completed'