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


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

continuar = True
produtos = []
estoque = Estoque()

while continuar:
    print("\nMenu de Opções:")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Preço de Produto")
    print("4. Valor Total do Estoque")
    print("5. Relatório Completo")
    print("6. Sair\n")
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        nome_produto = input("Nome do produto: ").strip().capitalize()
        quantidade_produto = int(input("Quantidade: ").strip())
        preco_produto = float(input("Preço: R$ ").strip())
        novo_produto = Produto(nome_produto, quantidade_produto, preco_produto)
        
        estoque.adicionar_produto(novo_produto)
        produtos.append(novo_produto)

        clear()
        print(f"Produto {nome_produto} criado com sucesso!")

    elif opcao == "2":
        if len(produtos) == 0:
            print("Nenhum produto adicionado!")
        else:
            clear()
            print("\nLista de Produtos:")
            for produto in produtos:
                print(produto.mostrar_info())
    
    elif opcao == "3":
        if len(produtos) == 0:
            clear()
            print("Nenhum produto adicionado!")
        else:
            nome_produto = input("Nome do produto: ").strip().capitalize()
            for produto in produtos:
                if produto.nome == nome_produto:
                    preco_produto = float(input("Novo preço: R$ ").strip())
                    clear()
                    produto.atualizar_preco(preco_produto)
                    break
            else:
                clear()
                print(f"Produto '{nome_produto}' não encontrado!")
    
    elif opcao == "4":
        if len(produtos) == 0:
            clear()
            print("Nenhum produto adicionado!")
        else:
            clear()
            estoque.valor_total()
    
    elif opcao == "5":
        if len(produtos) == 0:
            clear()
            print("Nenhum produto adicionado!")
        else:
            clear()
            print("\nRelatório Completo do Estoque:")
            estoque.relatorio_completo()
    
    elif opcao == "6":
        clear()
        print("Saindo do programa...")
        continuar = False
    