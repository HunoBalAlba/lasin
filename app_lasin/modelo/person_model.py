import reflex as rx
from typing import Optional
from sqlmodel import  Field

class Persona(rx.Model, table=True):

    id_persona:Optional [int] = Field(default=None, primary_key=True)
    #id:int
    ci:str
    nombre:str
    paterno :str
    materno :str
    sexo :str
    fecha_n :str
    
    ''' def __init__(self, id,ci,nombre,paterno,materno,sexo,fecha_nac):
        self.id = id
        self.ci=ci
        self.nombre=nombre
        self.paterno=paterno
        self.materno=materno
        self.sexo=sexo
        self.fecha_nac=fecha_nac

    '''