🌧️ Pluvion

Pluvion é uma ferramenta computacional voltada ao cálculo hidrológico aplicado a projetos de drenagem, com foco no processamento confiável de dados de bacias hidrográficas e na obtenção de parâmetros fundamentais de projeto, como tempo de concentração, intensidade de chuva e vazão de pico.

O projeto nasce com uma abordagem engenharia-first: o motor hidrológico é desenvolvido de forma independente da interface gráfica, garantindo rigor técnico, testabilidade e evolução sustentável.

🎯 Objetivo do Projeto

Desenvolver um motor hidrológico sólido e confiável, capaz de:

Processar dados físicos da bacia hidrográfica

Aplicar métodos hidrológicos consagrados

Fornecer resultados claros e rastreáveis para projetos de drenagem

A interface gráfica será apenas um meio de uso — não o centro do sistema.

🧠 Conceito Arquitetural

O Pluvion segue o padrão MVC (Model–View–Controller):

Model: núcleo hidrológico (dados, regras e cálculos)

View: interface gráfica (PySide6)

Controller: controle de fluxo e orquestração

Essa separação garante:

Código organizado

Facilidade de manutenção

Possibilidade de reutilização do motor em CLI, API ou web

🧮 Funcionalidades (V1)

Entrada de dados da bacia hidrográfica

Cálculo do tempo de concentração

Determinação da intensidade de chuva

Cálculo da vazão de projeto (método racional)

Apresentação clara dos parâmetros adotados

🚧 Escopo Atual

✔ Motor hidrológico em desenvolvimento
✔ Estrutura preparada para testes
✔ Interface gráfica planejada

❌ Integração com CAD/BIM
❌ Análises espaciais
❌ Automação avançada

Esses recursos ficam para versões futuras.

📂 Estrutura do Projeto
pluvion/
├── core/        # Motor hidrológico
├── controllers/ # Controle de fluxo
├── ui/          # Interface PySide6
├── tests/       # Testes do núcleo
├── utils/       # Funções auxiliares
└── main.py

🛠️ Tecnologias

Python 3

PySide6 (interface gráfica)

Arquitetura MVC

Testes unitários no núcleo hidrológico

📌 Filosofia do Projeto

Fórmulas vêm antes da interface.
Engenharia vem antes da estética.
Código claro dura mais que código rápido.

📈 Visão de Futuro

Expansão dos métodos hidrológicos

Geração de relatórios técnicos

Integração com outros fluxos de projeto

Possível uso como biblioteca ou serviço

⚠️ Aviso

Este projeto está em desenvolvimento e não substitui a análise crítica de um engenheiro. Os resultados devem sempre ser avaliados dentro do contexto técnico e normativo do projeto.
