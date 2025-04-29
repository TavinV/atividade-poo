class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    
    def mostrar_info(self):
        return f"{self.nome}: {self.quantidade} unidades - R$ {self.preco:.2f} cada"

    def atualizar_preco(self, novo_preco):
        print(f"Atualizando preço de {self.nome} de R$ {self.preco:.2f} para R$ {novo_preco:.2f}")
        self.preco = novo_preco


class Estoque:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto {produto.nome} adicionado ao estoque!")
    
    def listar_produtos(self):
        print("\nLista de Produtos no Estoque:")
        for produto in self.produtos:
            print(produto.mostrar_info())
        
    def valor_total(self):
        total = sum(p.quantidade * p.preco for p in self.produtos)
        print(f"\nValor total do estoque: R$ {total:.2f}")
        return total

    def atualizar_preco_produto(self, nome_produto, novo_preco):
        for produto in self.produtos:
            if produto.nome.lower() == nome_produto.lower():
                produto.atualizar_preco(novo_preco)
                return
        print(f"Produto '{nome_produto}' não encontrado no estoque.")

    def relatorio_completo(self):
        print("\nRelatório Completo do Estoque:")
        total_geral = 0
        for produto in self.produtos:
            valor_total_produto = produto.quantidade * produto.preco
            total_geral += valor_total_produto
            print(f"{produto.nome} - {produto.quantidade} unidades x R$ {produto.preco:.2f} = R$ {valor_total_produto:.2f}")
        print(f"\nValor total geral do estoque: R$ {total_geral:.2f}")


# Produtos
arroz = Produto("Arroz", 50, 5.99)
feijao = Produto("Feijao", 30, 8.50)
acucar = Produto("Acucar", 40, 3.75)

# Criando o estoque
meu_estoque = Estoque()

# Adicionando produtos
meu_estoque.adicionar_produto(arroz)
meu_estoque.adicionar_produto(feijao)
meu_estoque.adicionar_produto(acucar)

# Listando produtos
meu_estoque.listar_produtos()

# Atualizando preço
meu_estoque.atualizar_preco_produto("Feijao", 9.20)

# Exibindo relatório completo
meu_estoque.relatorio_completo()
