# Products list
produtos = []

def cadastrar_produto(produtos):
    print("\n=== Cadastro de Produto ===")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
    produtos.append(produto)

    print("\nProduto cadastrado!\n")

def listar_produtos(produtos):
    print("\n=== Lista de Produtos ===")
    if len(produtos) == 0:
        print("Não há produtos cadastrados.\n")
    else:
        for p in produtos:  
            print(f"{p['nome']} - R${p['preco']:.2f} - Estoque: {p['quantidade']}")

def vender_produto(produtos):
    print("\n=== Remoção de Produto ===")
    if len(produtos) == 0:
        print("Não há produtos cadastrados.\n")
        return
    
    nome = input("Digite o nome do produto vendido: ")
    quantidade = int(input("Digite a quantidade a vender: "))

    for p in produtos:
        if p["nome"].lower() == nome.lower():
            if p["quantidade"] >= quantidade:
                p["quantidade"] -= quantidade
                print(f"\nVenda realizada! Estoque atualizado\n")
            else:
                print("\nEstoque insuficiente!\n")
            break
    else:
        print("\nProduto não encontrado!\n")