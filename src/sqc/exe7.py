#Faça um Programa que calcule a área de um quadrado, em seguida mostre o
#dobro desta área para o usuário

base = int(input("Digite a base do quadrado: "))
height = int(input("Digite a altura do quadrado: "))

area = base * height
double = area * 2

print("Sua área será de " + str(double))