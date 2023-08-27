class Estoque:
    def __init__(self):
        self.Estoque = 0
        self.Pedidos = 0


    def get_Estoque(self):
        return self.Estoque
    
    def get_Pedidos(self):
        return self.Pedidos

    def add_Estoque(self,quantidade):
        self.Estoque = self.Estoque + quantidade
    
    def add_Pedidos(self,quantidade):
        self.Pedidos = self.Pedidos + quantidade

    def remove_Estoque(self,quantidade):
        self.Estoque = self.Estoque - quantidade

    def remove_Pedidos(self,quantidade):
        self.Pedidos = self.Pedidos - quantidade
    
    