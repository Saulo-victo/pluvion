import json
from pathlib import Path
from typing import TypedDict
from core.models.projeto import Projeto
from core.models.bacia import Bacia

class TipagemProjeto(TypedDict):
    nome: str
    bacias: list[dict]

class IoProjeto:
    def __init__(self):
        self.pastaProjetos = Path("projects").absolute()       

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
        self.caminhoProjeto = self.pastaProjetos / arquivo
        with open(self.caminhoProjeto, 'w') as arquivo:
            json.dump(projetoJson, arquivo, ensure_ascii=False, indent=2)


    def abrirProjeto(self, nomeDoArquivo):          
        arquivo = nomeDoArquivo.replace(' ', '') + '.json'  
        print(arquivo)              
        self.caminhoProjeto = self.pastaProjetos / arquivo
        print(self.caminhoProjeto)
        with open(self.caminhoProjeto, 'r') as projetoSalvo:
            projetoJson = json.load(projetoSalvo)

        projeto = Projeto(projetoJson['nome'])
        for i in projeto.listaBacias:
            print(i.nome)
        '''listaBacias = projetoJson['bacias']
        for i in listaBacias:
            print(i['nome'])'''







        