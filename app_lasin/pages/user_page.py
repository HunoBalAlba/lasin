
import reflex as rx
from ..modelo.user_model import User
from ..servicio.user_service import select_all

class UserState(rx.State):
    users:list[User]

    @rx.background
    async def get_all_user(self):
        async with self:
            print("***********************         user page             **************")
            self.users=select_all()
    

@rx.page(route='/user', title='user',on_load=UserState.get_all_user)
def user_page()-> rx.Component:
    return rx.flex(
        rx.heading('Usuariosss',align='center'),
        #rx.hstak(
        #)

        table_user(UserState.users),
        direction='column',
        style={"width":"60vw","margin":"auto"}
    )


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