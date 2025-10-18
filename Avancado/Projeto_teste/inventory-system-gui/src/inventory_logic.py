def cadastrar_produto(produtos, nome, preco, quantidade):
    produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
    produtos.append(produto)

def listar_produtos(produtos):
    return produtos

def vender_produto(produtos, nome, quantidade):
    for p in produtos:
        if p["nome"].lower() == nome.lower():
            if p["quantidade"] >= quantidade:
                p["quantidade"] -= quantidade
                return True, "Venda realizada! Estoque atualizado."
            else:
                return False, "Estoque insuficiente!"
    return False, "Produto não encontrado!"