from app_lasin.templates import template

import reflex as rx
from app_lasin.pages.LoginState import LoginState


@template(route="/g_cert", title="Gestion de Certificados")
def g_cert() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.cond(
            es_administrador_o_estudiante(),
                rx.vstack(


                    rx.heading("Certificados", size="8"),
                    rx.text("Certificados"),
                    rx.text(
                        "En esta pagina encontrara Certificados de estudiantes",
                        #rx.code("{your_app}/pages/ins.py"),
                    ),
                ),
        ),
        rx.cond(
            ~es_administrador_o_estudiante(),
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
def es_administrador_o_estudiante():
    return (LoginState.is_Administrador | LoginState.is_estudent)