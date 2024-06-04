#logica de negocio validadciones

from ..repositorio.user_repository import select_all,select_user_by_email,create_user,delete_user
from ..modelo.user_model import User

def select_all_user_service():
    #print("***********************         user ---service----             **************")
    users= select_all()
    #print (users)
    return users

def select_user_by_email_service(email:str):
    if(len(email)!=0):
        return select_user_by_email(email)
    else:
        return select_all()
    



def create_user_service(username:str,password:str,phone:str,name:str,tipo_u:str):
    #dict_tipo_usuario={'Estudiante':'e','Administrador':'a','Docente':'d','Público':'p'}
    user =select_user_by_email(username)
    if(len(user)==0):
        user_save=User(username=username,password=password,phone=phone,name=name,tipo_u=tipo_u)
        return create_user(user_save)
    else:
        print('el usuario ya existe')
        raise BaseException('el usuario ya existe - baseException')

def delete_user_service(email:str):
    return delete_user(email=email)

