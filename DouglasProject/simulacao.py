# coding=utf-8
import random
import Reader
from banco import Banco
from cliente import Cliente

input('Este programa simula aquisições de bancos e o % da carteira de crédito de cada banco após as aquisições.'
        ' Contudo, o número máximo de aquisições é de 28 bancos. Tecle Enter, por favor.')
input('Destaque-se que a base de dados é composta pelos 20 maiores bancos brasileiros mais os 10 maiores bancos estrangeiros.'
      ' Tecle Enter novamente, por gentileza.')

num_aquisicoes = int(input('Informe o número de aquisições de bancos brasileiros que você deseja simular: '))

# O programa poderia rodar as simulações com um número de aquisições pré-definidas, como solicitar ao usuário que
# informe um número de aquisições a serem simuladas. Particularmente, entendo que o mais indicado seria solicitar que
# o usuário insira o número de aquisições a serem simuladas.

#num_aquisicoes =

num_clientes = 5000
percentual_cliente = 0.02


class Simulacao:

    def __init__(self):
        self.bancos = list()
        self.clientes = list()

    def cria_agentes(self):
        dados = Reader.run()
        for item in dados:
            self.bancos.append(Banco(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8]))

        for i in range(num_clientes):
            banco_escolhido = random.choice(self.bancos)
            while banco_escolhido.ativo_total == 0:
                banco_escolhido = random.choice(self.bancos)
            self.clientes.append(Cliente(i + 1, banco_escolhido))
            banco_escolhido.numero_clientes += 1

    def run(self):
        acompanhamento = []
        vendidos = ['Nome,Ativo Total,Carteira de Crédito,Passivo Circulante,Captações,Patrimonio Liquido,'
                    'Lucro Liquido,Numero de Agencias,Numero de Postos,Comprado Por']

        for _ in range(num_aquisicoes):
            indice_comprador = random.randrange(len(self.bancos))  # Escolhendo indice do banco comprador
            banco_comprador = self.bancos.pop(indice_comprador)  # Selecionando banco comprador

            # se o banco comprador for grande, ele não pode comprar (comando opcional, desabilitado)
            #while banco_comprador.ativo_total >= 500000000:
            #    indice_comprador = random.randrange(len(self.bancos))
            #    self.bancos.append(banco_comprador)
            #    banco_comprador = self.bancos.pop(indice_comprador)

            indice_vendido = random.randrange(len(self.bancos))  # Escolhendo indice do banco vendido
            banco_vendido = self.bancos.pop(indice_vendido)  # Selecionando banco vendido

            # se o banco vendido tiver um ativo total igual a 0, vai-se iniciar um loop ate encontrar um banco valido
            while banco_vendido.ativo_total == 0:
                indice_vendido = random.randrange(len(self.bancos))
                self.bancos.append(banco_vendido)
                banco_vendido = self.bancos.pop(indice_vendido)

            banco_comprador.aquisicao(banco_vendido)
            self.bancos.append(banco_comprador)
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

        # setando juros após aquisicoes
        for banco in self.bancos:
            if banco.ativo_total != 0:
                banco.set_juros()

        salvar('acompanhamento.txt', acompanhamento)
        salvar('bancos_vendidos.csv', vendidos)

        # Calculando impacto dos clientes
        for banco in self.bancos:
            # banco 300.000
            percentual = percentual_cliente * banco.carteira_credito  # percentual 6000
            banco.carteira_credito += percentual*banco.numero_clientes

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
