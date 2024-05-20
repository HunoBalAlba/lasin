import psycopg2
from app_lasin.conexiones.config22 import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            cursor = conn.cursor()
            # Print PostgreSQL Connection properties
            #print ( conn.get_dsn_parameters(),"\n")

            # Print PostgreSQL version
            cursor.execute("SELECT version()")
            record = cursor.fetchone()
            print("You are connected to - ", record,"\n")

            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def mostrar_personas(config):
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


if __name__ == '__main__':
    config = load_config()
    connect(config)