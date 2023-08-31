class Almoxarifado:
    def __init__(self, id):
        self.id = id
        self.estoque = 0
        self.fabricarProdutos = 0 #quantidade de produtos a serem fabricados

    def get_id(self):
        return self.id

    def get_estoque(self):
        return self.estoque
    
    def get_fprodutos(self):
        return self.fabricarProdutos
    
    def set_fprodutos(self,qdd):
        self.fabricarProdutos = qdd

    def add_estoque(self,qdd):
        self.estoque = self.estoque + qdd

    def remove_estoque(self,qdd):
        self.estoque = self.estoque - qdd

