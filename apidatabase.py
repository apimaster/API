from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key = True)
    username = Column(String)
    password_hash = Column(String)
    email = Column(String)
    picture = Column(String)
    
engine = create_engine('sqlite:///apidatabase.db')
Base.metadata.create_all(engine)



