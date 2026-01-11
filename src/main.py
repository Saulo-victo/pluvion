from controllers.controllerProjeto import CalcularProjeto
from core.models.bacia import Bacia
from core.models.projeto import Projeto
from storage.projetoJson import IoProjeto


projetoMaranguape = Projeto('Projeto Maranguape')



Bacia01 = Bacia(nome='Bacia do Maranguape', area=100, coefInfiltracao=1, tempoRetorno=15, compLinhaDagua=2, cotaMontante=15, cotaJusante=0)
Bacia02 = Bacia(nome='Bacia do Acarau', area=200, coefInfiltracao=2, tempoRetorno=30, compLinhaDagua=4, cotaMontante=30, cotaJusante=0)
Bacia03 = Bacia(nome='Bacia do Acarau', area=200, coefInfiltracao=2, tempoRetorno=30, compLinhaDagua=4, cotaMontante=30, cotaJusante=0)
Bacia04 = Bacia(nome='Bacia do Acarau', area=200, coefInfiltracao=2, tempoRetorno=30, compLinhaDagua=4, cotaMontante=30, cotaJusante=0)



projetoMaranguape.adicionarBacia(Bacia01)
projetoMaranguape.adicionarBacia(Bacia02)
projetoMaranguape.adicionarBacia(Bacia03)
projetoMaranguape.adicionarBacia(Bacia04)


calcularBacias = CalcularProjeto(projetoMaranguape)

operacaoProjeto = IoProjeto()

#operacaoProjeto.salvarProjeto(projetoMaranguape)

operacaoProjeto.abrirProjeto('Projeto Saulo')













