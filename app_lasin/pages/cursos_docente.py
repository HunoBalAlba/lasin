from app_lasin.templates import template

from app_lasin.conexiones import QueryPersonas
#from user_page import user_page
from ..modelo.user_model import User
from ..servicio.user_service import select_all

import reflex as rx
from app_lasin.pages.LoginState import LoginState


@template(route="/c_docente", title="Cursos a Cargo")
def c_docente() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.cond(
            LoginState.is_Docente,
                rx.vstack(
                    rx.heading("Cursos del Instructor", size="8"),
                    rx.text("una vez modificado la nota no podras editar, \nasegurese de colocar la note correctamente."),
                    rx.text(
                        "En esta pagina podras colocar la nota correspondiente al cada Curso",
                        #rx.code("{your_app}/pages/ins.py"),
                        #mostrar_tabla_personas(),

                    #rx.code(),
                    #rx.code("app_lasin/pages/user_page.py"),
                ),

            
        
            ),
        ),
        rx.cond(
            ~LoginState.is_Docente,
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

