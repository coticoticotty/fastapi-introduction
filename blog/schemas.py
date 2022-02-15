from pydantic import BaseModel

class Blog(BaseModel):
  title: str
  body: str

  class Config:
    orm_mode = True

class ShowBlog(BaseModel):
  title: str
  body: str

  class Config:
    orm_mode = True
0
class User(BaseModel):
  name: str
  email: str
  password: str

  class Config:
    orm_mode: True

class ShowUser(BaseModel):
  name: str
  email: str
  password: str

  class Config:
    orm_mode: True
