import random


class Cliente:

    def __init__(self, id, banco=None):
        self.id = id
        #self.preferencia = random.choice(['capilaridade', 'solidez', 'juros'])
        self.banco = banco
