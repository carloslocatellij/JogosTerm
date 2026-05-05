import click
fogo = '🔥'
ovelha = '🐑'
lobo = '🐺'
feno = '🌾'
fogo_na_margem = fogo

margem_esquerda = [ovelha, lobo, feno]
rio = '~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~'
margem_direita = []

historia = """
Você é um pastor que perdeu sua ovelha, foi procura-la e
se deparou com uma situação inusitada:
Sua ovelha conseguiu atravessar um rio e encontrou bastante 
feno, o que é bom e você quer levar
para as outras comerem. 
Mas também, ela estava sendo emboscada por um lobo.
Como se não bastasse, a ovelha, o lobo e o feno
estavam em uma parte da margem cercada por fogo e não
tinha como escaparem, sorte que você foi de canoa
e prentede salvar todos, um por um !!!
digite "print(regras)" para saber como.
"""

regras = """
Cabe um por vez no barco. Mas a ovelha não pode ficar sozinha com o lobo e nem com o feno,
em nenhuma das margens.
O fogo avança a cada vez que você faz uma travessia
e se chegar a 12 chamas você perde.
Você ganha quando consegue levar todos para o outro lado.

comandos:
ver() => ver a situação completa.
embarcar(carga) => coloca na canoa a carga determinada 
que está na margem. 
desembarcar(carga) => desembarca a carga determinada da 
canoa na margem.
atravessar() => navega para a outra margem.
Bora jogar!
"""

canoa = {'margem': 'esquerda', 'cargas' : ( )}

def ver():
  click.clear()
  if canoa['margem'] == 'esquerda':
    print(fogo_na_margem)
    print(f'Margem esquerda: {margem_esquerda}')
    print(f'<_{canoa["cargas"]}_>')
    print(rio)
    print(f'Margem direita: {margem_direita}')
  else:
    print(fogo_na_margem)
    print(f'Margem esquerda: {margem_esquerda}')
    print(rio)
    print(f'<_{canoa["cargas"]}_>')
    print(f'Margem direita: {margem_direita}')


def embarcar(carga):
  if len(canoa['cargas']) >= 1:
    print('Não é possível embarcar mais cargas!')
    
  elif carga in canoa['cargas']:
    print(f'O/A {carga} já está na canoa!')
  elif canoa['margem'] == 'esquerda' and carga in margem_esquerda:
    margem_esquerda.remove(carga)
    canoa['cargas'] += (carga,)
  elif canoa['margem'] == 'direita' and carga in margem_direita:
    margem_direita.remove(carga)
    canoa['cargas'] += (carga,)
  else:
    print(f'O/A {carga} não está nesta margem')
  ver()


def desembarcar(carga):
  if carga not in canoa['cargas']:
    print(f'O/A {carga} não está na canoa!')
  else:
    if canoa['margem'] == 'esquerda':
      margem_esquerda.append(carga)
      canoa['cargas'] = tuple([c for c in canoa['cargas'] if c != carga])
    else:
      margem_direita.append(carga)
      canoa['cargas'] = tuple([c for c in canoa['cargas'] if c != carga])
  ver()


def atravessar():
  global fogo_na_margem
  fogo_na_margem += fogo
  if len(fogo_na_margem) >= 12:
    print(f'Você perdeu, o fogo queimou {margem_esquerda}!')
  elif canoa['margem'] == 'esquerda':
    if ovelha in margem_esquerda and lobo in margem_esquerda  or feno in margem_esquerda and ovelha in margem_esquerda:
      print('Você não pode atravessar!')
    else:
      canoa['margem'] = 'direita'
  else:
    if ovelha in margem_direita and lobo in margem_direita  or feno in margem_direita and ovelha in margem_direita:
      print('Você não pode atravessar!')
    else:
      canoa['margem'] = 'esquerda'
      
if __name__ == '__main__':
  print(historia)
  ver()
  
  comando = input('>>> ')