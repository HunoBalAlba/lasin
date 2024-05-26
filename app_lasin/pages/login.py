from app_lasin.templates import template
#######

import reflex as rx
import requests as rq
import re

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
    error=False

    @rx.background
    async def loginService(self,data:dict):
        async with self:
            self.loader=True
            self.error=False
            #response=rq.post('http://localhost:8080/auth/login',json=data,headers={"Content-Type":"applicacion/json"})
            response=rq.post('http://localhost:8000/',json=data,headers={"Content-Type":"aplicacion/json"})
            if response.status_code==200:
                self.response=response.json()
                self.loader=False
                return rx.direct('/')
            else:
                self.loader=False
                self.error=True
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




#@rx.page(route="/login",title="login")
#@template(route="/cert", title="Certificados")
@template(route="/login",title="login")
def login()->rx.Component:
    #return rx.section(
    return rx.section(
        rx.flex(
            rx.image(src='/logo_i.png',width="300px",border_radius="15px,50px"),
            rx.heading('Inicio de Sesión'),
            rx.form.root(
                rx.flex(
                    field_form_component_general("Usuario","Ingrese su correo","Ingrese un correo válido","username",
                                                 LoginState.set_username,LoginState.user_invalid),

                    field_form_component("Contraseña","Ingrese su contraseña","password",
                                         LoginState.set_password,"password"),

                    rx.form.submit(
                        rx.cond(
                            LoginState.loader,
                            rx.chakra.spinner(color="red",size="xs"),
                            rx.button(
                                "Iniciar sesión",
                                disabled=LoginState.validate_fields,
                                width="30vw"
                            ),
                        ),
                        as_child=True,
                    ),
                    direction="column",
                    justify="center",
                    align="center",
                    spacing="2",
                ),
                rx.cond(
                    LoginState.error,
                    rx.callout(
                        "Credenciales incrrectas",
                        icon="alert_triangle",
                        color_scheme="red",
                        role="alert",
                        style={"margin_top": "10px"}
                    ),
                ),
                on_submit=LoginState.loginService,
                reset_on_submit=True,
                width="80%",
            ),
            width="100%",
            direction="column",
            align="center",
            justify="center",
        ),
        style=style_section,
        justify="center",
        width="100%",
        
    )

def field_form_component(label:str,placeholder:str,name_var:str,
                         on_change_function,type_field:str)->rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input.input(
                    placeholder=placeholder,
                    on_change=on_change_function,
                    name=name_var,
                    type=type_field,
                    required=True,

                ),
                as_child=True,
            ),
            rx.form.message(
                "El Campo no puede ser nulo",
                match="valueMissing",
                color="red",
            ),
            direction="column",
            spacing="2",
            align="stretch",
        ),
        name=name_var,
        width="30vw"

    )

def field_form_component_general(label:str,placeholder:str,message_validate:str,name:str,
                                 on_change_function,show)->rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input.input(
                    placeholder=placeholder,
                    on_change=on_change_function,
                    name=name,
                    required=True
                ),
                as_child=True
            ),
            rx.form.message(
                message_validate,
                name=name,
                match="valueMissing",
                force_match=show,
                color="red"
            ),
            direction="column",
            spacing="2",
            align="stretch"
        ),
        name=name,
        width="30vw"

    )

style_section={
    "height":"90vh",
    "width":"80%",
    "margin":"auto",
}