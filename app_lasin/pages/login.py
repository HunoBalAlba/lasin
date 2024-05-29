from app_lasin.templates import template
#######

import reflex as rx
import requests as rq
import re
from app_lasin.pages.LoginState import LoginState

#from fastapi import FastAPI

#app = FastAPI()

'''
@rx.get("/fast")
async def root():
    return {"message": "Hello World"}


'''

    #LoginState.estado=False
    #LoginState.error=True

#@rx.page(route="/login",title="login")
#@template(route="/cert", title="Certificados")
@template(route="/login",title="login")
def login()->rx.Component:
    return rx.vstack(
        rx.cond( ~LoginState.estado,         

            #return rx.section(
            rx.section(
                #rx.section(
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
                                icon="triangle_alert",
                                color_scheme="red",
                                role="alert",
                                style={"margin_top": "10px"}
                            ),
                        ),
                        on_submit=LoginState.loginService,
                        reset_on_submit=True,
                        width="90%",
                    ),
                    width="100%",
                    direction="column",
                    align="center",
                    justify="center",
                ),
                #style=style_section,
                justify="center",
                width="100%",
                
            #)
            )
        ),
        rx.cond( LoginState.estado,  
                
                rx.vstack(
                    
                    rx.dialog.root(
                        rx.dialog.trigger(rx.button("Revisar Mi Cuenta", size="4")),
                        rx.dialog.content(
                            rx.dialog.title("Guardar Cambios"),
                            rx.dialog.description(
                                "Change your profile details and preferences.",
                                size="2",
                                margin_bottom="16px",
                            ),
                            rx.flex(
                                rx.text(
                                    "Name",
                                    as_="div",
                                    size="2",
                                    margin_bottom="4px",
                                    weight="bold",
                                ),
                                rx.input(
                                    default_value=f"{LoginState.name}",
                                    placeholder="Enter your name",
                                ),
                                rx.text(
                                    "Email",
                                    as_="div",
                                    size="2",
                                    margin_bottom="4px",
                                    weight="bold",
                                ),
                                rx.input(
                                    default_value=f"{LoginState.email}",
                                    placeholder="Enter your email",
                                ),
                                direction="column",
                                spacing="3",
                            ),
                            rx.flex(
                                rx.dialog.close(
                                    rx.button(
                                        "Cancel",
                                        color_scheme="gray",
                                        variant="soft",
                                    ),
                                ),
                                rx.dialog.close(
                                    rx.button("Abandonar",on_click=LoginState.cerrar_sesion_dd),
                                ),
                                spacing="3",
                                margin_top="16px",
                                justify="end",
                            ),
                        ),
                    ),
                    #cerrar_sesion_user_dialogo_component(),
                    rx.text("soy un fantasma"),
                ),
                
        ),
        justify="center",
                width="100%",
                
    #)
    )


def field_form_component(label:str,placeholder:str,name_var:str,
                         on_change_function,type_field:str)->rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input.input(  #rx.input.input(
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


def cerrar_sesion_user_dialogo_component()->rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon('trash-2'))),
        rx.dialog.content(
            rx.dialog.title('Cerrar sesion'),
            rx.dialog.description('está seguro de salir de la cuenta de usuario: '+LoginState.name),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        'Cancelar',
                        color_scheme='gray',
                        variant='soft'
                    ),
                ),
                rx.dialog.close(
                    rx.button('Confirmar',on_click=LoginState.cerrar_sesion_dd),

                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            )
        )
    )