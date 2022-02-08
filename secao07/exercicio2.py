lista6 = []
numero = ' '

while len(lista6) < 6:
    print("Digite um número:  ")
    numero = input()
    if len(lista6) < 6:
        lista6.append(numero)
print(lista6)

