# plantio

Software de banco de dados e ferramentas visuais para planejamento de plantios e áreas em Sistemas Agroflorestais - SAFS - e afins.

## conceito: Banco de dados de espécies e variedades

Cada planta cadastrada é uma entidade genêrica, sendo implementada pela variedade. Isto é, uma mesma planta pode possuir múltiplas variedades.

Cada variedade extende as propriedades da planta, mas pode alterar alguns atributos - mas não todos: exigência de solo, porte, necessidades hídricas etc; já aleopatias geralmente não são alteradas pelas variedades.

## Plantas / espécies

Cadastro de espécies com atributos diversos. Os atributos marcados com um * podem ser alterados pelas variedades.

* família
* porte *
* necessidades hídricas *
* exigência de solo *
* ciclos (crescimento, floração, frutificação, dormência) *
* densidade da copa -> vetor temporal de desenvolvimento *
* alelopatias (antagonismos) - seleção manual de outras espécies

## Variedades

Uma variedade é uma extensão da espécie, mas com variações pequenas. Podem ser atribuídas a experiências localizadas e temporais. 

* nome da variedade
* descrição
* localização
* porte
* exigências de solo
* porte
* ciclo de crescimento

## Definição de áreas

Definições sobre a área:
* dimensões
* solo
* clima
* declividade
* área total

## Definição do desenho da área

Padrões para implantação do plantio
* desenhos vetoriais de padrões (linhas contínuas, linhas em curva de nível, intersecções / flores / mandalas)
* mapeamento de áreas cultiváveis e passagens em áreas

1) Selecione uma área
2) defina um padro de implantação de plantio
3) escolha as espécies
* exibição de caixas de seleção separadas por atributos das plantas
* ao "arrastar" a planta para a área, pode projetar a copa dela (como área de mancha transparente)
4) espécies parceiras ou antagônicas são exibidas conforme as espécies adjacentes

## Consultas

* Visualização da projeção do canteiro por timeline / time range
* visualização por linhas paralelas
* visualizaço em plano horizontal (projeção timeline)
