print('Digite 10 números')

for i in range(1, 11):
    num = int(input(f'Digite seu {i}º número: '))
    if i == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f'O maior número é {maior} e o menor número é {menor}')
