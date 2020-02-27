# receba duas strings e verificam o tamanho e compare

text1 = "Brasil hexa 2006!"
text2 = "Brasil! hexa 2006!"
juntar1 = []
juntar2 = []

for letra in text1:
	juntar1.append(letra)
for letra in text2:
	juntar2.append(letra)
if(juntar1 == juntar2):
	print("Sao iguais!")
else:
	print("Sao diferentes!")

if (len(text1) == len(text2)):
	print("Possuem o mesmo tamanho!")
else:
	print("Nao possuem o mesmo tamanho!")