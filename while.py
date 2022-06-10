


x = 0

while x < 10:
    if x == 3:
        x = x + 1
        continue
        # break - e usado para sair do laco de repeticao e finalizar o while

    print(x)
    x = x + 1

print(f"acabou {x}")


contador = 1

while contador <= 10:
    print(contador)
    contador = contador + 1

else:                       # usado quando a repeticao acaba natualmente, caso a repeticao acabe antes, o else nao sera executado
    print("acabou")