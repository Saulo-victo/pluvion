from controllers.controllerHidrologico import CalcularBacia

class CalcularProjeto:
    def __init__(self, projeto):        
        for i in projeto.listaBacias:
            controllerHidrologico = CalcularBacia(i)
            

        
