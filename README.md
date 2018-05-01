# plantio

Software de banco de dados distribuído e ferramentas visuais para planejamento e acompanhamento de plantio de Sistemas Agroflorestais - SAFS e policultivos em geral.

## objetivos

* Criar um banco de dados sobre espécies de plantas com usos variados com alimentação de dados distribuída e colaborativa
* Criar uma ferramenta de planejamento de cultivos agroflorestais que auxilie na identificação de simpatias, alelopatias, compatibilidade de crescimento / insolação e interação e assim propicie uma análise combinatória
* Criar relatórios de previsão de colheita e ocupação do solo em escala temporal móvel para auxílio na implantação de sistemas agroflorestais capazes de garantir autosustento do solo (redução ao mínimo do uso de insumos externos - LEISA - Low External Input Sustainable Agriculture) e familiar.
* Fomentar o compartilhamento de informações agrícolas diretamente entre produtor@s sem mediação de técnicos de extensão agrícola
* Criar uma arquitetura expansível

## arquitetura

O software é um nó que pode funcionar sozinho (offline), mas pode se integrar a outros nós por meio de um protocolo de comunicação compartilhado.

````   X   nó isolado
    
    X---X
     \  |   nós em rede
       \|
        X
````
Um nó isolado, entretanto, é um nó da rede em potencial, podendo ser conectado. O software adere ao protocolo de comunicação do Baobáxia / http://github.com/RedeMocambos/baobaxia e a rede assume a característica de online/offline.

Cada informação adicionada a um nó possui referencias do nó em que se originou e do local a que se refere. A localização do dado, em conjunto com outros atributos de similaridade, definirão a relevância da informação.

## definição dos algorítmos de relevância

Uma questão crucial dos softwares de rede hoje em dia é o poder do algorítmo frente à pessoa que utiliza o software. Por isso, preferimos que além de o algorítmo ser disponibilizado como software livre, seja facilmente configurável e alterável para cada nó. Isso permite que variáveis e pesos diferentes sejam definidos em cada nó / comunidade - afinal a experiência obtida numa área de cerrado difere de uma em área de mata atlântica, muito embora guardem semelhanças entre si quando comparadas a uma área de clima temperado.

O programa propõe uma configuração inicial que pode ser livremente alterada.

### Sugestão de espécies na montagem

A sugestão de espécies aparece após a escolha da área e do padrão de plantio. Não há ordem de implantação, mas sugere-se que se inicie a seleção das espécies começando pelos maiores exemplares (arbóreos). A seleção de espécies busca todas as já adicionadas ao sistema e observa quais estratos já estão atendidos, sugerindo espécies a serem adicionadas para preencher os estratos faltantes. As espécies são filtradas de modo a privilegiar outras famílias e excluindo as plantas antagonistas. A configuração do algorítmo de seleção pode ser alterada por plantio/canteiro (ex: permitir mais de uma espécie da mesma família, quantidade de espécies por estrato)

### cardapio e planejamento de plantio

Uma forma de selecionar espécies é listar as frutas, verduras e demais plantas utilizadas em parte da alimentação de uma pessoa ou coletividade. A listagem de plantas pode levar a uma análise de viabilidade a fim de selecionar espécies viáveis para determinado local, conforme condições climáticas e de solo. Adicionalmente pode se criar rascunhos de agrupamentos com previsão de colheita para fins de abastecimento daquelas pessoas.

## conceito: Banco de dados de espécies e variedades

Cada espécie cadastrada é uma entidade genérica, podendo possuir variedades que expandem e sobrescrevem as propriedades da espécie. Uma mesma planta pode possuir múltiplas variedades.

As variedades extendem as propriedades da espécie e podem alterar alguns atributos - mas não todos. Exemplos de atributos alteráveis: exigência de solo, porte, necessidades hídricas etc.

A interação entre as espécies é mapeada sinalizando aleopatias e sinergias de modo a sugerir combinações favoráveis ou não.

