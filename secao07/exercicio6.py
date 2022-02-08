lista = []
numero = ' '

while len(lista) < 10:
    print("Digite um número:  ")
    numero = int(input())
    if len(lista) < 10:
        lista.append(numero)
lista.sort()
print(lista)
print(f'o menor número da lista é: {lista[0]} e o maior número da lista é: {lista[9]}')
