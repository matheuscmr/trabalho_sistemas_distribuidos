class Almoxarifado:
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def pedir_produto(self, id_peca, qdd):
        return id_peca, qdd
