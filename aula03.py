# Laços de Repetição e Listas
'''
print('carregando...')
print('carregando...')
print('carregando...')
'''
#for item in coleção: expressão
for carregando in range(1,4):#range(inicio,-1Fim,pulo)
  print('carregando...')

nomes = ['Dafhne','Leto','Mimô','Fátima']
for nome in nomes:
  print(nome)

# Problema 1 a N -  imprime os valores de 1 a N
'''
input numero maximo
valor inicial = 1
loop de valor_inicial a numero_maximo
	print valor
'''
valor_maximo = int(input('Digite o valor máximo: '))
valor_inicial = 1
for numero in range(valor_inicial,valor_maximo + 1):
  print(numero)