lista = []
listaquadrado = []
num = ' '

while num != 0:
    print('Digite um número real ou digite "0"(número zero) para sair.')
    num = float(input())
    if num > 0:
        lista.append(num)
        listaquadrado.append(num**2)
    if num == 0:
        print("Voce saiu do programa e, portanto, sua lista de números ficou da seguinte forma:")

print(f'Sua lista é: {lista}')
print(f'O valor ao quadrado dos intens de sua lista é: {listaquadrado}')


