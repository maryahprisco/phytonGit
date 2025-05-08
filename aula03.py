import os
os.system("cls")

#continuação input com int e float
#int() ->converte pra inteiro
#float() ->converte pra n quebrado

# numero= 10
# numero2=input("digite um numero:")
# print("o tipo de numero é  ")
# soma= numero+ int(numero2) 
# print(f"soma de {numero}+{numero2} =", soma)

# #exemplo2
# num1= input("digite um numero: ")
# soma= float(num1) +15
# print("a soma de", num1, "+", "15", "=", soma)

#exemplo3
# n1= float(input("digite um numero"))
# n2= float(input("digite outro numero:"))

# soma= n1+n2

# print(f"a soma de {n1} + {n2}=", soma)


#ATIV1
# n1= float(input("digite um numero:"))
# n2= float(input("digite outro numero:"))
# multiplicacao= n1*n2

# print(f"a multiplicacao de {n1} * {n2} é", multiplicacao )

#ATIV2
# n1= float(input("digite um numero:"))
# print (f"antecessor: {n1-1},")
# print (f"sucessor: {n1+1},")

#ATIV3
# n1= float(input("digite seu ano de nascimento:"))
# print (f"sua idade é {2025-n1}")

#porcentagem
# print("25%de 100+", 0.25*100)
# print("4% de 400=", 0.04*400)
# print("99% de 1525", 0.99*1525)

# #supondo que um produto custa 150 reais e o caixa deu um 
# #descontp de 15%
# exemplo = float(input("digite o preço do produto:"))
# desconto= 0.15*exemplo
# print("o preço do produto é: ", exemplo-desconto)

# ATIV%
print("===================SUPERMERCADO===================")

item1=(input("digite o nome do produto:"))
valor1=float(input("preço:"))
item2= (input("digite o nome do produto:"))
valor2=float(input("preço:"))

desconto10= valor1*0.10
desconto25= valor2*0.25

print(f"o valor de {item1} com 10% de desconto: {valor1-desconto10}")
print(f"o valor de {item2} com 25% de desconto: {valor2-desconto25}")


total=round(valor1-desconto10 + valor2-desconto25, 2)


print("===================TOTAL===================")
print(f"total: {total} ")




#round(valor,qtdcasasdecimais) -> faz o arredondamento dos valores