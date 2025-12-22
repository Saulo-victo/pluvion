def itenseidadePluviometrica(Bacia):
    itensidadePluviometrica = (923.08414*(Bacia.tempoRetorno**0.18146))/((Bacia.tempoConcentracao+11.92462)**0.75928)
    return itensidadePluviometrica
     

