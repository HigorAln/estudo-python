# para da split

# list = ["A", "B", "C", "D", "E", "F"]
# print(list[0:4]) # ou print(list[:4])

# l1 = [1,2,3]
# l2 = [4,5,6]

## para juntar
# print(l1 + l2)
# l1.extend(l2)

## adicionar no final
# l1.append("10")

## adicionar no inicio
# l1.insert(0, "Banana")

## deletar do final
# l1.pop()

## limpar lista
# l1.clear()

## para pegar o maior valor
# print(max(l1))

## para pegar o menor valor
# print(min(l1))

## para criar uma lista rapidamente com a funcao range
# print(list(range(0, 10)))

l2 = [0,1,2,3,4,5,6,7,8,9]

some = 0;
for valor in l2:
    some+=valor

print(some)