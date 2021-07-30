# Coleções(Listas)
'''
preco_1 = 20
preco_2 = 50
preco_3 = 200
'''
#Listas
precos = [20,50,200]#indices [0,1,2,...]
print(precos[1])#(precos.index(50))

diversidade = [18,'Leto',True]
print(diversidade[0])
print(diversidade[1])
print(diversidade[2])
# Laços em iteráveis
for preco in precos:
  print(preco)


# Some os valores
'''
Dado uma coleção de dados 'idades' [15,46,75,34,23], imprima na tela a soma destes valores.
'''
idades = [15,46,75,34,23]
total = 0

for idade in idades:
  total = total + idade
print(total)