class Fornecedor:
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def liberar_produto(self, id_peca, qdd):
        return id_peca, qdd
