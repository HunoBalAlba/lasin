"""Common templates used between pages in the app."""

from __future__ import annotations

from app_lasin import styles
from app_lasin.components.sidebar import sidebar
from typing import Callable

#from app_lasin.pages.login import  LoginState
from app_lasin.pages.LoginState import LoginState


import reflex as rx

# Meta tags for the app.
default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]

import app_lasin.pages.restriccion as res

def menu_item_link(text, href):
    

    return rx.box(
        excluir_paginas_segun_rol(text, href),
        width="100%",
    ),
    #return menu_item_enlace(text, href)

def excluir_paginas_segun_rol(text, href):
    
    #print(f"pagina:  {text}   enlace: {href}")
    return rx.box(
            rx.cond(
            href in res.lista_enlace_estudiante and LoginState.getTipoUsuario=='e',
            #print(f"pagina:  {text}   enlace: {href}"),
            menu_item_enlace(text, href),
        ),
        rx.cond(
            href in res.lista_enlace_Administrador and LoginState.getTipoUsuario=='a',
            #print(f"pagina:  {text}   enlace: {href}"),
            menu_item_enlace(text, href),
        ),
        rx.cond(
            href in res.lista_enlace_docente and LoginState.getTipoUsuario=='d',
            #print(f"pagina:  {text}   enlace: {href}"),
            menu_item_enlace(text, href),
        ),
        rx.cond(
            href in res.lista_enlace_publico and LoginState.getTipoUsuario=='p',
            #print(f"pagina:  {text}   enlace: {href}"),
            menu_item_enlace(text, href),
        ),
        

    )


def menu_item_enlace(text, href):
    return rx.menu.item(
        rx.link(
            text,
            href=href,
            
            width="100%",
            color="inherit",
        ),
        _hover={
            "color": styles.accent_color,
            "background_color": styles.accent_text_color,
        },
        
    )

class MouseMove(rx.State):
    text = "L A S I N"
    #size="lg"

    def change_text(self):
        if self.text == "Laboratorio\nsuperior\nde\nInformática\n":
            self.text = "L A S I N"
        else:
            self.text = "Laboratorio\nsuperior\nde\nInformática\n"



def menu_button() -> rx.Component:

    
    """The menu button on the top right of the page.

    Returns:
        The menu button component.
    """
    from reflex.page import get_decorated_pages

    return rx.vstack(
        rx.cond(
            ~LoginState.getEstado,
            rx.hstack( 
                rx.card(
                    #rx.link(
                        rx.flex(
                            rx.hstack(
                                rx.avatar(src="/logo_i.png",size="5"),
                                rx.box(
                                    rx.text("L A S I N", weight="bold", size="4",as_="div"),
                                    rx.text("Laboratorio Superior de Informática",size="1"),
                                    #rx.heading("L A S I N"),
                                    #rx.text( "Laboratorio Superior de Informática"),
                                ),
                                spacing="1",
                            )
                        ),
                        #rx.button(
                    # "Edit Profile",
                    # color_scheme="indigo",
                        #variant="solid",
                    #),
                    #),
                    as_child=True,
                    position="fixed",
                                right="5.2em",
                                top="0.2em",
                                z_index="100",
                ),
            
                    
                            #),
                
                menu_todos_los_items(),
            ),
        ),
        rx.cond(
            LoginState.getEstado,
                rx.hstack(
                    #cad_avatar(),
                    opciones_menu_usuario_avatar(),
                    menu_todos_los_items(),
                ),
                
            #LoginState.getEstado & ~LoginState.getError,
            
                #
        ),
    )
        



class ThemeState(rx.State):
    """The state for the theme of the app."""

    accent_color: str = "crimson"

    gray_color: str = "gray"


