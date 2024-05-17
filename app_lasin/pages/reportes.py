"""The dashboard page."""

from app_lasin.templates import template

import reflex as rx


@template(route="/reportes", title="Reportes")
def reportes() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("REPORTES", size="8"),
        rx.text("Reporte de Semanal"),
        rx.text(
            "En esta pagina encontrara los ultimos reportes ",
            #rx.code("{your_app}/pages/dashboard.py"),
        ),
    )
