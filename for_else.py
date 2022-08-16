variavel = ["Higor Allan", "Joao", "Maria", "Pedro"]

comeca_com_j = False

for valor in variavel:
    if valor.lower().startswith("j"):
        comeca_com_j = True


if comeca_com_j:
    print("Existem nomes que começam com J")
else:
    print("Não existem nomes que começam com J")