def template(
    route: str | None = None,
    title: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.event.EventHandler | list[rx.event.EventHandler] | None = None,
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    """The template for each page of the app.

    Args:
        route: The route to reach the page.
        title: The title of the page.
        description: The description of the page.
        meta: Additionnal meta to add to the page.
        on_load: The event handler(s) called when the page load.
        script_tags: Scripts to attach to the page.

    Returns:
        The template with the page content.
    """

    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        """The template for each page of the app.

        Args:
            page_content: The content of the page.

        Returns:
            The template with the page content.
        """
        # Get the meta tags for the page.
        all_meta = [*default_meta, *(meta or [])]

        def templated_page():
            return rx.hstack(
                sidebar(),
                rx.box(
                    rx.vstack(
                        page_content(),
                        rx.spacer(),
                        rx.logo(),
                        **styles.template_content_style,
                    ),
                    **styles.template_page_style,
                ),
                menu_button(),
                align="start",
                background=f"radial-gradient(circle at top right, {rx.color('accent', 2)}, {rx.color('mauve', 1)});",
                position="relative",
            )

        @rx.page(
            route=route,
            title=title,
            description=description,
            meta=all_meta,
            script_tags=script_tags,
            on_load=on_load,
        )
        def theme_wrap():
            return rx.theme(
                templated_page(),
                has_background=True,
                accent_color=ThemeState.accent_color,
                gray_color=ThemeState.gray_color,
            )

        return theme_wrap

    return decorator

def colocar_avatar_editar_perfil():
    return rx.flex(
    rx.avatar(src="/logo.jpg", fallback="RU", size="9"),
    rx.text("Reflex User", weight="bold", size="4"),
    rx.text("@reflexuser", color_scheme="gray"),
    rx.button(
        "Edit Profile",
        color_scheme="indigo",
        variant="solid",
    ),
    direction="column",
    spacing="1",
)




def menu_todos_los_items():
    from reflex.page import get_decorated_pages

    return rx.box(
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.icon("menu"),
                        variant="soft",
                    )
                ),
                
                #rx.menu.separator(),
                rx.menu.content(
                    
                    *[
                        menu_item_link(page["title"], page["route"])
                        for page in get_decorated_pages()
                    ],
                    #rx.menu.separator(),
                    #rx.link(rx.button("Redes Sociales"),color_scheme="mint", href="/redes_sociales") ,                   
                    
                    rx.menu.separator(),
                    
                    cerrar_sesion_cuadro_dialogo(),
                    
                ),
            ),
            #position="fixed",
            position="fixed",
            
            right="2em",
            top="2em",
            z_index="998",
        

    )


       

def cerrar_sesion_cuadro_dialogo():
    return rx.vstack(
        #rx.menu.separator(),
        rx.cond(LoginState.estado,
            rx.dialog.root(
                rx.dialog.trigger(rx.button("Cerrar Sesión", size="2")),
                rx.dialog.content(
                    rx.dialog.title("Cerrar Sesión"),
                    rx.dialog.description(
                        "Guarde los Cambios de su trabajo antes de salir",
                        size="2",
                        margin_bottom="16px",
                    ),
                    
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
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
            )
        ),
        rx.cond(~LoginState.estado,
            rx.link(rx.button("Iniciar Sesión"), href="/login") ,    
            
        )
    )

    



def opciones_menu_usuario_avatar():
    return rx.box(           
            rx.card(
                rx.flex(
                    rx.hstack(
                        rx.vstack(
                            rx.chakra.avatar(
                                rx.chakra.avatar_badge(
                                    box_size="1.25em",
                                    bg="green.500",
                                    border_color="green.500",
                                    
                                ),
                                name=f"{LoginState.getName}",
                                size="lg",
                            ),
                           
                        ),
                        
                        rx.vstack(
                            #rx.vstack(
                                #rx.text(f"{LoginState.obtener_tipo_usuario}"),
                                rx.text(f"{LoginState.getName}", weight="bold", size="2"),
                                rx.text(f"{LoginState.getEmail}", color_scheme="gray",size="1"),
                            #),
                            rx.hstack(
                                #rx.text(f"{LoginState.getEmail}", color_scheme="gray",size="1"),
                                rx.text(f"{LoginState.obtener_tipo_usuario}",size="2"),
                                rx.menu.root(
                                    rx.menu.trigger(
                                        rx.button(
                                            "Opciones", variant="soft", size="1"
                                        ),
                                    ),
                                    rx.menu.content(
                                        rx.menu.item("Editar Perfil"),
                                        rx.menu.item("Subir foto de perfil"),
                                        rx.menu.separator(),
                                        rx.menu.item("Cambiar Contraseña"),
                                        rx.menu.separator(),
                                        rx.menu.item(
                                            "Hoja de vida", color="red"
                                        ),
                                        rx.menu.separator(),
                                        cerrar_sesion_cuadro_dialogo(),
                                    ),
                                    #on_open_change=DropdownMenuState.count_opens,
                                ),
                            ),
                            #rx.text(f"{LoginState.getTipo_usuario_cadena}"),
                            direction="column",
                            spacing="1",                            
                        ),
                            
                    ),
                    
                ),
            ),
            position="fixed",
            right="5.2em",
            top="0.2em",
            z_index="100",
    )