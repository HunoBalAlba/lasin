"""Welcome to Reflex!."""

# Import all the pages.
from app_lasin.pages import *
###### import page suarios
#from app_lasin.servicio import user_page
##########


import reflex as rx

#from app_lasin.pages.LoginState import LoginState

class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App()
