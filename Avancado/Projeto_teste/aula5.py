# Aula 5 - Criar uma lista para armazenar os produtos (por enquanto, apenas o nome).
# Criar a opção para adicionar produtos à lista (só nome no início).
# Implementar a opção do menu para listar os produtos cadastrados.

produtos = []

while True:
    print("=== Sistema de Controle de Estoque ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Vender produto")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")


    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        produtos.append(nome)
        print("Produto cadastrado!\n")
    elif opcao == "2":
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