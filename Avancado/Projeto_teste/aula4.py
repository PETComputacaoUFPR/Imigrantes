# Aula 4 - Transformar o menu em um loop que só termina quando o usuário digitar “Sair”.

while True:
    print("=== Sistema de Controle de Estoque ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Vender produto")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")


    if opcao == "1":
        print("Opção de cadastro selecionada.")
    elif opcao == "2":
        print("Opção de listagem selecionada.")
    elif opcao == "3":
        print("Opção de venda selecionada.")
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")