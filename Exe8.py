#Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
#para o sindicato, faça um programa que nos dê:
#- Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido#

valor_hora = int(input('Quanto voce ganha por hora? '))
horas_mes = int(input('Quantas horas voce trabalha por mes?' ))

salario_bruto = valor_hora * horas_mes
ir = (11/100) * salario_bruto
inss = (8/100) * salario_bruto
sindicato = (5/100) * salario_bruto
salario_liquido = salario_bruto - (ir + inss + sindicato)

print(
    '- Salario bruto : R$',
    salario_bruto
)

print(
    '- IR : R$',
    ir
)

print(
    '- INSS : R$',
    inss
)

print(
    '- Sindicatos : R$',
    sindicato
)

print(
    '- Salario liquido : R$',
    salario_liquido
)