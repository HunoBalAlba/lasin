from sqlmodel import create_engine

def connect():
    #print("intentando conectar")
    engine = create_engine("postgresql://postgres:abc@localhost:5432/db_academico",echo=False)
    #print("se ha conectado sin excepciones...")
    return engine