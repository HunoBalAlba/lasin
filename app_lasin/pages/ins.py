from app_lasin.templates import template

from app_lasin.conexiones import QueryPersonas
#from user_page import user_page
from ..modelo.user_model import User
from ..servicio.user_service import select_all

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

          #rx.code(),
          #rx.code("app_lasin/pages/user_page.py"),
    
        ),
        
    )


'''

def user_page()-> rx.Component:
    return rx.flex(
        rx.heading('Usuariosss',align='center'),
        #rx.hstak(
        #)

        table_user(UserState.users),
        direction='column',
        style={"width":"60vw","margin":"auto"}
    )
'''
'''
def table_user(list_user: list[User])->rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell('nombre'),
                rx.table.column_header_cell('nombre usua'),
                rx.table.column_header_cell('password'),
                rx.table.column_header_cell('Accion')
            )
        ),
        rx.table.body(
            rx.foreach(list_user,row_table)
        )
    )


def row_table(user:User):
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.username),
        rx.table.cell(user.password),
        rx.table.cell(rx.hstack(
            rx.button('eliminar')
            #delete_user_dialogo_component(user.username),
            #rx.button(rx.icon('pencil'))
        ))
    )
'''

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