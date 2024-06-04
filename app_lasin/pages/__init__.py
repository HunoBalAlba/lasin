#from .reportes import reportes
from .index import index
from .ins import ins
from .preins import preins
from .cursos_docente import c_docente

from .gestion_cert import g_cert
from .gestion_cursos import g_cursos
#from .gestion_docente import g_docentes
#from .gestion_estudiante import g_estudiantes
from .historial_academico import h_academico
from .apariencia import apariencia
from .redes_sociales import enlaces_contacto
from .gestion_usuarios import g_usuarios
from .login import login
from .mi_perfil import mi_perfil


'''

from .index import index
from .ins import ins
from .cert import cert
from .apariencia import apariencia
from .redes_sociales import enlaces_contacto

'''

#from .user_page import user_page
#from .usuarios import usuarios
'''
from app_lasin.pages.LoginState import LoginState
print(type(LoginState))
print(LoginState.get_name)
print(LoginState.getEmail)
print(LoginState.getTipoUsuario)

#if  LoginState.getTipoUsuario=="e":
if  True:
    from .index import index
    from .cert import cert
    from .apariencia import apariencia
    from .redes_sociales import enlaces_contacto
    from .login import login
        
elif LoginState.getTipoUsuario=="a":
    from .index import index
    from .ins import ins
    from .cert import cert
    from .apariencia import apariencia
    from .redes_sociales import enlaces_contacto
    from .usuarios import usuarios
    from .login import login

        
elif LoginState.getTipoUsuario=="d":
    from .index import index
    from .apariencia import apariencia
    from .redes_sociales import enlaces_contacto
    from .login import login

else:
    from .index import index
    from .apariencia import apariencia
    from .redes_sociales import enlaces_contacto
    from .login import login

   '''

##from .cerrrar_sesion import cerrar

#from .login import login

#from app_lasin.pages.LoginState import LoginState

#def cerrarSesion():
#if ~LoginState.getEstado :
    #from .login import login
    
        
        