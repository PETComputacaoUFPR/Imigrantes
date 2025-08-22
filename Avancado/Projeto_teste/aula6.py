# Aula 6 - Alterar a estrutura para que cada produto seja um dicionário com nome, preço e quantidade.
# Exemplo: {"nome": "Arroz", "preco": 5.99, "quantidade": 10}
# Adaptar o cadastro para preencher todos esses campos.

produtos = []

while True:
    print("\n=== Sistema de Controle de Estoque ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Vender produto")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")


    if opcao == "1":
        print("\n=== Cadastro de Produto ===")
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade em estoque: "))

        produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
        produtos.append(produto)

        print("Produto cadastrado!\n")

    elif opcao == "2":
        print("\n=== Lista de Produtos ===")
        if len(produtos) == 0:
            print("Não há produtos cadastrados.\n")
        else:
            for p in produtos:  
                print(f"{p['nome']} - R${p['preco']:.2f} - Estoque: {p['quantidade']}")

    elif opcao == "3":
        print("\nOpção de venda selecionada.")

    elif opcao == "4":
        print("\nSaindo do sistema...\n")
        break
    else:
        print("Opção inválida!")