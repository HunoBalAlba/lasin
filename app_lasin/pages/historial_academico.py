from app_lasin.templates import template

import reflex as rx
from app_lasin.pages.LoginState import LoginState


@template(route="/h_academico", title="Historial Academico")
def h_academico() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.cond(
            LoginState.is_estudent,
                rx.vstack(


                    rx.heading("Historial Academico", size="8"),
                    rx.text("Cursos Inscritos"),
                    rx.text(
                        "En esta pagina encontrara tus cursos inscritos como estudiante",
                        #rx.code("{your_app}/pages/ins.py"),
                    ),
                ),
        ),
        rx.cond(
            ~LoginState.is_estudent,
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
