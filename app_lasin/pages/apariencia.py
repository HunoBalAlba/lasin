"""The settings page."""

from app_lasin.templates import ThemeState, template

import reflex as rx


@template(route="/apariencia", title="Apariencia")
def apariencia() -> rx.Component:
    """The settings page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("Apariencia", size="8"),
        rx.hstack(
            rx.text("Modo Oscuro: "),
            rx.color_mode.switch(),
        ),
        rx.hstack(
            rx.text("Color Claro: "),
            rx.select(
                [
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
                value=ThemeState.accent_color,
                on_change=ThemeState.set_accent_color,
            ),
        ),
        rx.text(
            "Elija el tema que mejor vea conveniente ",
            #"You can edit this page in ",
            #rx.code("{your_app}/pages/settings.py"),
            size="1",
        ),
    )
