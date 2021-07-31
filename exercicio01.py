''''
Crie um programa que recebe um número e imprime o seu fatorial.

# Método 5Q's  para montar um algorítimo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
numero
2. O que devo fazer com estes dados?
eu devo calcular o fatorial do número que for passado para o meu programa e o exibir na tela.
3. Quais são as restrições deste problema?
- O número deve ser um valor positivo
- O número deve ser um valor inteiro
4. Qual é o resultado esperado?
- O resultado esperado é que o fatorial do número providenciado seja exibido.
5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
  fatorial = fatorial * numero 
print(fatorial)
'''
numero = int(input('Escolha um número para saber seu fatorial: '))
if numero > 0:
  fatorial = 1
  for num in range(1, numero + 1):
    fatorial = fatorial * num
  print(numero,'!',' = ',fatorial)
else:
  print('Você digitou um numero invalido. Tente um número inteiro positivo!')