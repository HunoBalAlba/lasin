"""Sidebar component for the app."""

from app_lasin import styles

import reflex as rx


def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.hstack(
        # The logo.
        rx.color_mode_cond(
            rx.image(src="/logo_i.png", height="8em"),
            rx.image(src="/logo_i.png", height="8em"),
        ),
        rx.spacer(),
        #rx.text("Laboratorio\nsuperior\nde\nInformática"),
        rx.link(
            rx.button(
                #rx.icon("messages-square"),
                rx.icon("messages-square"),
                color_scheme="gray",
                variant="soft",
            ),
            href="https://bit.ly/LASIN-UMSA ",
        ),
        align="center",
        width="100%",
        border_bottom=styles.border,
        padding_x="1em",
        padding_y="0.1em", ##padding_y="2em",
    )


def sidebar_footer() -> rx.Component:
    """Sidebar footer.

    Returns:
        The sidebar footer component.
    """
    return rx.hstack(
        rx.spacer(),
        rx.link(
            rx.text("Carrera de Informatica"),
            href="http://informatica.umsa.bo/",
            color_scheme="gray",
        ),
        rx.link(
            rx.text("Lasin"),
            href="http://informatica.umsa.bo/",
            color_scheme="gray",
        ),
        width="100%",
        border_top=styles.border,
        padding="1em",
    )

from app_lasin.pages.LoginState import LoginState

import app_lasin.pages.restriccion as res

def sidebar_item(text: str, url: str) -> rx.Component:
     return excluir_paginas_segun_rol_sidebar(text, url)
    #return menu_item_enlace(text, href)

def excluir_paginas_segun_rol_sidebar(text, href):
    
    #print(f"pagina:  {text}   enlace: {href}")
    return rx.vstack(
        rx.cond(
            href in res.lista_enlace_estudiante and LoginState.getTipoUsuario=="e",
            #print(f"pagina:  {text}   enlace: {href}"),
            menu_modificado_sidebar_item(text, href),
        ),
        rx.cond(
            href in res.lista_enlace_Administrador and LoginState.getTipoUsuario=="a",
            #print(f"pagina:  {text}   enlace: {href}"),
            menu_modificado_sidebar_item(text, href),
        ),
        rx.cond(
            href in res.lista_enlace_docente and LoginState.getTipoUsuario=="d",
            #print(f"pagina:  {text}   enlace: {href}"),
            menu_modificado_sidebar_item(text, href),
        ),
        rx.cond(
            href in res.lista_enlace_publico and LoginState.getTipoUsuario=="p",
            #print(f"pagina:  {text}   enlace: {href}"),
            menu_modificado_sidebar_item(text, href),
        ),
        
        width="100%",

    )

def menu_modificado_sidebar_item(text: str, url: str) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (rx.State.router.page.path == url.lower()) | (
        (rx.State.router.page.path == "/") & text == "Home"
    )
    #print(active)

    return rx.link(
        rx.hstack(
            rx.text(
                text,
            ),
            bg=rx.cond(
                active,
                rx.color("accent", 2),
                "transparent",
            ),
            border=rx.cond(
                active,
                f"1px solid {rx.color('accent', 6)}",
                f"1px solid {rx.color('gray', 6)}",
            ),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            align="center",
            border_radius=styles.border_radius,
            width="100%",
            padding="1em",
        ),
        href=url,
        width="100%",
    ) 

def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    # Get all the decorated pages and add them to the sidebar.
    from reflex.page import get_decorated_pages

    return rx.box(
        rx.vstack(
            sidebar_header(),
            rx.vstack(
                *[
                    sidebar_item(
                        
                            text=page.get("title", page["route"].strip("/").capitalize()),
                            url=page["route"],
                    )
                    for page in get_decorated_pages() 
                ],
                width="100%",
                overflow_y="auto",
                align_items="flex-start",
                padding="1em",
            ),
            rx.spacer(),
            sidebar_footer(),
            height="100dvh",
        ),
        display=["none", "none", "block"],
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        border_right=styles.border,
    )
