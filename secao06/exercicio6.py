qtd = 10

media = 0

for n in range(1, qtd+1):
    num = int(input(f'Digite 10 números diferentes até completar {n}/{qtd}: '))
    media = media + num
media = media / 10
print(f'A média do resultados é: {media}')
