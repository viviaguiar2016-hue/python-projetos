def  cal_desconto():
    print('*******Calculadora de desconto*******')

    preco = float(input(f'qual preço do produto: '))
    pecentual = float(input(f'valor aplicado para desconto(0- 100%): '))
    desconto = round(preco* (pecentual/100),2)
    final = round (preco - desconto,2)

    print("-"*25+20*"-")
    print(f'calcule o valor de ${preco}. o valor aplicado de {desconto}%.')
    print(f'o valor do desconto calculado: ${desconto}.')
    print(f'o valor final do produto: ${final}')
    print(f'-'*25+20*'-')

cal_desconto()