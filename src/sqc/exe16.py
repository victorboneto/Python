#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
#em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 
#1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
# e o preço total.

import math
COST_LITER = 80
LITER = 18
LITER_PER_METERS = 3

meters = int(input("Digite os metros para pintar aqui: "))

liters = meters / LITER_PER_METERS
liter = liters / LITER
liters_total = math.ceil(liter)
cost_liters = int(liters_total) * COST_LITER 

if liter < 1:
  print("O custo será de 80 R$")
  print("Comprara 1 lata de tinta")
else:
  print("O custo será de {} R$" .format(cost_liters))
  print("Comprara {} latas de tinta" .format(liters_total))