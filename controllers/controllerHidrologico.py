from core.calculos import itensidadePluviometrica
from core.calculos import tempoConcetracao
from core.calculos import vazaoProjeto
from core.models import bacia

class HidrologiaController:
    def __init__(self, bacia):
        bacia.itensidadePluviometrica = itensidadePluviometrica(bacia)
        bacia.vazaoProjeto = vazaoProjeto(bacia)
        bacia.tempoConcentracao = tempoConcetracao(bacia)