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


def select_all_111():
    print("***********************         user ....   repository        **************")
    config = load_config()
    try:
            # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            cursor = conn.cursor()
                # Print PostgreSQL Connection properties
                #print ( conn.get_dsn_parameters(),"\n")

                # Print PostgreSQL version
            cursor.execute("SELECT * FROM personas")
            record = cursor.fetchall()
            print("You are connected to - ", record,"\n")
            return record
                
    except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    '''
    engine = connect(config)

    #engine = create_engine(
    "postgresql+pg8000://scott:tiger@localhost/test",
    isolation_level = "REPEATABLE READ"
)
    
    with Session(engine) as session:
        query=select(User)
        return session.exec(query).all()
    '''
    

def seleccionar_todos_usuarios(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            cursor = conn.cursor()
            # Print PostgreSQL Connection properties
            #print ( conn.get_dsn_parameters(),"\n")

            # Print PostgreSQL version
            cursor.execute("SELECT * FROM personas")
            record = cursor.fetchall()
            print("You are connected to - ", record,"\n")
            return record
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

