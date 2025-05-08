#aula 02 -> variaveis, tipos e input
#Tipos de dados
#String->texto
#Int->inteiro
 #Float-> quebrado

#declaração de variaveis
# escola ="senai"

# #mostrando o valor da variável no print
# #concatenando com o +
# print("o nome da minha escola é"+ escola)
# #separando por parametro
# print("o nome da minha escola é", escola)
# #f string {} -> mostra o valor da variável dentro das aspas
# print(f"o nome da minha escola é {escola}")

# numero=100

# print("somando com 10=" ,numero+10)
# print("subtraind0 5=", numero -5)
# print("dividindo por 2=", numero/2)
# print("multiplicando por 10=", numero *10)
# import os
# os.system("cls")

# nome="Maryah"
# idade= 16
# cpf= 49099409877

# print("Meu nome é", nome)
# print("minha idade é", idade)
# print("meu cpf é", cpf)

import os
os.system("cls")
os.system("color 5")

# #input

# texto= input("digite algo: ")
# print("voce digitou... ", texto)

print("********CADASTRO*******")
texto1= input("digite seu nome: ")
texto2= input("digite seu rg: ")
texto3= input("digite seu cpf: ")
print("********DADOS CADASTRADOS*******")
print("Nome: ", texto1)
print("Rg:", texto2)
print("Cpf:", texto3)
