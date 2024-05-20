from app_lasin.templates import template


import reflex as rx



@template(route="/usuarios", title="usuarios")
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
        
    )

