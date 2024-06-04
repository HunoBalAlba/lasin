from app_lasin.templates import template
from .user_page import user_page,UserState
from .person_page import PersonState,persona_page

import reflex as rx
from app_lasin.pages.LoginState import LoginState


@template(route="/g_usuarios", title="Gestion de usuarios",on_load=PersonState.get_all_person)
def g_usuarios() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.cond(
            LoginState.is_Administrador,
            rx.vstack(
                rx.heading("Seccion de Usuarios", size="8"),
                rx.text("Usuarios..."),
                rx.text(
                    "En esta pagina encontrara la administracion de los usuarios",
                    #rx.code("{your_app}/pages/ins.py"),
                    #mostrar_tabla_personas(),

                #rx.code(),
                #rx.code("app_lasin/pages/user_page.py"),
                
                ),
                #user_page()
                persona_page()
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
        #router_values(),
    )
#class RouterState(rx.State):
 #   pass


def router_values():
    return rx.chakra.table(
        headers=["Name", "Value"],
        rows=[
            [
                rx.text("router.page.host"),
                rx.code(UserState.router.page.host),
            ],
            [
                rx.text("router.page.path"),
                rx.code(UserState.router.page.path),
            ],
            [
                rx.text("router.page.raw_path"),
                rx.code(UserState.router.page.raw_path),
            ],
            [
                rx.text("router.page.full_path"),
                rx.code(UserState.router.page.full_path),
            ],
            [
                rx.text("router.page.full_raw_path"),
                rx.code(
                    UserState.router.page.full_raw_path
                ),
            ],
            [
                rx.text("router.page.params"),
                rx.code(
                    UserState.router.page.params.to_string()
                ),
            ],
            [
                rx.text("router.session.client_token"),
                rx.code(
                    UserState.router.session.client_token
                ),
            ],
            [
                rx.text("router.session.session_id"),
                rx.code(
                    UserState.router.session.session_id
                ),
            ],
            [
                rx.text("router.session.client_ip"),
                rx.code(
                    UserState.router.session.client_ip
                ),
            ],
            [
                rx.text("router.headers.host"),
                rx.code(UserState.router.headers.host),
            ],
            [
                rx.text("router.headers.user_agent"),
                rx.code(
                    UserState.router.headers.user_agent
                ),
            ],
            [
                rx.text("router.headers.to_string()"),
                rx.code(
                    UserState.router.headers.to_string()
                ),
            ],
        ],
        overflow_x="auto",
    )
