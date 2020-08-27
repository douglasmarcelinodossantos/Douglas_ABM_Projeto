import random


class Cliente:

    def __init__(self, id, banco=None):
        self.id = id
        self.banco = banco
        self.taxa_aceite = random.randint(150, 450) / 10