Um dos usos possíveis do software é como auxiliar no acompanhamento e registro de alelopatias e sinergias entre espécies: toda e qualquer informação adicionada possui uma referência de origem - que pode ser um estudo, um livro ou um dado observacional. Os pesos de cada uma das informações podem ser configurados de acordo com o plantio - por exemplo, seria possível atribuir peso maior a uma informação coletada a partir de dados observacionais num mesmo bioma ou região.


## Espécies

Cadastro de espécies com atributos diversos. Os atributos marcados com um * podem ser alterados pelas variedades.
* nome cientifico (Chave)
* nomes populares
* família
* fotos
* porte *
* necessidades hídricas *
* exigência de solo * dúvida - criei classes aleatórias, a revisar/repensar
* tolerância a poda (0-10) sendo 0 nenhuma, 10 rebrota vigorosa indefinidamente
* exigência de sol (0-10) sendo 0 sombra, 10 pleno sol
* temperatura (range)
* tempo de colheita
* interação com outras espécies: alelopatias e sinergias - seleção manual de outras espécies
* estrato: baixo, médio, alto/dossel, emergente
* sucessão: "perfil" da planta: colonizadoras, pioneiras, secundárias iniciais, secundárias tardias, clímax
* tempo de vida: dias, meses, anos

Tipo de porte: engloba os ciclos e a densidade da copa, descritos numa matriz espacial/temporal

## Variedades

Uma variedade é uma extensão da espécie, mas com variações pequenas. Podem ser atribuídas a experiências localizadas e temporais. 

* nome da variedade / cultivar
* descrição
* localização
* porte
* exigências de solo
* ciclo de crescimento

## Ciclos e Tipo de porte

Cada planta possui um ciclo, composto de várias fases. Cada fase está associada a um porte médio esperado determinada espécie ou variedade, com momentos de crescimento, floração, frutificação, dormência e caducidade.

O porte é uma descrição temporal simplificada do volume e densidade médios da copa.

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

### Catálogo de ciclos

Quando um ciclo de uma planta é adicionado, seu desenho vai para uma tabela de padrões de ciclos. Os ciclos de folhação de um abacateiro e de uma mangueira, por exemplo, podem ser relativamente parecidos; os ciclos de coqueiros e palmeiras e sua folhação igualmente podem ser parecidos. Deste modo, quando vou cadastrar o ciclo de uma planta nova, me é oferecido um catálogo de padrões de ciclos (desenhos) já preenchidos para facilitar o preenchimento.

### Campos 

* idFase
* idEspecie not null
* idVariedade
* nome      not null
* ordem     smallint not null
* descricao
* matrizPorte   json
* floracao      bool
* frutificacao  bool
* deciduidade   bool ? dúvida: seria necessário um descritor específico ?

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

## Padrão de plantio

Padrões de plantio são formas de agrupamento de espécies. Podem ser canteiros lineares, mandalas, círculos ou curvas de nível.

## Consultas

* Visualização da projeção do canteiro por data / faixa de tempo
* visualização por linhas paralelas
* visualizaço em plano horizontal (projeção timeline)

### Apresentações gráficas possíveis para saída de dados

Evolução do crescimento das plantas
https://square.github.io/cubism/

Diagrama de famílias, atributos (solo, umidade etc) ciclos de vida e tempo de colheita
https://www.jasondavies.com/coffee-wheel/

Calendar view
https://bl.ocks.org/mbostock/4063318

## Referências

A elaboração do sistema utiliza conceitos da agroecologia e agrofloresta. Destacamos aqui algumas das referências bibliográficas utilizadas:


PRIMAVESI, Ana. Pergunte ao solo e às raízes - uma análise do solo tropical e mais de 70 casos resolvidos pela agroecologia. São Paulo: Nobel, 2014.

REIJNTJES, C.; HAVERKORT, B.; WATERS-BAYER, A. Agricultura para o futuro: uma introducao a agricultura sustentavel e de baixo uso de insumos externos. Rio de Janeiro: AS-PTA, 1994.

