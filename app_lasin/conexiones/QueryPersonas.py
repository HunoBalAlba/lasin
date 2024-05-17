'''from app_lasin.modelos import Persona

import reflex as rx


class QueryPersonas(rx.State):
    personas: list[Persona.Persona] = []

    def obtener_personas(self):
        with rx.session() as session:
            self.personas = session.exec(Persona.select()).all()
''' 