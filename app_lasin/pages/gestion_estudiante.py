from app_lasin.templates import template

from app_lasin.conexiones import QueryPersonas
#from user_page import user_page
from ..modelo.user_model import User
from ..servicio.user_service import select_all

import reflex as rx
from app_lasin.pages.LoginState import LoginState


@template(route="/g_estudiantes", title="Gestion de Estudiantes")
def g_estudiantes() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.cond(
            LoginState.is_Administrador,
                rx.vstack(
                    rx.heading("Gestion de Estudiantes", size="8"),
                    rx.text(" crud "),
                    rx.text(
                        "En esta pagina podras adicionar nuevos Estudiantes y editar",
                        #rx.code("{your_app}/pages/ins.py"),
                        #mostrar_tabla_personas(),

                    #rx.code(),
                    #rx.code("app_lasin/pages/user_page.py"),
                ),

            
        
            ),
        ),
        rx.cond(
            ~LoginState.is_Administrador,
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
      
    )

