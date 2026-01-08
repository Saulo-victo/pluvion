from core.calculos.itensidadePluviometrica import itensidadePluviometrica
from core.calculos.tempoConcetracao import tempoConcetracao
from core.calculos.vazaoProjeto import vazaoProjeto

class ControllerBacia:
    def __init__(self, bacia):
        bacia.tempoConcentracao = tempoConcetracao(bacia)
        bacia.itensidadePluviometrica = itensidadePluviometrica(bacia)
        bacia.vazaoProjeto = vazaoProjeto(bacia)
        