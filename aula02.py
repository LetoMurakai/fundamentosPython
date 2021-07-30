# Condicionais
# if, elif e else
'''
E ae Jão, bora dar uma saída hoje?
Se eu terminar meu trabalho aqui, eu consigo...
'''
trabalho_terminado = False

if trabalho_terminado == True:
  print('Opa! Bora pro role.')
else:
  print('Não vai dar pra sair agora...')

'''
Ei, você consegue me ajudar me ajudar a levar essas caixas lá para fora hoje a tarde ?
Se eu estiver livre, sim. Mas, se não pede ao meu irmão para te ajudar.
'''

estou_livre = False 

if estou_livre == True:
  print('Posso te ajudar hoje sim!')
else:
  print('Peça ao meu irmão, ele pode te ajudar!')

'''
Eu cheguei atrasado na aula, ainda posso entrar?
Se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrario irá tomar uma suspensão.
'''
numero_atraso = 2

if numero_atraso >= 3:
  print('Você está suspenso!!!')
elif numero_atraso == 1:
  print('Pode entrar, mas cuidado com os atrasos para não ser suspenso!')
elif numero_atraso == 2:
  print('Pode entrar, porem caso tome mais uma falta, irá ser suspenso!')
else:
  print('Pode entrar.')

# Encontre o mair entre dois números
'''
input primeiro_valor
input segundo_valor
if primeiro_valor > segundo_valor
  print o primeiro valor é maior
else
 print o segundo valor é maior
'''
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
  print('O primeiro valor '+primeiro_valor+' é maior que, '+segundo_valor)
else:
  print('O segundo valor '+segundo_valor+' é maior que, '+primeiro_valor)