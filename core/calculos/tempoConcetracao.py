def tempoConcetracao(Bacia):
    tempoConcetracao = (57)*(((Bacia.compLinhaDagua**3)/Bacia.desnivel)**0.385)
    return tempoConcetracao
    
    

