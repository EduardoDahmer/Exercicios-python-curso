lista = []
numero = ' '

while len(lista) < 10:
    print("Digite um número:  ")
    numero = int(input())
    if len(lista) < 10:
        lista.append(numero)
print(f'Sua lista é {lista}')
numpar, numimpar = 0, 0
for num in lista:
    if num % 2 == 0:
        numpar += 1
    else:
        numimpar +=1
print(f'Na sua lista, há {numpar} números pares e {numimpar} números impares')
