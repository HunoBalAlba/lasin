from app_lasin.templates import template

from app_lasin.conexiones import QueryPersonas

import reflex as rx


@template(route="/ins", title="Inscripciones")
def ins() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Inscripciones", size="8"),
        rx.text("Inscripcion"),
        rx.text(
            "En esta pagina encontrara incripciones docentes y estudiantes ",
            #rx.code("{your_app}/pages/ins.py"),
            #mostrar_tabla_personas(),
        ),
        
    )

'''

def mostrar_tabla_personas():
    # Asegúrate de llamar primero a obtener_personas() para llenar el estado con los datos.
    columnas = ["ID", "Nombre", "Edad", "Carrera"]
    datos = [[persona.id, persona.ci, persona.nombre, persona.paterno] for persona in QueryPersonas.personas]

    return rx.data_table(
        columns=columnas,
        data=datos,
        pagination=True,  # Opcional, habilita la paginación.
        search=True,  # Opcional, habilita una barra de búsqueda.
        sort=True,  # Opcional, permite ordenar los datos.
    )
'''