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

##### ***3) Aplicação do modelo ABM para a pergunta de pesquisa<br/>***

O Modelo Baseado em Agentes (ABM) se mostra adequado para a pergunta de pesquisa, tendo em vista que se configuraria 
como capaz de auxiliar na simulação de cenários, contribuindo para uma avaliação "ex-antes" no tocante aos impactos
de uma eventual política pública que favorecesse o aumento da concorrência no mercado bancário, incluindo um 
estímulo maior a entrada das chamadas fintechs e bigtechs nesse mercado; hipótese esta que não foi explorada neste
trabalho e que, portanto, poderia ser considerada como uma agenda futura de estudos no campo da concentração 
bancária, não se limitando ao mercado de crédito, mas podendo ser estendida ao mercado de intermediação financeira 
como um todo.

##### ***4) Agentes***

Os agentes seriam os 20 maiores bancos brasileiros, considerando os respectivos valores de ativos totais. Além disso,
foram inseridos, para fins de interações no tocante às aquisições, os 10 maiores bancos estrangeiros. Para fins de 
simplificação do modelo, considerou-se que, inicialmente, os bancos estrangeiros não atuariam no Brasil até a 
realização da primeira aquisição por parte desses bancos. 

Cumpre esclarecer que os bancos e as respectivas variáveis não foram criadas aleatoriamente, mas sim com base em 
dados obtidos no IF.data do Bacen. Assim, a alimentação do programa foi realizada por meio do arquivo "dados.csv",
disponível neste diretório do GitHub (https://github.com/douglasmarcelinodossantos/Douglas_ABM_Projeto).

##### ***5) Processo a ser replicado, padrão, regras e literatura***

O processo a ser replicado se refere ao movimento de aquisições de bancos a fim de mensurar qual seriam os potencias
impactos no mercado de crédito, em especial, na concentração de crédito e no ranking dos maiores bancos brasileiros 
em caso de aquisições de bancos brasileiros por bancos estrangeiros e/ou nacionais.

Quanto ao padrão e regras, vislumbrou-se que, além das interações realizadas entre os bancos brasileiros, poder-se-ia 
realizar interações de compras de bancos por parte de instituições financeiras internacionais de forma a demonstrar
os benefícios para os clientes de uma maior abertura do mercado bancário brasileiro. Cabe destacar que todas as
interações seriam realizadas de forma aleatória, por meio da funcionalidade random, disponível na linguagem Python 
e no aplicativo PyCharm.

Ainda sobre as regras, destaque-se que se referem às atuações dos agentes "bancos" enquanto compradores e potenciais 
ativos a serem adquiridos, caso existam bancos interessados e capazes de adquirirem os bancos que atuam no mercado
brasileiro. Diante disso, a origem das regras seriam basedas no livre mercado, nas quais o banco comprador poderia
adquirir quaisquer dos bancos que atuam no Brasil. 

Por outro lado, como forma de impedir que, inadvertidamente, um banco que não atuasse no Brasil fosse comprado na
simulação realizada no Programa, foi inserida, no script, uma restrição para somente pudessem ser objeto de 
aquisições os bancos que possuíssem ativos totais diferentes de zero, conforme linhas 60 a 64 do arquivo simulacao.py,
reproduzidas a seguir:

```python
  # se o banco vendido tiver um ativo total igual a 0, vai-se iniciar um loop ate encontrar um banco valido
            while banco_vendido.ativo_total == 0:
                indice_vendido = random.randrange(len(self.bancos))
                self.bancos.append(banco_vendido)
                banco_vendido = self.bancos.pop(indice_vendido)

````
No tocante à literatura sobre concentração bancária, cabe destacar o trabalho do Prof. Daniel Oliveira Cajueiro, PhD, 
que tem se dedicado aos estudos da chamada Teoria "Grande Demais para Quebrar" ” (TBTF, too big to fail), atuando,
inclusive, na orientação de pesquisas que se valem do ABM, como por exemplo na dissertação apresentada ao Programa 
de Mestrado em Economia da Universidade de Brasília por Joaquim Ignacio Alves de Vasconcellos e Lima, sob título
"Um arcabouço computacional para estudo do setor bancário através de modelos baseados em agentes", disponível em:
https://repositorio.unb.br/bitstream/10482/16752/1/2014_JoaquimIgnacioAlvesDeVasconcellosELima.pdf.

##### ***6) Ambiente de Interação***

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

##### ***7) Processo***

De forma resumida, o primeiro passo do Programa é a alimentação da base de dados por meio do arquivo Reader.py, que
realiza a leitura do arquivo dados.csv. A partir daí, são criados os bancos que se configuram com os agentes do 
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
    def set_juros(self):
        self.taxa_juros = random.randint(150, 450) / 10  # Gerando taxa de juros aleatoria entre 15% e 45%
````

Já o percentual da carteira de crédito total de cada banco é calculada da seguinte forma:

````python
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
````

Cabe destacar que, para simular o impacto de cada cliente na carteira de crédito, foi simulado que a cada cliente
migrado com a aquisição dos bancos, a carteira de crédito do banco adquirido seria acrescido de 2%, para fins de
simulação de acréscimo da margem de contribuição de cada cliente em cada banco.

##### ***8) Validação***

Quanto à validação, os dados inciais utilizados refletem a situação dos 20 maiores bancos brasileiros com posição
de março de 2020. Tais dados foram obtidos do repositório do IF.data do Bacen. Portanto, de certo modo, o modelo
replica os dados empíricos exsitentes.

Adicionalmente, os dados que resultam do acionamento do modelo podem ser validados mediante às consultas aos 
arquivos acompanhamento.txt e bancos_vendidos.csv.

Ademais, sugestões e recomendações associadas á pesquisa são bem-vindas, em especial do Professor Bernardo Furtado,
tendo em vista que contribuiriam para o aprimoramento do modelo.

##### ***9) Verificação e Teste***

Conforme os testes realizados ao longo do desenvolvimento do código anexo a este readme.md, foi possível verificar
que o código realiza o que se pretende. Além disso, foram realizados prints intermediários, conforme pode ser 
evidenciado pelos arquivos acompanhamento.txt e bancos_vendidos.csv. Adicionalemente, foram utilizados o debug ao 
longo do desenvolvimento do código.






        