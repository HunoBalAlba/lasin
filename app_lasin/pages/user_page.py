
import reflex as rx
from ..modelo.user_model import User
from ..servicio.user_service import select_all_user_service,select_user_by_email_service,create_user_service,delete_user_service

from .notify import notify_component
import asyncio

class UserState(rx.State):
    users:list[User]
    user_buscar:str
    error:str=''

    @rx.background
    async def get_all_user(self):
        async with self:
            #print("***********************         user page             **************")
            self.users=select_all_user_service()
    
    @rx.background
    async def get_user_by_email(self):
        async with self:
            self.users=select_user_by_email_service(self.user_buscar)

    def buscar_on_change(self,value:str):
        self.user_buscar=value

    
    async def handlenotify(self):
        async with self:
            await asyncio.sleep(2)
            self.error=''

    @rx.background
    async def create_user(self,data:dict):
        async with self:
            try:
                self.users=create_user_service(username=data['username'],password=data['password'],phone=data['phone'],name=data['name'])
            except BaseException as be:
                print(be.args)
                self.error=be.args
        await self.handlenotify()

    @rx.background
    async def delete_user_by_email(self,email):
        async with self:
            self.users=delete_user_service(email)



#@rx.page(route='/user', title='user',on_load=UserState.get_all_user)
def user_page()-> rx.Component:
    return rx.flex(
        # datos de la pagina web  router_values(),
        rx.heading('Usuariosss',align='center'),
        rx.hstack(
            buscar_user_component(),
            create_user_dialogo_component(),
            justify='center',
            style={"width":"60vw","margin":"auto"}
        ),

        table_user(UserState.users),
        rx.cond(
            UserState.error!='',
            notify_component(UserState.error,'shield-alert', 'yellow')
        ),
        direction='column',
        style={"width":"60vw","margin":"auto"},
        
    )


def table_user(list_user: list[User])->rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell('nombre'),
                rx.table.column_header_cell('nombre usuaario'),
                rx.table.column_header_cell('Telefono'),
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
        rx.table.cell(user.phone),
        rx.table.cell(rx.hstack(
            #rx.button('eliminar')
            delete_user_dialogo_component(user.username)
            #delete_user_dialogo_component(user.username),
            #rx.button(rx.icon('pencil'))
        ))
    )

def buscar_user_component()->rx.Component:
    return rx.hstack(
        rx.input(placeholder='Ingrese Email',on_change=UserState.buscar_on_change),
        rx.button('Buscar usuario',on_click=UserState.get_user_by_email)
    )



def create_user_form() ->rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder='Nombre',
                name="name"
            ),
            rx.input(
                placeholder='Email',
                name="username"
            ),
            rx.input(
                placeholder='Contraseña',
                name="password",
                type='password'
            ),
            rx.input(
                placeholder='Telefono',
                name="phone"
            ),
            rx.dialog.close(
                rx.button('Guardar', type='submit')
            ),

        ),
        on_submit=UserState.create_user,
    )

def create_user_dialogo_component()->rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button('Crear usuario')),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title('Crear usuarioooo'),
                create_user_form(),
                justify='center',
                align='center',
                direction='column',
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button('cancelar',color_scheme='gray',variant='soft')
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            style={'width':'300px'}
        ),
    )

def delete_user_dialogo_component(username:str)->rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon('trash-2'))),
        rx.dialog.content(
            rx.dialog.title('Eliminar Usuario'),
            rx.dialog.description('está seguro de querer eliminar el usuario'+username),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        'Cancelar',
                        color_scheme='gray',
                        variant='soft'
                    ),
                ),
                rx.dialog.close(
                    rx.button('Confirmar',on_click=UserState.delete_user_by_email(username)),

                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            )
        )
    )



'''

def router_values():
    return rx.chakra.table(
        headers=["Name", "Value"],
        rows=[
            [
                rx.text("router.page.host"),
                rx.code(UserState.router.page.host),
            ],
            [
                rx.text("router.page.path"),
                rx.code(UserState.router.page.path),
            ],
            [
                rx.text("router.page.raw_path"),
                rx.code(UserState.router.page.raw_path),
            ],
            [
                rx.text("router.page.full_path"),
                rx.code(UserState.router.page.full_path),
            ],
            [
                rx.text("router.page.full_raw_path"),
                rx.code(
                    UserState.router.page.full_raw_path
                ),
            ],
            [
                rx.text("router.page.params"),
                rx.code(
                    UserState.router.page.params.to_string()
                ),
            ],
            [
                rx.text("router.session.client_token"),
                rx.code(
                    UserState.router.session.client_token
                ),
            ],
            [
                rx.text("router.session.session_id"),
                rx.code(
                    UserState.router.session.session_id
                ),
            ],
            [
                rx.text("router.session.client_ip"),
                rx.code(
                    UserState.router.session.client_ip
                ),
            ],
            [
                rx.text("router.headers.host"),
                rx.code(UserState.router.headers.host),
            ],
            [
                rx.text("router.headers.user_agent"),
                rx.code(
                    UserState.router.headers.user_agent
                ),
            ],
            [
                rx.text("router.headers.to_string()"),
                rx.code(
                    UserState.router.headers.to_string()
                ),
            ],
        ],
        overflow_x="auto",
    )
'''