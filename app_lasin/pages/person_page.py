
import reflex as rx
from ..modelo.person_model import Persona
from ..servicio.person_service import select_all_person_service,select_person_by_ci_service,create_person_service,delete_person_service

from .notify import notify_component
import asyncio

class PersonState(rx.State):
    personas:list[Persona]
    persona_buscar:str
    error:str=''

    dict_a:dict={'Enero':'01','Febrero':'02','Marzo':'03','Abril':'04','Mayo':'05','Junio':'06','Julio':'07','Agosto':'08','Septiembre':'09','Octubre':'10','Noviembre':'11','Diciembre':'12'}

    
    def obtener_lista_meses(self):
        return self.dict_a.keys()
    
    def obt_nro_mes(self,mes:str):
        return self.dict_a.get(mes)
    
    
    @rx.background
    async def get_all_person(self):
        async with self:
            #print("***********************         user page             **************")
            self.personas=select_all_person_service()
    
    @rx.background
    async def get_person_by_ci(self):
        async with self:
            self.personas=select_person_by_ci_service(self.persona_buscar)

    def buscar_on_change(self,value:str):
        self.persona_buscar=value

    
    async def handlenotify(self):
        async with self:
            await asyncio.sleep(2)
            self.error=''

    @rx.background
    async def create_person(self,data:dict):
        async with self:
            try:
                #if data['password']==data['password_2']:
                fecha_nnn=costruir_fecha_nacimiento(data['fecha_a'],data['fecha_m'],data['fecha_d'])
                self.personas=create_person_service(ci=data['ci'],nombre=data['nombre'],paterno=data['paterno'],materno=data['materno'],sexo=data['sexo'],fecha_n=fecha_nnn)
            except BaseException as be:
                print(be.args)
                self.error=be.args
        await self.handlenotify()

    @rx.background
    async def delete_person_by_ci(self,ci):
        async with self:
            self.personas=delete_person_service(ci)

   
def costruir_fecha_nacimiento(anio:str,mes:str,dia:str):
        dict_a:dict={'Enero':'01','Febrero':'02','Marzo':'03','Abril':'04','Mayo':'05','Junio':'06','Julio':'07','Agosto':'08','Septiembre':'09','Octubre':'10','Noviembre':'11','Diciembre':'12'}
        mmm=dict_a.get(mes)
        #print(mmm)
        #print(anio+'-'+mmm+'-'+dia)
        return anio+'-'+mmm+'-'+dia

#@rx.page(route='/user', title='user',on_load=UserState.get_all_user)
def persona_page()-> rx.Component:
    return rx.flex(
        # datos de la pagina web  router_values(),
        rx.heading('personas',align='center'),
        rx.hstack(
            buscar_personas_component(),
            create_persona_dialogo_component(),
            justify='center',
            style={"width":"90vw","margin":"auto"}
        ),

        table_personas(PersonState.personas),
        rx.cond(
            PersonState.error!='',
            notify_component(PersonState.error,'shield-alert', 'yellow')
        ),
        direction='column',
        style={"width":"90vw","margin":"auto"},
        
    )


def table_personas(list_user: list[Persona])->rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell('ci'),
                rx.table.column_header_cell('nombre'),
                rx.table.column_header_cell('paterno'),
                rx.table.column_header_cell('pmaterno'),
                rx.table.column_header_cell('sexo'),
                rx.table.column_header_cell('fecha Nacimiento'),
                
                rx.table.column_header_cell('Accion')
            )
        ),
        rx.table.body(
            rx.foreach(list_user,row_table)
        )
    )


def row_table(persona:Persona):
    
    
    return rx.table.row(
        rx.table.cell(persona.ci),
        rx.table.cell(persona.nombre),
        rx.table.cell(persona.paterno),
        rx.table.cell(persona.materno),
        rx.table.cell(persona.sexo),
        rx.table.cell(persona.fecha_n),
        rx.table.cell(rx.hstack(
            #rx.button('eliminar')
            delete_person_dialogo_component(persona.ci)
            #delete_user_dialogo_component(user.username),
            #rx.button(rx.icon('pencil'))
        ))
    )

def buscar_personas_component()->rx.Component:
    return rx.hstack(
        rx.input(placeholder='Ingrese Cedula de Identidad',on_change=PersonState.buscar_on_change),
        rx.button('Buscar',on_click=PersonState.get_person_by_ci)
    )



def create_person_form() ->rx.Component:
    
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder='Cedula de Identidad',
                name="ci"
            ),
            rx.input(
                placeholder='Nombre',
                name="nombre"
            ),
            rx.input(
                placeholder='Apellido Paterno',
                name="paterno",
                #type='password'
            ),
            rx.input(
                placeholder='Apellido materno',
                name="materno",
                #type='password'
            ),
            rx.vstack(
                rx.text("Elija el Genero:"),
                rx.select(
                    ["Masculino", "Femenino", "sin especificar"],
                    default_value="Masculino",
                    name="sexo",
                ),
            ),
            rx.vstack(
                rx.text("Elija la fecha de nacimiento:"),
                rx.hstack(
                    rx.vstack(
                        rx.text("Año:"),
                        rx.select(
                            obtener_lista_años(),
                            default_value='2000',
                            name="fecha_a",
                        ),
                    ),
                    rx.vstack(
                        rx.text("Mes:"),
                        rx.select(
                            obtener_lista_meses(),
                            default_value='Julio',
                            name="fecha_m",
                        ),
                    ),
                    rx.vstack(
                        rx.text("Dia:"),
                        rx.select(
                            obtener_lista_dias(),
                            default_value='16',
                            name="fecha_d",
                        ),
                    ),
                    
                    
                ),
                
            ),
            
            rx.vstack(
                rx.text("Elija el Tipo de Usuario:"),
                rx.select(
                    ["Administrador", "Estudiante", "Docente","Persona"],
                    default_value="Persona",
                    name="tipo_u",
                ),
            ),
            
            
            rx.dialog.close(
                rx.button('Guardar', type='submit')
            ),

        ),
        on_submit=PersonState.create_person,
    )

def create_persona_dialogo_component()->rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button('Crear')),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title('Crear Persona'),
                create_person_form(),
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

def delete_person_dialogo_component(ci:str)->rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon('trash-2'))),
        rx.dialog.content(
            rx.dialog.title('Eliminar Persona'),
            rx.dialog.description('está seguro de querer eliminar a la persona '+ci),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        'Cancelar',
                        color_scheme='gray',
                        variant='soft'
                    ),
                ),
                rx.dialog.close(
                    rx.button('Confirmar',on_click=PersonState.delete_person_by_ci(ci)),

                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            )
        )
    )

def obtener_lista_años():
    lista_a=[]
    for i in range(1960,2020):
        #print(i)
        lista_a.append(str(i))
    return lista_a

def obtener_lista_meses():
    #mmm=PersonState.obtener_lista_meses()
    lista_a=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    
    #print(mmm)
    return lista_a


def obtener_lista_dias():
    lista=[]
    for i in range(1,10):
        #print(i)
        lista.append('0'+str(i))
    for i in range(10,32):
        #print(i)
        lista.append(str(i))
    #print(lista)
    return lista

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