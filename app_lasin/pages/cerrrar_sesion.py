"""The home page of the app."""

from app_lasin import styles
from app_lasin.templates import template

import reflex as rx

from app_lasin.pages.LoginState import LoginState
#@template(route="/", title="Home", image="/github.svg")
@template(route="/cerrar", title="cerrar")
def cerrar() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    #LoginState.cerrar_sesion_dd()
    #return rx.redirect("/login")
    

    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
        #return rx.redirect("/login")
        LoginState.cerrar_sesion_dd()
    return rx.markdown(content, component_map=styles.markdown_style)
    

'''
def Cerrar_cuenta_dialogo_component(username:str)->rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon('trash-2'))),
        rx.dialog.content(
            rx.dialog.title('Eliminar Usuario'),
            rx.dialog.description('está seguro de querer eliminar el usuario'+username),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        'Cancelar',
                        color_scheme='gray',
                        variant='soft'
                    ),
                ),
                rx.dialog.close(
                    rx.button('Confirmar',on_click=UserState.delete_user_by_email(username)),

                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            )
        )
    )
'''

