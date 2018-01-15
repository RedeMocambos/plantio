# plantio

Software de banco de dados e ferramentas visuais para planejamento de plantios de policultivos e áreas em Sistemas Agroflorestais - SAFS.

## conceito: Banco de dados de espécies e variedades

Cada espécie cadastrada é uma entidade genêrica, podendo possuir variedades que expandem e sobrescrevem as prorpedades da espécie. Uma mesma planta pode possuir múltiplas variedades.

As variedades extendem as propriedades da espécie, mas pode alterar alguns atributos - mas não todos: exigência de solo, porte, necessidades hídricas etc.

A interação entre as espécies é mapeada sinalizando aleopatias e sinergias de modo a sugerir combinações favoráveis ou não.

## Espécies

Cadastro de espécies com atributos diversos. Os atributos marcados com um * podem ser alterados pelas variedades.

* família
* porte *
* necessidades hídricas *
* exigência de solo *
* tolerância a poda
* exigência de sol (0-10) sendo 0 sombra, 10 pleno sol
* interação com outras espécies: alelopatias e sinergias - seleção manual de outras espécies
* estrato: baixo, médio, alto/dossel, emergente
* sucessão: "perfil" da planta: colonizadoras, pioneiras, secundárias iniciais, secundárias tardias, clímax

Tipo de porte: engloba os ciclos e a densidade da copa, descritos numa matriz espacial/temporal

## Variedades

Uma variedade é uma extensão da espécie, mas com variações pequenas. Podem ser atribuídas a experiências localizadas e temporais. 

* nome da variedade / cultivar
* descrição
* localização
* porte
* exigências de solo
* porte
* ciclo de crescimento

## Tipo de porte

O porte da espécie é uma descrição temporal simplificada do volume e densidade médios da copa. 

O tipo de porte descreve o ciclo médio esperado da planta, indicando momentos de crescimento, floração, frutificação, dormência e caducidade.

A descrição deve contemplar necessariamente:

1) emergência
2) crescimento inicial
3) desenvolvimento pleno

Adicionalmente, conforme a espécie, podem existir:

4) Caducidade / perda de folhas
5) Podas juvenis

O porte é descrito numa matriz espacial 2D (informações do porte x altura serão descritos no estrato). O porte é descrito por um percentual de cobertura foliar, aonde 0 é ausente e 10 é cobertura completa.

Exemplos:

    # emergência
    __________
    |         |
    |    1    |
    |         |
    -----------
      
    # desenvolvimento inicial
    __________
    |    1    |
    |  1 4 1  |
    |    1    |
    -----------    
    
    # porte maduro - floração, frutificação
    ___________
    |  1 4 1  |
    |  4 8 4  |
    |  1 4 1  |
    -----------

## Interação entre plantas

A interação é a descrição da interação da relação de uma planta com outra. Podem ser mapeadas interaçes de tipos sinérgicos (cooperativos) ou alelopáticos (antipatia). O objetivo é otimizar a cooperação entre espécies e evitar combinações conflituosas. Como nem sempre a relação é simétrica, a interação é descrita numa direção, ou seja, de uma planta em relação a outra (existem casos em que uma planta faz muito bem a outra mas o contrário não é verdadeiro).

A intensidade da relação também pode ser apontada, como: suave, média, agressiva. Nas interações agressivas, uma espécie pode inviabilizar outra pela simples presença numa mesma área, mesmo que em canteiros distintos.

Uma interação associa duas espécies, define um tipo de relação, a intensidade da relação e adicionalmente se vinculam mais referências. O objetivo dessa informação estar presente no banco de dados é filtrar espécies conforme o grau de simpatia ou antipatia no momento da relação.


## Definição de áreas

Definições sobre a área:
* dimensões
* solo
* clima
* declividade predominante / ondulação: plano, baixada, encosta acentuada, encosta suave
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
