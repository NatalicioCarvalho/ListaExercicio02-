nome = input("Digite seu nome: ")
produto = input("Digite o produto: ")
quantidade = int(input("Digite a quantidade: "))
preco_unitario = float(input("Digite o preço unitário: "))
total = quantidade * preco_unitario
print(f"Compra realizada por {nome}: Produto {produto}, Quantidade {quantidade}, Valor unitário R$ {preco_unitario:.2f} Total R$ {total:.2f}")
