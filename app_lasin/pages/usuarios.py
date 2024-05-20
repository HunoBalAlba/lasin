from app_lasin.templates import template
from .user_page import user_page,UserState

import reflex as rx



@template(route="/usuarios", title="usuarios",on_load=UserState.get_all_user)
def usuarios() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Seccion de Usuarios", size="8"),
        rx.text("Usuarios..."),
        rx.text(
            "En esta pagina encontrara la administracion de los usuarios",
            #rx.code("{your_app}/pages/ins.py"),
            #mostrar_tabla_personas(),

          #rx.code(),
          #rx.code("app_lasin/pages/user_page.py"),
        
        ),
        user_page()
        
    )

