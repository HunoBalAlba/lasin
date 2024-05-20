#logica de negocio validadciones

from ..repositorio.user_repository import select_all

def select_all_user_service():
    print("***********************         user ---service----             **************")
    users= select_all()
    print (users)
    return users
