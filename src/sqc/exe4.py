#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

number_1 = float(input("Digite a primeria nota: "))
number_2 = float(input("Digite a segunda nota: "))
number_3 = float(input("Digite a terceira nota: "))
number_4 = float(input("Digite a quarta nota: "))

media = (number_1 + number_2 + number_3 + number_4) / 4

print("A media foi de " + str(media))