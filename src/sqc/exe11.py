#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

value_1 = int(input("Digite o primeiro valor: "))
value_2 = int(input("Digite o segundo valor: "))
value_3 = int(input("Digite o terceiro valor: "))

#o produto do dobro do primeiro com metade do segundo .
print("Questão A")
product_1 = value_1 * 2
product_2 = value_2 / 2 
soma_product = product_1 + product_2

print("O dobro do primeiro é de " + str(product_1))
print("A metade do segundo é de " + str(product_2))
print("A soma dos dois será de " + str(soma_product))

#a soma do triplo do primeiro com o terceiro.
print("Questão B")
first = value_1 * 3
soma = first * value_3

print("O triplo do primeiro é de " + str(first))
print("O teceiro valor é de " + str(value_3))
print("A soma deles é de " + str(soma))

#o terceiro elevado ao cubo.
print("Questão C")
cubic = value_3 ** 3

print("O valor cúbico do terceiro é de " + str(cubic))