# Variáveis

# Números
velocidade_internet = 10 # int
nota_filme = 8.1 # float

# Valores Boleanos
esta_aberto = False # True = sim, False = não

# String
nome_do_curso = 'Lógica de Programação'

# Como variáveis seriam usadas em um programa real ?

# Problema 1 - Valor por hora
# Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.
''''
input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal / horas_trabalhadas_por_mes
print valor_hora
'''

salario_mensal = input ('Qual é o seu salario mensal? ')#input, armazena temporariamente o que foi passado.
horas_trabalhadas_por_mes = input('Quantas horas você trabalha por mês ? ')


valor_hora = int (salario_mensal) / int(horas_trabalhadas_por_mes)

print(valor_hora)#print , mostra na tela o resultado