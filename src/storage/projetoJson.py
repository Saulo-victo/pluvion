import json
from pathlib import Path
from typing import TypedDict



class TipagemProjeto(TypedDict):
    nome: str
    bacias: list[dict]

class IoProjeto:
    def __init__(self):
        self.CAMINHO_PROJETO = Path("projects").absolute()        

    def salvarProjeto(self, projeto):        
        listaBacias = []
        for i in projeto.listaBacias:
            bacia = {
                "nome": i.nome,
                "area": i.area,
                "coeficiente_infiltracao": i.coefInfiltracao,
                "tempo_retorno": i.tempoRetorno,
                "comprimento_linhaDagua": i.compLinhaDagua,
                "cota_montante": i.cotaMontante,
                "cota_jusante": i.cotaJusante,
                "vazao_projeto": i.vazaoProjeto,
                "tempo_concentracao": i.tempoConcentracao,
                "itensidade_pluviometrica": i.itensidadePluviometrica,

            }
            listaBacias.append(bacia)

        projetoJson: IoProjeto = {
            "nome": projeto.nome,
            "bacias": listaBacias
        }              
        arquivo = projeto.nome.replace(' ', '') + '.json'
        self.CAMINHO_PROJETO = self.CAMINHO_PROJETO / arquivo
        with open(self.CAMINHO_PROJETO, 'w') as arquivo:
            json.dump(projetoJson, arquivo, ensure_ascii=False, indent=2)






        