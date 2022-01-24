qtd = 10

soma = 0

for n in range(1, qtd+1):
    num = int(input(f' Digite 10 números diferentes até completar {n}/{qtd}: '))
    soma = num + soma
print(f' A soma dos números é: {soma}')

