from controllers.controllerHidrologico import ControllerBacia
from core.models.bacia import Bacia

bacia_teste = Bacia('Bacia do Maranguape', 2808227.33, 0.3, 15, 2.617, 17.488, 0)
bacia_controller = ControllerBacia(bacia_teste)

print(bacia_teste.nome)
print(bacia_teste.area)
print(bacia_teste.coefInfiltracao)
print(bacia_teste.cotaJusante)
print(bacia_teste.cotaMontante)
print(bacia_teste.tempoRetorno)
print(bacia_teste.compLinhaDagua)
print(bacia_teste.desnivel)
print(bacia_teste.itensidadePluviometrica)
print(bacia_teste.vazaoProjeto)
print(bacia_teste.tempoConcentracao)



