# Aqui temos os principios da criação das fabricas
class Fabrica:
    def __init__(self, id):
        self.QuantidadeParaFabricar = []  # quantidade de cada produto a ser fabricada
        for i in range(5):
            self.QuantidadeParaFabricar.append(0)
        if (id == 1):
            self.id = 1  # se for a fabrica 1, vai criar 5 linhas de produção
            self.LinhaP = []
            self.Produtos = []
            for i in range(5):
                buffer_m = []  # criação do vetor buffer de materias, a principio tera apenas 10 materiais, cada posição indicará a quantidade de cada material
                buffer_p = []  # criação do vetor buffer de produtos feitos.
                for j in range(10):
                    buffer_m.append(0)
                for j in range(5):
                    buffer_p.append(0)
                self.LinhaP.append(buffer_m)
                self.Produtos.append(buffer_p)
        else:  # aqui faremos a mesma coisa para a fabrica 2, a principal diferença é o numero de linhas de produção
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

    def get_id(self):  # metodo para retornar o id da fabrica
        return self.id

    def get_linhas_m(self):  # metodo para retornar todas as linhas de produção de materias
        return self.LinhaP

    # metodo para retornar uma linha especifica de produção de materiais
    def get_linha_m(self, linha):
        return self.LinhaP[linha]

    # metodo que retorna a quantidade de um material em todas as linhas da fabrica
    def get_material(self, material):
        materiais = []
        if self.get_id() == 1:
            for i in range(5):
                materiais.append(self.LinhaP[i][material])
        else:
            for i in range(8):
                materiais.append(self.LinhaP[i][material])
        return materiais

    # metodo que retorna a quantidade de um material em uma linha especifica da fabrica
    def get_material_from_linha(self, linha, material):
        return self.LinhaP[linha][material]

    def get_linhas_p(self):  # metodo para retornar todas as linhas de produtos finalizados
        return self.Produtos

    # metodo para retornar uma linha especifica de produtos finalizados
    def get_linha_p(self, linha):
        return self.Produtos[linha]

    # metodo para retornar a quantidade de produtos a serem fabricados
    def get_quantidade(self):
        return self.QuantidadeParaFabricar

    # metodo para retornar quantos produtos x devem ser fabricados
    def get_quantidade_p(self, produto):
        return self.QuantidadeParaFabricar[produto]

    # metodo para inserir em uma linha x um material y
    def inserir_material(self, linha, material):
        self.LinhaP[linha][material] = self.LinhaP[linha][material] + 1

    # metodo para inserir em uma linha x um material y uma quantidade z
    def inserir_materiais(self, linha, material, qtde):
        self.LinhaP[linha][material] = self.LinhaP[linha][material] + qtde

    # metodo para remover em uma linha x um material y
    def remover_material(self, linha, material):
        self.LinhaP[linha][material] = self.LinhaP[linha][material] - 1

    # metodo para remover material em uma linha x um material y uma quantidade z
    def remover_materiais(self, linha, material, qtde):
        self.LinhaP[linha][material] = self.LinhaP[linha][material] - qtde

    # metodo para inserir produto finalizado em uma linha x um material y
    def adicionar_produto(self, linha, produto):
        self.Produtos[linha][produto] = self.Produtos[linha][produto] + 1

    # metodo para inserir produto finalizado em uma linha x um material y uma quantidade z
    def adicionar_produtos(self, linha, produto, qtde):
        self.Produtos[linha][produto] = self.Produtos[linha][produto] + qtde

    # metodo para remover produto em uma linha x um material y
    def remover_produto(self, linha, produto):
        self.Produtos[linha][produto] = self.Produtos[linha][produto] - 1

    # metodo para remover produto em uma linha x um material y uma quantidade z
    def remover_produtos(self, linha, produto, qtde):
        self.Produtos[linha][produto] = self.Produtos[linha][produto] - qtde

    # adiciona uma quantidade de produtos x a serem produzidos
    def adicionar_quantidade(self, produto, quantidade):
        self.QuantidadeParaFabricar[produto] = self.QuantidadeParaFabricar[produto] + quantidade

    # adiciona uma quantidade de produtos x a serem produzidos
    def remover_quantidade(self, produto, quantidade):
        self.QuantidadeParaFabricar[produto] = self.QuantidadeParaFabricar[produto] - quantidade
        print("-1 produto a fazer ...")

    def fabricar_produto(self, linha, produto):

        for i in range(10):  # verifica se tem todos os materias
            if (self.get_material_from_linha(linha, i) <= 0):
                print("materias insuficientes... ")
                return
        for i in range(10):  # tendo todos materias, remove eles da linha
            self.remover_material(linha, i)
        # remove um produto da fábrica a ser feito
        self.remover_quantidade(produto, 1)
        print("materiais utilizados ...")
        print("fabricando produto ...")
        # adiciona o produto ao buffer no final da linha
        self.adicionar_produto(linha, produto)
        print("produto ", produto, " na linha ", linha, " finalizado ...")

    def enviar_produto(self, linha, produto):
        qtd_p = self.get_linha_p(linha)
        if (qtd_p[produto] >= 1):  # verifica se tem o produto no buffer da linha
            self.remover_produto(linha, produto)
            print("produto ", produto, " da linha ",
                  linha, " enviado para o estoque ...")
        else:
            print("erro, produto não estava na linha")

    def enviar_produtos(self, linha, produto):
        qtd_p = self.get_linha_p(linha)
        if (qtd_p[produto] >= 1):  # verifica se tem o produto no buffer da linha
            self.remover_produtos(linha, produto, qtd_p[produto])
            print("produto ", produto, " da linha ",
                  linha, " enviado para o estoque ...")
        else:
            print("erro, produto não estava na linha")
