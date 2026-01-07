class Bacia:
    def __init__(self, nome: str, area: float, coefInfiltracao: float, tempoRetorno:float, compLinhaDagua:float, cotaMontante:float, cotaJusante:float):
        
        if not nome.strip():
            raise ValueError('O campo nome deve ser preenchido')
        else:
            self.nome = nome      

        if isinstance(cotaJusante, str):
            raise ValueError("A cota de jusante deve ser um número") 
        else:
            self.cotaJusante = cotaJusante

        if isinstance(cotaMontante, str):
            raise ValueError("A cota de montante deve ser um número")    
        else:
            self.cotaMontante = cotaMontante

        if self.cotaMontante - self.cotaJusante < 0:
            raise ValueError('Cota de montante superior a cota de jusante')              
        else:            
            self.desnivel = self.cotaMontante - self.cotaJusante  

        if not isinstance(compLinhaDagua, str) and compLinhaDagua > 0:
            self.compLinhaDagua = compLinhaDagua
        else:
            raise ValueError("O comprimento da linha dágua deve ser maior do que zero e do tipo decimal") 

        if not isinstance(area, str) and area > 0:
            self.area = area
        else:
            raise ValueError("A área da Bacia deve ser maior do que zero e do tipo decimal")     

        if not isinstance(coefInfiltracao, str) and coefInfiltracao > 0:
            self.coefInfiltracao = coefInfiltracao
        else:
            raise ValueError("O coeficiente de infiltração deve ser maior do que zero e do tipo decimal")          

        if not isinstance(tempoRetorno, str) and tempoRetorno > 0:
            self.tempoRetorno = tempoRetorno
        else:
            raise ValueError("O tempo de retorno deve ser maior do que zero e do tipo decimal")    
                
        #Resultado hidrológico
        self.vazaoProjeto = None
        self.tempoConcentracao = None
        self.itensidadePluviometrica = None  

B1 = Bacia('2', 12, 2, 15, 152, 50, 30)

    








