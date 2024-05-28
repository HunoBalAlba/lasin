"""Common templates used between pages in the app."""

from __future__ import annotations

from app_lasin import styles
from app_lasin.components.sidebar import sidebar
from typing import Callable

import reflex as rx

# Meta tags for the app.
default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]


def menu_item_link(text, href):
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

    if True:
        return rx.hstack( 
            rx.card(
                rx.link(
                    rx.flex(
                        rx.avatar(src="/logo_i.png"),
                        rx.box(
                            rx.heading("LASIN"),
                            rx.text(
                                "Laboratorio Superior de Informática"
                            ),
                        ),
                        spacing="2",
                        
                    ),
                    #rx.button(
                   # "Edit Profile",
                   # color_scheme="indigo",
                    #variant="solid",
                #),
                ),
                as_child=True,
                position="fixed",
                            right="8em",
                            top="1em",
                            z_index="100",
            ),
           
                
                        #),
            
            menu_todos_los_items(),
        )
    else:
        return rx.hstack(
        cad_avatar(),
        menu_todos_los_items(),
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


def cad_avatar():
    return rx.box(           
            rx.card(
                rx.link(
                    rx.flex(
                    #rx.avatar(src="/logo_i.png"),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                               # rx.box(
                                    rx.chakra.avatar(
                                        rx.chakra.avatar_badge(
                                        box_size="1.25em",
                                        bg="green.500",
                                        border_color="green.500",
                                        ),
                                    name="Balvoa Albarracin",
                                    ),
                        #rx.spacer(),
                        #),
                                variant="ghost",
                            ),
                        ),
                        
                        rx.menu.content(
                    menu_item_link("Configuracion", "/"),
                    rx.menu.separator(),
                    menu_item_link("mis ultimas actividades", "/"),
                    menu_item_link("Cerrar Secion", "/login"),
                ),
                    ),
                                rx.box(
                                    rx.heading("Estudiante"),
                                    rx.text(
                                        "Hugo Balvoa Albarracin"
                                    ),
                                ),
                                spacing="2",
                    ),
                ),
                        as_child=True,
                        position="fixed",
                            right="8em",
                            top="1em",
                            z_index="100",
                        ),
                   
            #),
            
           
            #position="relative",

            #rx.text("Laboratorio\nsuperior\nde\nInformática\n",font_size="1em"),
                #rx.spacer(),
            position="fixed",
            right="10em",
            top="0.2em",
            z_index="100",
        ),




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
                    rx.menu.separator(),
                    #enlaces_contacto(),
                    menu_item_link("Iniciar Sesion", "/login"),
                    menu_item_link("Redes Sociales", "/redes_sociales"),
                ),
            ),
            position="fixed",
            right="2em",
            top="2em",
            z_index="500",
        

    )

