#Aqui temos os principios da criação das fabricas
class Fabrica:
    def __init__(self, id):
        self.QuantidadeParaFabricar = [] #quantidade de cada produto a ser fabricada
        for i in range(5):
            self.QuantidadeParaFabricar.append(0)
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

    def get_quantidade(self): # metodo para retornar a quantidade de produtos a serem fabricados
        return self.QuantidadeParaFabricar

    def get_quantidade_p(self,produto): # metodo para retornar quantos produtos x devem ser fabricados
        return self.QuantidadeParaFabricar[produto]

    def inserir_material(self, linha,material): # metodo para inserir em uma linha x um material y
        self.LinhaP[linha][material] = self.LinhaP[linha][material] + 1

    def inserir_materiais(self, linha,material,qtde):# metodo para inserir em uma linha x um material y uma quantidade z
        self.LinhaP[linha][material] = self.LinhaP[linha][material] + qtde

    def remover_material(self, linha,material): # metodo para remover em uma linha x um material y
        self.LinhaP[linha][material] = self.LinhaP[linha][material] - 1

    def remover_materiais(self, linha,material,qtde):# metodo para remover material em uma linha x um material y uma quantidade z
        self.LinhaP[linha][material] = self.LinhaP[linha][material] - qtde
    
    def adicionar_produto(self, linha,material): # metodo para inserir produto finalizado em uma linha x um material y
        self.Produtos[linha][material] = self.Produtos[linha][material] + 1

    def adicionar_produtos(self, linha,material,qtde):# metodo para inserir produto finalizado em uma linha x um material y uma quantidade z
        self.Produtos[linha][material] = self.Produtos[linha][material] + qtde

    def remover_produto(self, linha,produto): # metodo para remover produto em uma linha x um material y
        self.Produtos[linha][produto] = self.Produtos[linha][produto] - 1

    def remover_produtos(self, linha,produto,qtde):# metodo para remover produto em uma linha x um material y uma quantidade z
        self.Produtos[linha][produto] = self.Produtos[linha][produto] - qtde

    def adicionar_quantidade(self,produto,quantidade): # adiciona uma quantidade de produtos x a serem produzidos
        self.QuantidadeParaFabricar[produto] = self.QuantidadeParaFabricar[produto] + quantidade
    
    def remover_quantidade(self,produto,quantidade): # adiciona uma quantidade de produtos x a serem produzidos
        self.QuantidadeParaFabricar[produto] = self.QuantidadeParaFabricar[produto] - quantidade
        print("-1 produto a fazer ...")

    def fabricar_produto(self,linha,produto):
        
        for i in range(10): # verifica se tem todos os materias
            if(self.get_material_from_linha(linha,i)<=0):
                print("materias insuficientes... ")
                return
        for i in range(10): # tendo todos materias, remove eles da linha
            self.remover_material(linha,i)
        self.remover_quantidade(produto,1) #remove um produto da fábrica a ser feito
        print("materiais utilizados ...")
        print("fabricando produto ...")
        self.adicionar_produto(linha,produto) # adiciona o produto ao buffer no final da linha
        print("produto ", produto," na linha ",linha," finalizado ...")
    
    def enviar_produto(self,linha,produto):
        qtd_p = self.get_linha_p(linha)
        if(qtd_p[produto]>=1): #verifica se tem o produto no buffer da linha
            self.remover_produto(linha,produto)
            print("produto ", produto," da linha ",linha, " enviado para o estoque ...")
        else:
            print("erro, produto não estava na linha")