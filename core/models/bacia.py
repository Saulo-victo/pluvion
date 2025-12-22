class Bacia:
    def __init__(self, nome: str, area: float, coefInfiltracao: float, tempoRetorno:float, compLinhaDagua:float, cotaMontante:float, cotaJusante:float):
        #Identificação
        self.nome = nome

        #Dados físicos
        self.cotaMontante = cotaMontante
        self.cotaJusante = cotaJusante
        if self.cotaMontante - self.cotaJusante > 0:
            self.desnivel = self.cotaMontante - self.cotaJusante
        else:
            raise ValueError('Cota de montante superior a cota de jusante')  

        self.compLinhaDagua = compLinhaDagua
        self.area = area
        #Parâmetro de projeto
        self.coefInfiltracao = coefInfiltracao     
        self.tempoRetorno = tempoRetorno        
        
        #Resultado hidrológico
        self.vazaoProjeto = None
        self.tempoConcetracao = None
        self.itenseidadePluviometrica = None  
        

    
    def itenseidadePluviometrica(self):
        self.itenseidadePluviometrica = (923.08414*(self.tempoRetorno**0.18146))/((self.tempoConcetracao+11.92462)**0.75928)
        return self.itenseidadePluviometrica
    
    def vazaoProjeto(self):
        self.vazaoProjeto = self.area * self.coefInfiltracao * self.itenseidadePluviometrica
        return self.vazaoProjeto
    






