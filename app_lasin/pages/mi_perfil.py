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
#ruta:str="login"
#i#f LoginState.estado:
  #  ruta="Ver Sesion"
#else:
    #~LoginState.estado,
 #   ruta="login"

    
   
@template(route="/mi_perfil",title="Mi perfil")
def mi_perfil()->rx.Component:
    return rx.vstack(
        rx.cond( LoginState.estado,  
                
                rx.vstack(
                    
                    rx.dialog.root(
                        rx.dialog.trigger(rx.button("Guardar Cambios", size="4")),
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
                    rx.text("Datos Generales",size="4",font_weight="bold"),
                    rx.text(f"Nombre: {LoginState.name}"),
                    rx.text(f"Correo electronico: {LoginState.username}"),
                    
                ),
                
        ),
        rx.cond( ~LoginState.estado, 
                rx.hstack(
                rx.heading("\n\n404", size="8"),
                rx.text("   "),
                rx.text(
                    "No se ha encontrado la pagina",
                ),
                #align="center",
                position= "absolute",
                top= "50%",
                left= "50%",
            ), 
        ),
        justify="center",
                width="100%",
                
    #)
    )
