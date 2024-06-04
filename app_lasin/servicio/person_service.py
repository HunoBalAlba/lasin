#logica de negocio validadciones

from ..repositorio.person_repository import select_all,select_persona_by_ci,create_person,delete_person
from ..modelo.person_model import Persona

def select_all_person_service():
    #print("***********************         user ---service----             **************")
    personas= select_all()
    #print (users)
    return personas

def select_person_by_ci_service(ci:str):
    if(len(ci)!=0):
        return select_persona_by_ci(ci)
    else:
        return select_all()
    



def create_person_service(ci:str,nombre:str,materno:str,paterno:str,sexo:str,fecha_n):
    #dict_tipo_usuario={'Estudiante':'e','Administrador':'a','Docente':'d','Público':'p'}
    persona =select_persona_by_ci(ci)
    if(len(persona)==0):
        person_save=Persona(ci=ci,nombre=nombre,materno=materno,paterno=paterno,sexo=sexo,fecha_n=fecha_n)
        return create_person(person_save)
    else:
        print('la persona ya existe')
        raise BaseException('la persona ya existe - baseException')

def delete_person_service(ci:str):
    return delete_person(ci=ci)

