def Calc(number1, number2):
    return number1*number2

print(Calc(2,26))

print("{0} - {1} - {2}".format(2,26,52))
print("{i} - {n} - {o}".format(i=2, n=26, o=Calc(2,26)))
print(f"{2} - {26} - {Calc(2,26)}")

message = f'''
Um texto giagnet
aqui dentro
como
exemplo
de como ficaria
um texto
com quebra
de linha
'''

print(message)