from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,String,Integer,Column,ForeignKey,Text
from sqlalchemy.orm import relationship,scoped_session,sessionmaker
import os


Base_DIR=os.path.dirname(os.path.realpath(__file__))
connection_str="sqlite:///"+os.path.join(Base_DIR,'posts.db')
Base=declarative_base()
engine=create_engine(connection_str,echo=True)


class User(Base):
    __tablename__="users"
    id=Column(Integer(),primary_key=True)
    username=Column(String(45),nullable=False)
    email=Column(String(80),nullable=False)
    posts=relationship("Posts",backref="author")

    def __repr__(self) -> str:
        return f"<User {self.username}>"
    

class Posts(Base):
    __tablename__="posts"
    id=Column(Integer(),primary_key=True)
    title=Column(String(),nullable=False)
    content=Column(Text(),nullable=False)
    userId=Column(Integer(),ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"<User {self.title}>"
    

session=scoped_session(
    sessionmaker(bind=engine)
)    
    

Base.metadata.create_all(bind=engine)