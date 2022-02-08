lista = []
numero = ' '

while len(lista) < 8:
    print("Digite um número:  ")
    numero = int(input())
    if len(lista) < 8:
        lista.append(numero)
print('Agora, digite o valor X e o valor Y, que são utilizados para verificar a posição no vetor: ')
print('Valor X: ')
valorX = int(input())
if valorX <= 8:
    print('Valor Y: ')
    valorY = int(input())
    if valorY <= 8:
        soma = lista[valorX] + lista[valorY]
        print(f'O valor da soma dos índices selecionados em X e Y é: {soma}')
    if valorY > 8:
        print('Digite apenas números entre 0 e 8.')
else:
    print('Digite apenas números entre 0 e 8.')
