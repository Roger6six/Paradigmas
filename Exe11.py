dia = int(input("Informe o dia de nascimento: "))
mes = int(input("Informe o mes de nascimento: "))
ano = int(input("Informe o ano de nascimento: "))
m = "Janeiro Fev Março Abril Maio Jun Jul Agost Setem Out Nov Dez"
m2 = m.split()

print("Data de nascimento: %i/ %i/ %i"%(dia,mes,ano))
print("Voce nasceu em",dia,"de",m2[mes-1]," ",ano)
