import os

os.system("clear")

print("""
====================MENU===============
     \t\Frutas  \t\ preço ate 5kg   \t\ preço acima 5kg
    
1   \t\maça     \t\t2,50             \t\2,20
2   \t\morango   \t\t1,80            \t\1,50  
""")

quant_morango   = float(input("Digite a quantidade de morango: "))
quant_maca = float(input("Digite a quantidade de maçã: "))

maca = float(2.50)
macav = float(2.20)
morango = float(1.80)
morango2 = float(1.50)

if quant_maca or quant_morango <=5:
    total=(quant_morango*morango)+(quant_maca*macav)
    print(f"total:{total} ")
elif quant_maca or morango > 8:
    total=(quant_morango*morango)+(quant_maca*macav)
    Total_final=(total*10)
    print(f"valor a ser pago: {Total_final} ")
