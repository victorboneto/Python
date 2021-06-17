#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
#o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior
#que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve
#pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
#que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso
#a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
#Imprima os dados do programa com as mensagens adequadas.

WEIGHT_BY_RELEASE = 50
MULTA = 4
Weight = input("Digite o valor do peso: ")

if WEIGHT_BY_RELEASE < int(Weight):
  excess = (int(Weight) - 50) * MULTA
  print("O Excesso que João terá que pagar é de {} R$ e teve o excesso de {} kg" .format(excess, Weight))
else:
  print("não precisa pagar")