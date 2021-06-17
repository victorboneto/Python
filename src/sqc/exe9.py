#Faça um Programa que peça a temperatura em graus Fahrenheit,
#transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

graus = int(input("Digite o graus Fahrenheit aqui: "))

celsius = 5 * ((graus - 32) / 9)

print("Tem {}ºc" .format(celsius))