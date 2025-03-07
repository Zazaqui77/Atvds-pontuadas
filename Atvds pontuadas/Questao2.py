import os

os.system("clear")

#Solicitar dadosestado_civil :
dados=0
estado_civil =str(input("Digite seu estado civil : "))
sexo=str(input("Digite seu sexo: "))
if estado_civil=="casado(a)":
 dados=str(input("Digite seu tempo de casado(a)"))
 
else:
    print("Obrigado pelas informações")

#exxibindo resultados
print(f"estado_civil:{estado_civil}")
print(f"sexo:{sexo}")
print(f"dados: {dados}")