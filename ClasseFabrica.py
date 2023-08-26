class Fabrica:
    def __init__(self, id):
        if (id == 1):
            self.id = 1
            self.LinhaP = []
            for i in range(5):
                buffer_m = []
                for j in range(10):
                    buffer_m.append(0)
                self.LinhaP.append(buffer_m)
        else:
            self.id = 2
            self.LinhaP = []
            for i in range(8):
                buffer_m = []
                for j in range(10):
                    buffer_m.append(0)
                self.LinhaP.append(buffer_m)
    def get_id(self):
        return self.id
    def get_linhas(self):
        return self.LinhaP
    def inserir_material(self, linha,material):
        self.LinhaP[linha][material] = self.LinhaP[linha][material] + 1
    def inserir_materiais(self, linha,material,qtde):
        self.LinhaP[linha][material] = self.LinhaP[linha][material] + qtde
    def get_linha(self, linha):
        return self.LinhaP[linha]
    