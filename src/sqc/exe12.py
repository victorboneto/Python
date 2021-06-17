#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#usando a seguinte fórmula:
# (72.7*altura) - 58

height = input("Digite sua altura aqui: ")

peso = (72.7 * height) - 58

print("Seu peso ideal é de {}Kg" .format(peso))