funcionarios = ["Diogo", "Diego", "Douglas", "Daiane", "Daniela", "Ferreira", "José", "Viviane", "Ronilda"]

produtos = ["Iphone 14", "Ipad", "Mac Book", "Apple Watch"]

quantidades_produtos_vendido = [
    [10, 25, 36, 30],
    [52, 60, 25, 90],
    [20, 36, 85, 96],
    [6, 44, 96, 150],
    [20, 25,69 ,80],
    [85, 74, 96 ,10],
    [25, 58, 96, 41],
    [52, 74, 96, 20],
    [10, 5, 74, 30]

]

for i, funcionario in enumerate(funcionarios):
    print("-------------- Vendas ------------------")
    print(f"O funcionário {funcionario}:")
    print(f"{quantidades_produtos_vendido[i][0]} unidades de {produtos[0]}")
    print(f"{quantidades_produtos_vendido[i][1]} unidades de {produtos[1]}")
    print(f"{quantidades_produtos_vendido[i][2]} unidades de {produtos[2]}")
    print(f"{quantidades_produtos_vendido[i][3]} unidades de {produtos[3]}")
    print("----------------------------------------")
    print()


estoque = [10, 50, 60, 90, 40, 60, 14, 5, 10]
produtos = ["Coca-cola", "Pepsi", "Fanta Uva", "Cerveja Brahma", "Suco de Laranja", "Guarana Antartica", "Fanta Laranja", "Fanta Guarana", "Guaranita"]

quantidade_minima = 25;

for i, qtd in enumerate(estoque):
    if qtd < quantidade_minima:
        print(f"O produto {produtos[i]} está a baixo do estoque.")
        print("Por favor fazer um pedido para repor a quantidade em estoque!")
        print()