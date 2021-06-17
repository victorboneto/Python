#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
#o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:


INCOME_TAX = 0.11
SYNDICATED = 0.05
INSS = 0.08

salary_hour = float(input("Digite quanto que você ganha por hora: "))
mouth_hour =  float(input("Digite quantas horas você trabalha por mês: "))

#salario bruto
gross_salary = salary_hour * mouth_hour
print("você ganha {}R$" .format(gross_salary))

cost_INSS = gross_salary * INSS
print("você pagou para o INSS {} R$" .format(cost_INSS))

cost_syndicated = gross_salary * SYNDICATED
print("você pagou para o sindicado {} R$" .format(cost_syndicated))

salary_liquid = gross_salary - (cost_syndicated + cost_INSS )
print("Seus salario liquido depois dos impostos obrigatórios é  de {} R$ " .format(salary_liquid))