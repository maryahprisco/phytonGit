import os
os.system("cls")

#IF ENCADEADO
#EL IF


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# # ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
# #  SE MENOR QUE 12 -> CRIANÇA
# #  SE MENOR QUE 18 -> ADOLESCENTE
# #  SE MENOR QUE 60 -> ADULTO
# #  SE NAO -> IDOSO


# # NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# # SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")




#**********exercicio**********

# nota1= float(input("Digite a primeira nota: ").replace (",","."))
# nota2= float(input("Digite a segunda nota: ").replace (",","."))

# media= (nota1+nota2)/2

# if media <=5:
#     print(f"Sua média é {media: .2f}: ")
#     print("Reprovado")

# elif media >5 and media <7:
#     print (f"Sua média é {media: .2f}: ")
#     print("Em recuperação")

# elif media > 7:
#     print(f"Sua media é {media: .2f}:")
#     print("Aprovado!")

#: .2f formata para duas caas decimais apenas no fstring


#**********exercicio2**********

# peso=float(input("Digite seu peso:") .replace (",","."))
# alt= float(input("Digite sua altura:") .replace (",","."))

# imc= round(peso/(alt*alt) ,2)

# if imc < 17:
#     print(f"seu IMC é {imc}")
#     print("Você esta muito abaixo do peso")
   
# elif imc >18.5 and  imc <24.99:
#     print(f"seu IMC é {imc}")
#     print("Você esta com peso normal")

# elif imc >25 and  imc <29.99:
#     print(f"seu IMC é {imc}")
#     print("Você esta acima do peso")

# elif imc >30 and  imc <34.99:
#     print(f"seu IMC é {imc}")
#     print("Você esta com obesidade I ")
   
# elif imc >35 and  imc <39.99:
#     print(f"seu IMC é {imc}")
#     print("Você esta com obesidade II ")  

# else:
#     print("Você esta com obesidade III (morbida)")


#**********exercicio3**********

print(r"""

                                                                                                                                                                                                        
         _______      
       //  ||\ \     
 _____//___||_\ \___ 
 )  _          _    \
 |_/ \________/ \___|
___\_/________\_/___  """)

sal= float(input("Digite seu salário:").replace (",","."))

aum20= sal*0.20
aum15= sal* 0.15
aum10= sal*0.10
aum5= sal*0.05

print("Salários até R$ 2799,99 :aumento de 20%;")
print("Salários entre R$ 2800,00 e R$6999,99: aumento de 15%;")
print("Salários entre R$ 7000,00 e R$ 14999,99: aumento de 10%;")
print(" Salários de R$ 15000,00 em diante: aumento de 5%")

if sal <2799.99 :
    print (f"Seu salário era {sal}")
    print (f"O percentual de aumento é 20%")
    print (f"O valor do aumento é {sal-aum20}")
    print (f"Seu novo salário é {sal+aum20}.")
elif sal >2800.00 and sal<6999.99 :
    print (f"Seu salário era {sal}")
    print (f"O percentual de aumento é 15%")
    print (f"O valor do aumento é {sal-aum15}")
    print (f"Seu novo salário é {sal+aum15}.") 
elif sal >7000.00 and sal<14999.99:
    print (f"Seu salário era {sal}")
    print (f"O percentual de aumento é 10%")
    print (f"O valor do aumento é {sal-aum10}")
    print (f"Seu novo salário é {sal+aum10}.") 
else:
    print (f"Seu salário era {sal}")
    print (f"O percentual de aumento é 5%")
    print (f"O valor do aumento é {sal-aum5}")
    print (f"Seu novo salário é {sal+aum5}.") 