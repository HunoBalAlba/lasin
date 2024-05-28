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
        router_values(),
    )
class RouterState(rx.State):
    pass


def router_values():
    return rx.chakra.table(
        headers=["Name", "Value"],
        rows=[
            [
                rx.text("router.page.host"),
                rx.code(RouterState.router.page.host),
            ],
            [
                rx.text("router.page.path"),
                rx.code(RouterState.router.page.path),
            ],
            [
                rx.text("router.page.raw_path"),
                rx.code(RouterState.router.page.raw_path),
            ],
            [
                rx.text("router.page.full_path"),
                rx.code(RouterState.router.page.full_path),
            ],
            [
                rx.text("router.page.full_raw_path"),
                rx.code(
                    RouterState.router.page.full_raw_path
                ),
            ],
            [
                rx.text("router.page.params"),
                rx.code(
                    RouterState.router.page.params.to_string()
                ),
            ],
            [
                rx.text("router.session.client_token"),
                rx.code(
                    RouterState.router.session.client_token
                ),
            ],
            [
                rx.text("router.session.session_id"),
                rx.code(
                    RouterState.router.session.session_id
                ),
            ],
            [
                rx.text("router.session.client_ip"),
                rx.code(
                    RouterState.router.session.client_ip
                ),
            ],
            [
                rx.text("router.headers.host"),
                rx.code(RouterState.router.headers.host),
            ],
            [
                rx.text("router.headers.user_agent"),
                rx.code(
                    RouterState.router.headers.user_agent
                ),
            ],
            [
                rx.text("router.headers.to_string()"),
                rx.code(
                    RouterState.router.headers.to_string()
                ),
            ],
        ],
        overflow_x="auto",
    )
