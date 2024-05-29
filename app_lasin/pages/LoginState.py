#from app_lasin.templates import template
#######

import reflex as rx
import requests as rq
import re
###
from ..modelo.user_model import User
from ..servicio.user_service import select_all_user_service,select_user_by_email_service,create_user_service,delete_user_service


#from fastapi import FastAPI

#app = FastAPI()

'''
@rx.get("/fast")
async def root():
    return {"message": "Hello World"}


'''

class LoginState(rx.State):
    loader: bool=False
    username:str="example@mail.com"
    password:str
    name:str
    tipo_usuario:str="Administrador"
    email:str
    error=False
    #usuario:User
    estado:bool=False

    @rx.var
    def getEmail(self):
        return self.email
    @rx.var
    def getUssername(self):
        return self.username
    @rx.var
    def getPassword(self):
        return self.password
    @rx.var
    def getError(self):
        return self.error
    @rx.var
    def getEstado(self):
        return self.estado
    @rx.var
    def getName(self):
        return self.name
    @rx.var
    def getTipoUsuario(self):
        return self.tipo_usuario

    @rx.background
    async def loginService(self,data:dict):
        async with self:
            self.loader=True
            self.error=False
            #response=rq.post('http://localhost:8080/auth/login',json=data,headers={"Content-Type":"applicacion/json"})
            #response=rq.post('http://localhost:8000/',json=data,headers={"Content-Type":"aplicacion/json"})
            #if response.status_code==200:
            users=select_user_by_email_service(self.username)
            if len(users)!=0:
                for user in users:
                    print(user)
                    usuario:User=user
                    self.name=usuario.name
                    self.email=usuario.username
                    print(self.getName)
                    print(self.getEmail)
                    #self.estado=True
                    if user.password==self.password:
                        self.estado=True
                        print(self.loader,"   loader")
                        self.loader=False
                        print(self.loader," loader")
                        return rx.redirect("/")
                    else:
                        print("..no coinciden las contraseñas ",self.username, "   verifique los paswword")
                        self.loader=False
                        self.error=True
                        self.estado=False
                    #self.loader=False
                    #return rx.redirect("/login")
                    
                    


                #self.name=lista[0][0]
                
                #print(type(users[0]))
                #usuario=user
                #rint(usuario.name)


                #if True:
                #self.response=response.json()
                self.loader=False
                #return rx.direct('/ins')
                return rx.redirect("/login")
            else:
                print("..no se encontro al usuario ",self.username, "   verifique los credenciales")
                self.loader=False
                self.error=True
                self.estado=False
    @rx.var
    def user_invalid(self)->bool:
        return not (re.match(r"[^@]+@[^@]+.[^@]+",self.username)and "example@mail.com")
    
    @rx.var
    def user_empty(self)->bool:
        return not self.username.strip()
    
    @rx.var
    def password_empty(self)->bool:
        return not (self.password.strip())
    
    @rx.var
    def validate_fields(self)->bool:
        return(
            self.user_empty
            or self.user_invalid
            or self.password_empty
        )
    #@rx.var
    def cerrar_sesion_dd(self):
        self.estado=False
#@rx.page(route="/login",title="login")
#@template(route="/cert", title="Certificados")

#select_user_by_email_service
