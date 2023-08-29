class Almoxarifado:
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def pegar_produto(self, id_peca, qdd):  # inicialmente, ele tem produtos infinitos
        return id_peca, qdd
