from sqlalchemy import Column, Integer, String
from app.db import Base

class user(Base):
   __tablename__="users"
   id=Column(Integer, primary_key=True)
   name=Column(String)
   email=Column(String, unique=True)
