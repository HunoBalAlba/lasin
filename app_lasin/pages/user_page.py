
import reflex as rx
from ..modelo.user_model import User
from ..servicio.user_service import select_all_user_service,select_user_by_email_service

class UserState(rx.State):
    users:list[User]
    user_buscar:str

    @rx.background
    async def get_all_user(self):
        async with self:
            print("***********************         user page             **************")
            self.users=select_all_user_service()
    
    @rx.background
    async def get_user_by_email(self):
        async with self:
            self.users=select_user_by_email_service(self.user_buscar)

    def buscar_on_change(self,value:str):
        self.user_buscar=value





#@rx.page(route='/user', title='user',on_load=UserState.get_all_user)
def user_page()-> rx.Component:
    return rx.flex(
        rx.heading('Usuariosss',align='center'),
        rx.hstack(
            buscar_user_component(),
            justify='center',
            style={"width":"60vw","margin":"auto"}
        ),

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

def buscar_user_component()->rx.Component:
    return rx.hstack(
        rx.input(placeholder='Ingrese Email',on_change=UserState.buscar_on_change),
        rx.button('Buscar usuario',on_click=UserState.get_user_by_email)
    )