import os
os.system("cls")

#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)


#EXERCICIOS IF ELSE
# exercicio1

# idade=float(input("digite sua idade:"))
 
# if idade > 18 :
#      print("maior de idade")

# # else:
# #      print("menor de idade")




# #exercicio2


# # idade=float(input("digite sua idade:"))
 
# if idade == 0 or idade > 120 :
#      print("idade invalida")

# else:
#      print("idade valida")






#exercicio3
# email=input(("digite seu email:"))
# senha= float(input("digite sua senha:"))

# if "python@senai.com" == email:
#     if "12345678" == senha:
       
#         print("USUARIO AUTENTICADO")
 
# else:
#     print("USUARIO ou senha Inválidos") 



# print("HORTIFRUTTI APPLE JACK ")
# qt= int (input("Digite a quantidade de maças:"))

# if qt < 12:
#      calc=qt*0.30
#      print("voce ira pagar (0,30 uni) : R$ ", calc)
# else:
#      calc=qt*0.25
#      print("voce ira pagar (0,25 uni) : R$ " , calc)


# ***********exercicio1***********

#vog= (input("Digite uma letra:"))

# if vog == "a"  or vog == "A" or  vog =="e" or vog == "E" or  vog =="i" or vog == "I" or vog =="o" or vog == "O" or vog =="u" or vog == "U" :
#      print("essa letra é uma vogal")

# else: 
#      print("essa letra é uma consoante")

     

# ***********exercicio2***********

# n1= input("digite um mumero:")
# n2= input("digite outro numero:")

# if n1<n2:
#     print(f"o numero maior é {n2}")
#     print(f"o numero menor é {n1}")

# else:
#      print(f"o numero maior é {n1}")
#      print(f"o numero menor é {n2}")


#REESCREVENDO DE OUTRA MANEIRA
#and(e) or(e) in(dentro) -> Apenas pra string
l=input("digite uma letra: ")

if l in "aeiouAEIOU":
     print("vogal")
else:
     print("consoante")