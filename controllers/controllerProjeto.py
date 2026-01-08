from controllers.controllerHidrologico import CalcularBacia
from core.models.projeto import Projeto

class CalcularProjeto:
    def __init__(self, projeto):        
        for i in projeto.listaBacias:
            controllerHidrologico = CalcularBacia(i)
            

        
