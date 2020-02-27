nome = ""
s = ""

nome = input("Informe o nome:")

for letra in reversed(nome):
	s+=letra
print(s.upper())