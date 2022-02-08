# Exercício 6

celsius = float(input('Digite a temperatura em Graus Celsius: '))
fahrenheit = celsius *(9.0/5.0) + 32.0
print(f'A temperatura convertida de Celsius para Fahrenheit é {fahrenheit}')

# Exercício 26

areametros = float(input('Digite o valor da área em m²: '))
areahectares = areametros * 0.0001
print(f'O valor de área de {areametros}m² convertidos para hectares é de {areahectares}. ')

# Exercício 37
valorproduto = float(input('Para aplicar o desconto, digite o valor do produto: '))
valor = valorproduto * 12/100
valordesconto = valorproduto - valor
print(f'O valor do produto com desconto de 12% fica: R$ {valordesconto}')
