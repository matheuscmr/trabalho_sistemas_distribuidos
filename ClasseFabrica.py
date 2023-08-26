#Aqui temos os principios da criação das fabricas
class Fabrica:
    def __init__(self, id):
        if (id == 1):
            self.id = 1  # se for a fabrica 1, vai criar 5 linhas de produção
            self.LinhaP = []
            self.Produtos = []
            for i in range(5):
                buffer_m = [] # criação do vetor buffer de materias, a principio tera apenas 10 materiais, cada posição indicará a quantidade de cada material
                buffer_p = [] # criação do vetor buffer de produtos feitos.
                for j in range(10):
                    buffer_m.append(0)
                for j in range(5):
                    buffer_p.append(0)
                self.LinhaP.append(buffer_m)
                self.Produtos.append(buffer_p)
        else: # aqui faremos a mesma coisa para a fabrica 2, a principal diferença é o numero de linhas de produção
            self.id = 2
            self.LinhaP = []
            self.Produtos = []
            for i in range(8):
                buffer_m = []
                buffer_p = []
                for j in range(10):
                    buffer_m.append(0)
                for j in range(5):
                    buffer_p.append(0)
                self.LinhaP.append(buffer_m)
                self.Produtos.append(buffer_p)
    def get_id(self): # metodo para retornar o id da fabrica 
        return self.id
    
    def get_linhas_m(self): # metodo para retornar todas as linhas de produção de materias
        return self.LinhaP

    def get_linha_m(self, linha): # metodo para retornar uma linha especifica de produção de materiais
        return self.LinhaP[linha]
    
    def get_material(self, material): # metodo que retorna a quantidade de um material em todas as linhas da fabrica
        materiais = []
        if self.get_id() == 1:
            for i in range(5):
                materiais.append(self.LinhaP[i][material])
        else:
            for i in range(8):
                materiais.append(self.LinhaP[i][material])
        return materiais
    
    def get_material_from_linha(self,linha,material): # metodo que retorna a quantidade de um material em uma linha especifica da fabrica
        return self.LinhaP[linha][material]

    def get_linhas_p(self): # metodo para retornar todas as linhas de produtos finalizados
        return self.Produtos

    def get_linha_p(self, linha): # metodo para retornar uma linha especifica de produtos finalizados
        return self.Produtos[linha]

    def inserir_material(self, linha,material): # metodo para inserir em uma linha x um material y
        self.LinhaP[linha][material] = self.LinhaP[linha][material] + 1

    def inserir_materiais(self, linha,material,qtde):# metodo para inserir em uma linha x um material y uma quantidade z
        self.LinhaP[linha][material] = self.LinhaP[linha][material] + qtde
    