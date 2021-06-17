#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
# peso ideal, utilizando as seguintes fórmulas:


height = float(input("Digite sua altura: "))

print("Peso ideal para homens!")
#Para homens: (72.7*h) - 58
man = (72.7 * height) - 58
print("Peso ideal: {}Kg" .format(man))

print("Peso ideal para mulheres!")
#Para mulheres: (62.1*h) - 44.7
female = (62.1 * height) - 44.7
print("Peso ideal: {}Kg" .format(female))