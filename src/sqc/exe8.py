#Faça um Programa que pergunte quanto você ganha por hora e o
#número de horas trabalhadas no mês. Calcule e mostre o total
#do seu salário no referido mês.

salary_per_hour = int(input("Quanto que você ganha por hora: "))
hour_per_week = int(input("Quantas horas você trabalha por mês: "))

salary_total = salary_per_hour * hour_per_week

print("Você ganha {}R$ por mês" .format(salary_total))