from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  email = Column(String)
  password = Column(String)


class Blog(Base):
  __tablename__ = 'blogs'

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  body = Column(String)

# データベースを再構築した場合、一度.blog.dbを削除してから再度サーバーを立ち上げないと、エラーが出る。