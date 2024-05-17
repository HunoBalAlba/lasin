from app_lasin.templates import template

import reflex as rx


@template(route="/cert", title="Certificados")
def cert() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Certificados", size="8"),
        rx.text("Certificados"),
        rx.text(
            "En esta pagina encontrara Certificados de estudiantes",
            #rx.code("{your_app}/pages/ins.py"),
        ),
    )