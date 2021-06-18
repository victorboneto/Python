#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho 
#em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 
#litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que 
#custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

#comprar apenas latas de 18 litros;

import math

LITER_PER_METERS = 6
LITER_TIN = 18
COST_LITER = 80
GALLON = 3.6
COST_GALLON = 25

meters = float(input("Quantos metros você quer: "))

#Multi-uso
liter = meters / LITER_PER_METERS


print("Só latas")

liters_tin = liter / LITER_TIN
liters = math.ceil(liters_tin)
cost_liter = liters * COST_LITER

if liters < 1:
  print("O custo será de 80 R$")
  print("Comprara 1 lata de tinta")
else:
  print("O custo será de {} R$" .format(cost_liter))
  print("Comprara {} latas de tinta" .format(liters))

print("Só galão")

gallon_tin = liter / GALLON
gallon = math.ceil(gallon_tin)
cost_gallon = gallon * COST_GALLON

if gallon < 1:
  print("O custo será de 25 R$")
  print("Comprara 1 galão de tinta")
else:
  print("O custo será de {} R$" .format(cost_gallon))
  print("Comprara {} latas de tinta" .format(gallon))

print("Latas e galões")

mix_A = int(liter / 18.0)
mix_B = int((liter - (mix_A * 18)) / 3.6)

if ((liter - (mix_A * 18) % 3.6 != 0)):
    mix_B += 1

print('Mistura: %d latas e %d galoes = %.2f' % (mix_A, mix_B, ((mix_A * 80) + (mix_B * 25))))
