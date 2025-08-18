# Aula 1 - Menu inicial
#  Criar um menu inicial do sistema, apenas exibindo as opções com print().

print("=== Sistema de Controle de Estoque ===")
print("1 - Cadastrar produto")
print("2 - Listar produtos")
print("3 - Vender produto")
print("4 - Sair")

# Aula 2 - Permitir que o usuário digite uma opção do menu (ainda sem fazer nada com ela).

opcao = input("Escolha uma opção: ")

# Aula 3 - Implementar a lógica básica para escolher o que acontece ao digitar uma opção no menu.

if opcao == "1":
    print("Opção de cadastro selecionada.")
elif opcao == "2":
    print("Opção de listagem selecionada.")
elif opcao == "3":
    print("Opção de venda selecionada.")
elif opcao == "4":
    print("Saindo do sistema...")
else:
    print("Opção inválida!")

        