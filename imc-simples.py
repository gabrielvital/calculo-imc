print ("Bem vindo à Calculadora IMC!")

nome = input("Para começar, digite seu nome: ")

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Agora, digite seu peso em kg: "))

imcfinal = peso / (altura * altura)

print (nome, "seu IMC é", imcfinal)

if imcfinal <= 17:
    print ("Você está muito abaixo do peso ideal.")

elif imcfinal <= 18.49:
    print ("Você está abaixo do peso ideal.")

elif imcfinal <= 24.99:
    print ("Você está com o peso normal.")

elif imcfinal <= 29.99:
    print ("Você está acima do peso.")

elif imcfinal <= 34.99:
    print ("Você está obeso.")

elif imcfinal <= 39.99:
    print ("Você está com obesidade severa")

else:
    print ("Você está com obesidade mórbida")
