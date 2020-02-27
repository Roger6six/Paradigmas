#Peso maior que 50 quilos deve pagar uma multa de 4 reais por quilo

peso = int(input('Joao, quanto quilos de peixe voce vai levar? '))


if peso > 50.00:
    print('Existe um excesso')
    multa = (peso - 50) * 4
    print('Valor da multa e R$ ', multa)
else:
    print('A quantidade esta correta nao existe multas')
