total = 10
media = 0
print('Números Negativos são descartados!')
for n in range( 1,11):
    num = int(input(f'Digite seu {n}º número positivo: '))
    if num > 0:
        media = media + num
media = media / 10
print(f'A média é {media}')
