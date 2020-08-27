##### ***Mestrado Profissional em Políticas Públicas e Desenvolvimento***
##### ***Instituto de Pesquisa Econômica Aplicada - Ipea***
##### ***Disciplina de Python para Modelagem Baseada em Agentes***
##### ***Professor: Bernardo Alves Furtado***
##### ***Aluno: Douglas Marcelino dos Santos***
##### ***Brasília, 23 de julho de 2020***


##### ***Trabalho Final da Disciplina***
##### ***ABM - Projeto***   


##### ***1) Pergunta de Pesquisa***

A pergunta de pesquisa que norteia o Projeto de Modelagem Baseada em Agentes para obtenção do crédito da 
disciplina de nome análogo e, que é parte do Programa de Mestrado Profissional em Políticas Públicas e 
Desenvolvimento do Ipea, está representada a seguir:

##### ***Como ficariam o ranking das maiores instituições financeiras e a concentração de crédito caso ocorram aquisições no mercado bancário, considerando como potenciais adquirentes tanto bancos brasileiros como os dez maiores bancos mundiais?***

##### ***2) Hipótese:***

Como hipótese, poder-se-ia considerar a seguinte:

Caso ocorram aquisições de bancos brasileiros, por parte de bancos estrangeiros que não possuem operações no 
Brasil, seria possível uma alteração significativa no ranking das maiores instituições financeiras, bem como 
uma redução significativa na concentração de crédito. Por outro lado, caso as aquisições sejam realizados por 
bancos brasileiros, possivelmente o ranking e a concentração de crédito não se alteraria, pois, dificilmente, 
um banco pequeno teria condições de comprar um dos seis maiores bancos ou mesmo, de adquirir vários bancos 
médios que propiciassem ao banco pequeno (comprador) subir posições no ranking de ativos totais, bem como reduzir 
a concentração de crédito.

Portanto, considerando o poder econômico dos maiores bancos brasileiros, provavelmente, as aquisições de 
instituições financeiras seriam realizadas por esses maiores bancos. Cabe destacar as últimas aquisições 
realizadas no mercado bancário brasileiro foram realizadas pelos gigantes brasileiros, como por exemplo: 
Itaú vs. Unibanco, Bradesco vs. HSBC e até mesmo a XP Investimentos, também pelo Itaù Unibanco.

Outro aspecto importante é que os 6 maiores bancos brasileiros detêm cerca de 69,21% da carteira de crédito do 
mercado bancário, conforme pode ser observado a partir dos dados contidos no IF.data do Banco Central do Brasil - 
disponível em: https://www3.bcb.gov.br/ifdata/. Assim, a simulação realizada pelo programa objeto deste Projeto 
ABM seria útil para mensurar quais seriam os impactos da existência de um número maior de bancos com consideráveis
capacidades de atuação no mercado bancário, como por exemplo, os maiores bancos estrangeiros que ainda não atuam
no Brasil em larga escala.

##### ***3) Objetivo do Projeto de Pesquisa<br/>***

O projeto de pesquisa possui como objetivos principais "simular a aquisição aleatória sucessiva de bancos" no 
intuito de observar a concentração financeira, em especial no que diz respeito ao ranking de maiores bancos e à 
concentração de crédito, bem como no comportamento dos clientes.

##### ***4) Aplicação do modelo ABM para a pergunta de pesquisa<br/>***

O Modelo Baseado em Agentes (ABM) se mostra adequado para a pergunta de pesquisa, tendo em vista que se configuraria 
como capaz de auxiliar na simulação de cenários, contribuindo para uma avaliação "ex-antes" no tocante aos impactos
de uma eventual política pública que favorecesse o aumento da concorrência no mercado bancário, incluindo um 
estímulo maior a entrada das chamadas fintechs e bigtechs nesse mercado; hipótese esta que não foi explorada neste
trabalho e que, portanto, poderia ser considerada como uma agenda futura de estudos no campo da concentração 
bancária, não se limitando ao mercado de crédito, mas podendo ser estendida ao mercado de intermediação financeira 
como um todo.

##### ***5) Agentes***

Os agentes seriam os 20 maiores bancos brasileiros, considerando os respectivos valores de ativos totais. Além disso,
foram inseridos, para fins de interações no tocante às aquisições, os 10 maiores bancos estrangeiros. Para fins de 
simplificação do modelo, considerou-se que, inicialmente, os bancos estrangeiros não atuariam no Brasil até a 
realização da primeira aquisição por parte desses bancos. 

