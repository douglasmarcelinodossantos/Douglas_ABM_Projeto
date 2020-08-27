# coding=utf-8
import random
import Reader
from banco import Banco
from cliente import Cliente

mensagem = 'Destaque-se que a base de dados é composta pelos 20 maiores bancos brasileiros mais os 10 maiores bancos ' \
        'estrangeiros. Este programa simula aquisições de bancos e o % da carteira \nde crédito de cada banco após ' \
        'as aquisições. Contudo, o número máximo de aquisições é de 28 bancos.\ninforme o número de aquisiçõe de ' \
        'bancos brasileiros que você deseja simular: '

num_aquisicoes = int(input(mensagem))
while num_aquisicoes > 28 or num_aquisicoes < 1:
    num_aquisicoes = int(input("Escolha im número de aquisições entre 1 e 28: "))

# O programa poderia rodar as simulações com um número de aquisições pré-definidas, como solicitar ao usuário que
# informe um número de aquisições a serem simuladas. Particularmente, entendo que o mais indicado seria solicitar que
# o usuário insira o número de aquisições a serem simuladas.

#num_aquisicoes =

num_clientes = 65000  # considerar o número de clientes x 1.000
num_clientes_novos = random.randint(1000, 45000)  # adicionando novos clientes ao mercado bancário (x 1.000)
valor_por_cliente = 10000  # ticket de médio de operações de crédito para os novos clientes


class Simulacao:

    def __init__(self):
        self.bancos = list()
        self.clientes = list()
        self.novos_clientes = list()

    def cria_agentes(self):
        dados = Reader.run()
        for item in dados:
            self.bancos.append(Banco(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8]))

        for i in range(num_clientes):
            cliente = Cliente(i + 1, None)

            banco_escolhido = random.choice(self.bancos)
            diferenca = cliente.taxa_aceite - banco_escolhido.taxa_juros
            while banco_escolhido.ativo_total == 0 or diferenca < -5:
                banco_escolhido = random.choice(self.bancos)
                diferenca = cliente.taxa_aceite - banco_escolhido.taxa_juros
            cliente.banco = banco_escolhido
            self.clientes.append(cliente)
            banco_escolhido.numero_clientes += 1

    def run(self):
        acompanhamento = []
        vendidos = ['Nome,Ativo Total,Carteira de Crédito,Passivo Circulante,Captações,Patrimonio Liquido,'
                    'Lucro Liquido,Numero de Agencias,Numero de Postos,Comprado Por']

        for _ in range(num_aquisicoes):
            indice_comprador = random.randrange(len(self.bancos))  # Escolhendo indice do banco comprador
            banco_comprador = self.bancos.pop(indice_comprador)  # Selecionando banco comprador

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

            # muda clientes do banco vendido para o banco comprador
            for cliente in self.clientes:
                if cliente.banco == banco_vendido:
                    cliente.banco = banco_comprador
        acompanhamento.append(f"Clientes novos {num_clientes_novos}")
        salvar('acompanhamento.txt', acompanhamento)
        salvar('bancos_vendidos.csv', vendidos)

        # Calculando taxas de juros dos bancos
        taxas = []
        for banco in self.bancos:
            taxas.append(banco.taxa_juros)

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

            # impacto novo cliente
            banco_escolhido.carteira_credito += valor_por_cliente

        # Calculando o crédito total
        # O saldo total de crédito  da carteira classificada do SFN seria de aproximadamente R$ 3.573.752.789 (x 1.000).
        # Dessa forma, para fins de cálculos do % de cada banco, subtraiu-se do referido valor a soma dos saldos das
        # carteiras de crédito dos 20 maiores bancos brasileiros (aproximadamente R$ 2.733.480.262 x 1.000), valor este
        # contido no arquivo "dados.csv". Dessa forma, após os movimentos de aquisições, é calculdo o novo percentual de
        # cada banco na carteira de crédito total, conforme fórmula contida na linha 117 a seguir. Cabe destacar que,
        # o saldo total de crédito e os saldos da carteira de crédito dos 20 maiores bancos brasileiros foram extraídos
        # do IF.data do Bacen: https://www3.bcb.gov.br/ifdata/
        credito_total_sfn = 840272527.0
        for banco in self.bancos:
            credito_total_sfn += banco.carteira_credito

        for banco in self.bancos:
            if banco.ativo_total != 0:
                porcentagem = float((banco.carteira_credito * 100) / credito_total_sfn)
                print(f"{banco.nome}\nAtivos totais: {banco.ativo_total}\nCarteira de crédito: {banco.carteira_credito}"
                      f"- {'%.2f' % porcentagem} do SFN")

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


def salvar(arquivo, valores):
    with open(arquivo, 'w') as file:
        file.writelines(valores)


if __name__ == '__main__':
    simulacao = Simulacao()
    simulacao.cria_agentes()
    simulacao.run()
