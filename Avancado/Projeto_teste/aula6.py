# Aula 6 - Alterar a estrutura para que cada produto seja um dicionário com nome, preço e quantidade.
# Exemplo: {"nome": "Arroz", "preco": 5.99, "quantidade": 10}
# Adaptar o cadastro para preencher todos esses campos.

produtos = []

while True:
    print("=== Sistema de Controle de Estoque ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Vender produto")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")


    if opcao == "1":
        print("Opção de cadastro selecionada.")
        nome = input("Digite o nome do produto: ")
        produtos.append(nome)
        print("Produto cadastrado!\n")
    elif opcao == "2":
        print("Opção de listagem selecionada.")
        print("Produtos cadastrados:")
        for p in produtos:
            print("-", p)
            print("\n")
    elif opcao == "3":
        print("Opção de venda selecionada.")
    elif opcao == "4":
        print("Saindo do sistema...\n")
        break
    else:
        print("Opção inválida!")