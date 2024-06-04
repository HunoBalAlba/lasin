###metodos que interactuan con la base de datos
# declaramos los datos para wl acceso a base de datos


import psycopg2
from ..modelo.person_model import Persona
from .connect_db import connect
from sqlmodel import Session, select

from .config import load_config

def select_all():
     engine=connect()
     with Session(engine) as session:
          query=select(Persona)
          return session.exec(query).all()
     
def select_persona_by_ci(ci:str):
     engine=connect()
     with Session(engine) as session:
          #query=select(Persona).where(Persona.username==email)
          query=select(Persona).where(Persona.ci==ci)
          # select * from 
          return session.exec(query).all()
     
def create_person(persona:Persona):
    engine=connect()
    with Session(engine) as session:
        session.add(persona)
        session.commit()
        query=select(Persona)
        # select * from 
        return session.exec(query).all()

def delete_person(ci:str):
    engine=connect()
    with Session(engine) as session:
        query=select(Persona).where(Persona.ci==ci)
        person_delete=session.exec(query).one()
        session.delete(person_delete)
        session.commit()
        query=select(Persona)
        return session.exec(query).all()
    
    