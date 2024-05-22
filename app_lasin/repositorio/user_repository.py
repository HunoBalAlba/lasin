###metodos que interactuan con la base de datos
# declaramos los datos para wl acceso a base de datos


import psycopg2
from ..modelo.user_model import User
from .connect_db import connect
from sqlmodel import Session, select

from .config import load_config

def select_all():
     engine=connect()
     with Session(engine) as session:
          query=select(User)
          return session.exec(query).all()
     
def select_user_by_email(email:str):
     engine=connect()
     with Session(engine) as session:
          query=select(User).where(User.username==email)
          # select * from 
          return session.exec(query).all()
     
def create_user(user:User):
    engine=connect()
    with Session(engine) as session:
        session.add(user)
        session.commit()
        query=select(User)
        # select * from 
        return session.exec(query).all()

def delete_user(email:str):
    engine=connect()
    with Session(engine) as session:
        query=select(User).where(User.username==email)
        user_delete=session.exec(query).one()
        session.delete(user_delete)
        session.commit()
        query=select(User)
        return session.exec(query).all()
    
    