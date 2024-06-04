"""Welcome to Reflex!."""

# Import all the pages.

from app_lasin.pages.LoginState import LoginState
from app_lasin.pages import *
###### import page suarios
#from app_lasin.servicio import user_page
##########


import reflex as rx

#from app_lasin.pages.LoginState import LoginState

class State(rx.State):
    """Define empty state to allow access to rx.State.router."""
from app_lasin.pages.LoginState import LoginState
#print(type(LoginState))
#print(LoginState.get_name)
#print(LoginState.getEmail)
#print(LoginState.getTipoUsuario)



'''
lista_enlace_estudiante:list=["/cert"]
lista_enlace_docente:list=[]
lista_enlace_Administrador:list=["/usuarios","/cert","/ins"]
'''


'''
if  LoginState.getTipoUsuario=="e":
    from app_lasin.pages import login,index,apariencia
        
elif LoginState.getTipoUsuario=="a":
    from app_lasin.pages import *
        
elif LoginState.getTipoUsuario=="d":
    from app_lasin.pages import login,index,apariencia

else:
    from app_lasin.pages import *

'''
# Create the app.
app = rx.App()
