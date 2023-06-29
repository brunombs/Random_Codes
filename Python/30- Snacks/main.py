from content import produtos

# Variável para registrar o valor das vendas
valor_vendas = 0.0

# Exibição das categorias disponíveis
print("Bem-vindo(a) à máquina de snacks!")

while True:
    print("Selecione uma categoria:")
    categorias = list(produtos.keys())
    for indice, categoria in enumerate(categorias):
        print(str(indice+1) + "- " + categoria.capitalize())

    # Solicitação da categoria ao usuário
    while True:
        categoria_escolhida = input("Digite o número da categoria desejada: ")

        # Verificação da entrada da categoria
        if categoria_escolhida.isdigit() and int(categoria_escolhida) <= len(categorias):
            categoria_selecionada = categorias[int(categoria_escolhida) - 1]
            break
        else:
            print("Categoria inválida. Por favor, tente novamente.")

    while True:
        # Exibição dos produtos disponíveis na categoria escolhida
        produtos_categoria = produtos[categoria_selecionada]
        print("Produtos disponíveis na categoria:", categoria_selecionada)
        for indice, (produto, preco) in enumerate(produtos_categoria.items()):
            print(str(indice+1) + "- " + produto + " (Preço: R$ %.2f)" % preco)

        # Solicitação do número do produto ao usuário
        while True:
            numero_produto = input("Digite o número do produto desejado: ")

            # Verificação do número do produto
            if numero_produto.isdigit() and int(numero_produto) <= len(produtos_categoria):
                produto_escolhido = list(produtos_categoria.keys())[int(numero_produto) - 1]
                preco_produto = produtos_categoria[produto_escolhido]
                print("Você escolheu:", produto_escolhido)
                print("Preço: R$ %.2f" % preco_produto)

                # Atualização do valor das vendas
                valor_vendas += preco_produto

                break
            else:
                print("Número de produto inválido. Por favor, tente novamente.")

        # Solicitação se deseja escolher mais algum produto
        while True:
            resposta = input("Deseja escolher mais algum produto dessa categoria? (S/N): ").upper()
            if resposta == "N":
                break
            elif resposta == "S":
                break
            else:
                print("Resposta inválida. Por favor, responda com S ou N.")

        if resposta == "N":
            break

    # Solicitação se deseja escolher outra categoria
    while True:
        resposta = input("Deseja escolher outra categoria? (S/N): ").upper()
        if resposta == "N":
            print("Encerrando o programa...")
            print("Valor total das vendas: R$ %.2f" % valor_vendas)
            exit()
        elif resposta == "S":
            break
        else:
            print("Resposta inválida. Por favor, responda com S ou N.")
            