Cumpre esclarecer que os bancos e as respectivas variáveis não foram criadas aleatoriamente, mas sim com base em 
dados obtidos no IF.data do Bacen. Assim, a alimentação do programa foi realizada por meio do arquivo "dados.csv",
disponível neste diretório do GitHub (https://github.com/douglasmarcelinodossantos/Douglas_ABM_Projeto).

##### ***6) Processo a ser replicado, padrão, regras e literatura***

O processo a ser replicado se refere ao movimento de aquisições de bancos a fim de mensurar quais seriam os potencias
impactos no mercado de crédito, em especial, na concentração de crédito e no ranking dos maiores bancos brasileiros 
em caso de aquisições de bancos brasileiros por bancos estrangeiros e/ou nacionais.

Quanto ao padrão e regras, vislumbrou-se que, além das interações realizadas entre os bancos brasileiros, poder-se-ia 
realizar interações de compras de bancos por parte de instituições financeiras internacionais de forma a demonstrar
os benefícios para os clientes de uma maior abertura do mercado bancário brasileiro. Cabe destacar que todas as
interações seriam realizadas de forma aleatória, por meio da funcionalidade random, disponível na linguagem Python 
e no aplicativo PyCharm.

Ainda sobre as regras, destaque-se que se referem às atuações dos agentes "bancos" enquanto compradores e potenciais 
ativos a serem adquiridos, caso existam bancos interessados e capazes de adquirirem os bancos que atuam no mercado
brasileiro. Diante disso, a origem das regras seriam baseadas no livre mercado, nas quais o banco comprador poderia
adquirir quaisquer dos bancos que atuam no Brasil. 

Por outro lado, como forma de impedir que, inadvertidamente, um banco que não atuasse no Brasil fosse comprado na
simulação realizada no Programa, foi inserida, no script, uma restrição para somente pudessem ser objeto de 
aquisições os bancos que possuíssem ativos totais diferentes de zero, conforme linhas 60 a 96 do arquivo simulacao.py,
reproduzidas a seguir:

```python
            # verifica quais bancos podem ser comprados
            bancos_possiveis = []
            while len(bancos_possiveis) == 0:
                if banco_comprador.ativo_total > 0:
                    for banco in self.bancos:
                        if banco_comprador.ativo_total > banco.ativo_total != 0:
                            # cria tupla com banco e indice
                            bancos_possiveis.append((banco, self.bancos.index(banco)))

                    if len(bancos_possiveis) == 0:
                        indice_comprador = random.randrange(len(self.bancos)) # Escolhendo indice do banco comprador
                        self.bancos.append(banco_comprador) # Devolvendo banco com menor ativo e lista de bancos
                        banco_comprador = self.bancos.pop(indice_comprador) # Selecionando banco comprador
                else:
                    for i in range(len(self.bancos)):
                        bancos_possiveis.append((self.bancos[i], i))

            indice_vendido = random.randrange(len(bancos_possiveis))  # Escolhendo indice do banco vendido
            banco_vendido = bancos_possiveis.pop(indice_vendido)  # Selecionando banco vendido

            # se o banco vendido tiver um ativo total igual a 0, vai-se iniciar um loop ate encontrar um banco valido
            while banco_vendido[0].ativo_total == 0:
                indice_vendido = random.randrange(len(bancos_possiveis))
                bancos_possiveis.append(banco_vendido)
                banco_vendido = bancos_possiveis.pop(indice_vendido)

            banco_comprador.aquisicao(banco_vendido[0])
            self.bancos.pop(banco_vendido[1])
            self.bancos.append(banco_comprador)
            banco_vendido = banco_vendido[0]
            acompanhamento.append(f'Banco {banco_comprador.nome} comprou banco {banco_vendido.nome}\n')
            vendido = '\n' + str(banco_vendido.nome) + ',' + str(banco_vendido.ativo_total) + ',' + \
                      str(banco_vendido.carteira_credito) + ',' + str(banco_vendido.passivo_circulante) + ',' + \
                      str(banco_vendido.captacoes) + ',' + str(banco_vendido.patrimonio_liquido) + ',' + \
                      str(banco_vendido.lucro_liquido) + ',' + str(banco_vendido.numero_agencias) + ',' + \
                      str(banco_vendido.numero_postos) + ',' + str(banco_comprador.nome)
            vendidos.append(vendido)

````
No tocante à literatura sobre concentração bancária, cabe destacar o trabalho do Prof. Daniel Oliveira Cajueiro, PhD, 
que tem se dedicado aos estudos da chamada Teoria "Grande Demais para Quebrar" ” (TBTF, too big to fail), atuando,
inclusive, na orientação de pesquisas que se valem do ABM, como por exemplo na dissertação apresentada ao Programa 
de Mestrado em Economia da Universidade de Brasília por Joaquim Ignacio Alves de Vasconcellos e Lima, sob título
"Um arcabouço computacional para estudo do setor bancário através de modelos baseados em agentes", disponível em:
https://repositorio.unb.br/bitstream/10482/16752/1/2014_JoaquimIgnacioAlvesDeVasconcellosELima.pdf.

##### ***7) Ambiente de Interação***

O ambiente de interação entre os agentes, ou seja, entre os bancos compradores e adquiridos se dá de forma aleatória,
viabilizada pelo comando random.randrange, assim como a mudança do ambiente. Cabe destacar que as aquisições são 
realizadas uma após outra, sendo que após a realização de todas as interações é gerado um arquivo csv contendo os 
resultados das interações. Nesse instante, são apresentados os valores das variáveis: Ativo Total, Carteira de Crédito,
Passivo Circulante, Captações, Patrimonio Liquido, Lucro Liquido, Numero de Agencias, Numero de Postos, Porcentagem
de Carteira de Crédito, Número de Clientes e Taxa de Juros. 

Os valores finais das variáveis são apurados por meio da seguinte programação:

````python
        valores = ['Nome,Ativo Total,Carteira de Crédito,Passivo Circulante,Captações,Patrimonio Liquido,'
                   'Lucro Liquido,Numero de Agencias,Numero de Postos,Porcentagem de Carteira de Crédito,'
                   'Número de Clientes,Taxa de Juros']
        for banco in self.bancos:
            porcentagem = float((banco.carteira_credito * 100) / credito_total_sfn)
            valor = '\n' + str(banco.nome) + ',' + str(banco.ativo_total) + ',' + str(banco.carteira_credito) + ',' + \
                    str(banco.passivo_circulante) + ',' + str(banco.captacoes) + ',' + str(banco.patrimonio_liquido) + \
                    ',' + str(banco.lucro_liquido) + ',' + str(banco.numero_agencias) + ',' \
                    + str(banco.numero_postos) + ',' + str('%.2f' % porcentagem) + ',' + str(banco.numero_clientes) + \
                    ',' + str(banco.taxa_juros)
            valores.append(valor)
            print("---------------------")
            print(banco)

        salvar('resultado_aquisicoes.csv', valores)
````

Ademais, é importante destacar que, no início do programa é solicitado ao usuário informar qual seria o número de
aquisições que ele desejaria simular. O código também poderia ser adaptado a fim de se travar um número fixo de 
aquisições, no entanto, considero que o mais adequado seria permitir que o usuário informe a quantidade desejada,
desde que limitada a 28 bancos, uma vez que o número de bancos utilizado no programa é de 30 instituições
financeiras.

##### ***8) Processo***

De forma resumida, o primeiro passo do Programa é a alimentação da base de dados por meio do arquivo Reader.py, que
realiza a leitura do arquivo dados.csv. A partir daí, são criados os bancos que se configuram como os agentes do 
modelo ABM objeto deste texto, considerando os dados das variáveis extraídas do IF.data do Banco Central. 

Após a leitura dos dados e a criação dos agentes, há a criação dos clientes, a fim de ilustar interações entre os 
clientes e os bancos. Inicialmente, são distribuidos aleatoriamente entre os bancos brasileiros, ou seja, que possuem 
ativos totais diferentes de zero. Por meio do arquivo "simulacao.py", as interações são realizadas. Dessa forma, 
para que o Programa rode, basta acionar o comando run no arquivo simulacao.py, no PyCharm ou em outro leitor para 
programas desenvolvidos na linguagem Python.

Além disso, conforme já mencionado neste texto, com as interações (aquisições de bancos), ocorrem mudanças nos 
valores das variáveis (ativo total, patrimônio líquido, carteira de crédito, número de cliente, entre outros). Assim,
o Programa calcula os novos valores mediante a soma dos recursos do banco, com exceção da taxa de juros e da 
concentração de crédito. A taxa de juros também é atribuída aleatoriamente, conforme a seguir:

````python
    def __init__(self, nome, ativo_total, carteira_credito, passivo_circulante, captacoes, patrimonio_liquido,
                 lucro_liquido, numero_agencias, numero_postos):
        self.nome = nome
        self.ativo_total = int(ativo_total)
        self.carteira_credito = int(carteira_credito)
        self.passivo_circulante = int(passivo_circulante)
        self.captacoes = int(captacoes)
        self.patrimonio_liquido = int(patrimonio_liquido)
        self.lucro_liquido = int(lucro_liquido)
        self.numero_agencias = int(numero_agencias)
        self.numero_postos = int(numero_postos)
        self.numero_clientes = 0
        self.taxa_juros = random.randint(150, 450) / 10  # Gerando taxa de juros aleatoria entre 15% e 45%
````

Já o percentual da carteira de crédito total de cada banco é calculada da seguinte forma:

````python
        credito_total_sfn = 840272527.0
        for banco in self.bancos:
            credito_total_sfn += banco.carteira_credito

        for banco in self.bancos:
            if banco.ativo_total != 0:
                porcentagem = float((banco.carteira_credito * 100) / credito_total_sfn)
                print(f"{banco.nome}\nAtivos totais: {banco.ativo_total}\nCarteira de crédito: {banco.carteira_credito}"
                      f"- {'%.2f' % porcentagem} do SFN")
````

Destaque-se que a condicionalidade do processo de aquisição de bancos está relacionada aos valores dos ativos totais, ou 
seja, caso o banco comprador possua um ativo menor do que o banco que seria adquirido, a aquisição é suspensa e o 
sistema aciona um loop até identificar uma compra viável (banco comprador com ativo total maior do que o banco a ser 
comprado). Cumpre esclarecer, ainda, que essa condicionalidade não se aplicaria aos bancos estrangeiros, considerando o 
potencial financeiro que eles possuem por se tratarem dos 10 maiores bancos mundiais. 

`````python
            # verifica quais bancos podem ser comprados
            bancos_possiveis = []
            while len(bancos_possiveis) == 0:
                if banco_comprador.ativo_total > 0:
                    for banco in self.bancos:
                        if banco_comprador.ativo_total > banco.ativo_total != 0:
                            # cria tupla com banco e indice
                            bancos_possiveis.append((banco, self.bancos.index(banco)))

                    if len(bancos_possiveis) == 0:
                        indice_comprador = random.randrange(len(self.bancos))  # Escolhendo indice do banco comprador
                        self.bancos.append(banco_comprador)  # Devolvendo banco com menor ativo e lista de bancos
                        banco_comprador = self.bancos.pop(indice_comprador)  # Selecionando banco comprador
                else:
                    for i in range(len(self.bancos)):
                        bancos_possiveis.append((self.bancos[i], i))

            indice_vendido = random.randrange(len(bancos_possiveis))  # Escolhendo indice do banco vendido
            banco_vendido = bancos_possiveis.pop(indice_vendido)  # Selecionando banco vendido

            # se o banco vendido tiver um ativo total igual a 0, vai-se iniciar um loop ate encontrar um banco valido
            while banco_vendido[0].ativo_total == 0:
                indice_vendido = random.randrange(len(bancos_possiveis))
                bancos_possiveis.append(banco_vendido)
                banco_vendido = bancos_possiveis.pop(indice_vendido)

            banco_comprador.aquisicao(banco_vendido[0])
            self.bancos.pop(banco_vendido[1])
            self.bancos.append(banco_comprador)
            banco_vendido = banco_vendido[0]
            acompanhamento.append(f'Banco {banco_comprador.nome} comprou banco {banco_vendido.nome}\n')
            vendido = '\n' + str(banco_vendido.nome) + ',' + str(banco_vendido.ativo_total) + ',' + \
                      str(banco_vendido.carteira_credito) + ',' + str(banco_vendido.passivo_circulante) + ',' + \
                      str(banco_vendido.captacoes) + ',' + str(banco_vendido.patrimonio_liquido) + ',' + \
                      str(banco_vendido.lucro_liquido) + ',' + str(banco_vendido.numero_agencias) + ',' + \
                      str(banco_vendido.numero_postos) + ',' + str(banco_comprador.nome)
            vendidos.append(vendido)
````` 

Voltando aos clientes, inicialmente o programa inicia com 65.000. Cabe destacar que, esse número, para fins da análise, 
deve ser multiplicado por mil, tendo em vista que os valores apresentados nas variáveis dos bancos, incluindo os dados 
referentes às carteiras e crédito das instituições financeiras, também devem ser multiplicados por 1.000).

Ademais, considerando que a População Economicamente Ativa (PEA) no Brasil seria de aproximadamente 110 milhões 
de pessoas e que há cerca de 45 milhóes de desbancarizados no país, o número de pessoas que possuem conta bancária
no Brasil seria da ordem de 65 milhões de pessoas.

Dessa forma, conforme código a seguir, o programa cria aleatoreamente novos clientes. O número de clientes a serem 
criados varia de 1.000 a 45.000. Além disso, para fins de observação, foi estipulado que o ticket médio das operações de
crédito dos novos clientes seria de R$ 10.000,00. Assim, a cada novo cliente no SFN, ocorreria uma elevação de R$ 10 mil
na carteira de crédito do banco ao qual esse novo fosse vinculado.

````python
num_clientes = 65000  # considerar o número de clientes x 1.000
num_clientes_novos = random.randint(1000, 45000)  # adicionando novos clientes ao mercado bancário (x 1.000)
valor_por_cliente = 10000  # ticket de médio de operações de crédito para os novos clientes
````

No que tange à influência da taxa de juros nos resultados de concentração de crédito, cabe ressaltar que a lógica 
utiliza no código teve como inspiração o mercado real. Conforme é demonstrado no trecho adiante extraído do código do
programa, a taxa de juros de tolerância dos clientes varia, de forma aleatória, entre 15% e 45%, semelhantemente à taxa 
que é atribuída aos bancos.

`````python
class Cliente:

    def __init__(self, id, banco=None):
        self.id = id
        self.banco = banco
        self.taxa_aceite = random.randint(150, 450) / 10
`````

Assim, a escolha do banco pelo cliente se assemelha a situação que ocorre no mercado bancário, visto que o cliente 
possui uma taxa de juros de preferência e procura uma instituição que ofereça uma taxa muito próxima a que ele deseja. 
Caso não seja encotrado um banco que ofereça o patamar de juros semelhante ao demandado pelo cliente, é aceito o banco
que ofereça a menor taxa do mercado:

`````python
        # Calculando impacto dos clientes
        for j in range(len(self.clientes), num_clientes_novos+len(self.clientes)):
            cliente = Cliente(j + 1, None)

            existe_banco = False
            for banco in self.bancos:
                if (cliente.taxa_aceite-banco.taxa_juros) > -5 and banco.ativo_total != 0:
                    existe_banco = True

            if not existe_banco:
                cliente.banco = self.bancos[taxas.index(min(taxas))]

            else:
                banco_escolhido = random.choice(self.bancos)
                diferenca = cliente.taxa_aceite - banco_escolhido.taxa_juros

                while banco_escolhido.ativo_total == 0 or diferenca < -5:
                    banco_escolhido = random.choice(self.bancos)
                    diferenca = cliente.taxa_aceite - banco_escolhido.taxa_juros
                cliente.banco = banco_escolhido

            self.clientes.append(cliente)
            cliente.banco.numero_clientes += 1
`````

Portanto, o acréscimo da carteira de crédito dos bancos é realizado com base no número de novos clientes e na taxa de 
juros de preferência, ambos definidos aleatoreamente pelo programa, além, obviamente, das aquisições de outros bancos. 

##### ***9) Validação***

Quanto à validação, os dados inciais utilizados refletem a situação dos 20 maiores bancos brasileiros com posição
de março de 2020. Tais dados foram obtidos do repositório do IF.data do Bacen. Portanto, de certo modo, o modelo
replica os dados empíricos exsitentes.

Adicionalmente, os dados que resultam do acionamento do modelo podem ser validados mediante às consultas aos 
arquivos acompanhamento.txt e bancos_vendidos.csv.

##### ***10) Verificação e Teste***

Conforme os testes realizados ao longo do desenvolvimento do código anexo a este readme.md, foi possível verificar
que o código realiza o que se pretende. Além disso, foram realizados prints intermediários, conforme pode ser 
evidenciado pelos arquivos acompanhamento.txt e bancos_vendidos.csv. Adicionalemente, foram utilizados o debug ao 
longo do desenvolvimento do código.

##### ***11) Conclusão***

Realizadas as simulações por meio do código desenvolvido, infere-se que a entrada de bancos estrangeiros no mercado 
brasileiro, seja por meio de aquisição de bancos, ou mesmo pela autorização do Banco Central para novos players, poderia
auxiliar na redução da concentração de crédito.

Por outro lado, caso as aquisições fossem realizadas pelos grandes bancos brasileiros, a concentração aumentaria, 
prejudicando os consumidores e a economia, principalmente no tocante às taxas de juros oferecidas no mercado bancário.

Diante disso, uma estratégia eficiente por parte do regulador brasileiro poderia ser facilitar a entrada de novos 
players no mercado financeiro. Além dos grandes bancos estrangeiros poderia ser estimulada a atuação de fintechs, 
conforme o próprio Bacen já tem sinalizado por meio de suas análises e regulações recentes, como por exemplo, a criação
do Pix, que permitirá uma maior flexibilidade na transferência de recursos entre clientes de diversas instituições.

Por fim, uma maior quantidade de instituições financeiras no país, tanto bancos estrangeiros, como fintechs, poderia 
contribuir para a redução dos patamares de juros oferecidos no Brasil e, consequentemente, propiciar a bancarização de
um número maior de brasileiros.







        