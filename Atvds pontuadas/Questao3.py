import os

os.system("Clear")

numero_um = int(input("Digite o numero um: "))
numero_dois = int(input("Digite o numero_dois"))

#Verificando dados

if numero_um == numero_dois :
    soma = numero_um + numero_dois
    print(f"Valor da soma: {soma}")
else:
 multiplicacao = numero_um * numero_dois
 print(f"valor da multiplicação: {multiplicacao}")

 print(f"valor do numero_um: {numero_um}")
 print(f"valor do numero_dois: {numero_dois}")