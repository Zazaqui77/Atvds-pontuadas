import os 
os.system("clear")

#Solicitar dados 
numero_um = int(input("Digite o numero um: "))
numero_dois = int(input("Digite o numero dois: "))
numero_tres = int(input("Digite o numero tres: "))

#Verificiando dados :
soma = numero_um + numero_dois 
if soma > numero_tres:
    print("primeiro numero e segundo numero maior que o terceiro numero")

else:
    print("terceiro numero maior que um e dois")

#exebir resultados 
print(f"numero_um escolhido: {numero_um}")
print(f"numero_dois escolhido: {numero_dois}")
print(f"numero_tres escolhido: {numero_tres}")