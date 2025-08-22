# Aula 8 - OBS.: PODE SER FEITO EM 2 AULAS 
# Criar função para vender produto:
# Solicitar nome e quantidade.
# Usar if para verificar se o produto existe e se tem estoque.
# Atualizar a quantidade.

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
        if p["nome"].lower() == nome.lower():  # EXTRA: compara sem diferenciar maiúsc/minúsc
            if p["quantidade"] >= quantidade:
                p["quantidade"] -= quantidade  # EXTRA: -= 
                print(f"\nVenda realizada! Estoque atualizado\n")
            else:
                print("\nEstoque insuficiente!\n")
            break
    else:
        print("\nProduto não encontrado!\n")
    
    

produtos = []

while True:
    print("\n=== Sistema de Controle de Estoque ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Vender produto")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")


    if opcao == "1":
        cadastrar_produto(produtos)

    elif opcao == "2":
        listar_produtos(produtos)

    elif opcao == "3":
        vender_produto(produtos)

    elif opcao == "4":
        print("\nSaindo do sistema...\n")
        break
    else:
        print("Opção inválida!")
