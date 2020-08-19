import random

class Banco:

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
        self.taxa_juros = 0

    def set_juros(self):
        self.taxa_juros = random.randint(150, 450) / 10  # Gerando taxa de juros aleatoria entre 15% e 45%

    def __str__(self):
        objeto = self.nome + "\nAtivo Total: " + self.ativo_total.__str__() + "\nCarteira de Credito: " + self.carteira_credito.__str__() + "\nPassivo Circulante: " + self.passivo_circulante.__str__() + "\nCaptações: " + self.captacoes.__str__() + "\nPatrimonio: " + self.patrimonio_liquido.__str__() + "\nLucro Liquido: " + self.lucro_liquido.__str__() + "\nNumero de Agencias: " + self.numero_agencias.__str__() + "\nNumero de Postos: " + self.numero_postos.__str__()
        return str(objeto)

    def aquisicao(self, banco_comprado):
        self.ativo_total += banco_comprado.ativo_total
        self.carteira_credito += banco_comprado.carteira_credito
        self.passivo_circulante += banco_comprado.passivo_circulante
        self.captacoes += banco_comprado.captacoes
        self.patrimonio_liquido += banco_comprado.patrimonio_liquido
        self.lucro_liquido += banco_comprado.lucro_liquido
        self.numero_agencias += banco_comprado.numero_agencias
        self.numero_postos += banco_comprado.numero_postos
        self.numero_clientes += banco_comprado.numero_clientes

    def exporter(self):
        return [self.nome, self.ativo_total, self.carteira_credito, self.passivo_circulante, self.captacoes,
                self.patrimonio_liquido, self.lucro_liquido, self.numero_agencias, self.numero_postos]
