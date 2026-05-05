from random import shuffle
import sys

figuras  =  ['🦊', '🐢', '💙', '🐥', '🏄', '👄', '🐑', '🐍', '🐒', '🍕' ,
             '🍇', '🌭', '🌮', '🍔', '🏀', '🎳', '⚽', '🌜', '🏆', '🌎']

figuras = figuras * 2

shuffle(figuras)

cartas = [
     figuras[0:8],
     figuras[8:16],
     figuras[16:24],
     figuras[24:32],
     figuras[32:]]

back_card = []
for _ in range(6):
    back_card.append(['🃏' for z in range(8)])
    
def tela():
    
    print(f'''
         0 |1 |2 |3 | 4| 5| 6| 7
       A {' '.join(back_card[0])}
       B {' '.join(back_card[1])}
       C {' '.join(back_card[2])}
       D {' '.join(back_card[3])}
       E {' '.join(back_card[4])}
       ''')
    
linha = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}


def troca( cart: tuple):
    back_card[cart[0]][cart[1]] = cartas[cart[0]][cart[1]]


def escolha():
    print('Digite a linha(A até E)  e a coluna (1 até 8), ou outra coisa para sair: ')
    esc = input()
    esc = esc.title().strip()
    
    if len(esc) > 2 or not esc[0].isalpha() or not esc[1].isdigit():
        print("Até a próxima.")
        sys.exit()

    else:
        cart = ( linha[esc[0]] , int(esc[1]))
        troca(cart)
        tela()
        return cart

    
while back_card != cartas:
    
    primeira = escolha()
    segunda = escolha()
    
    if cartas[primeira[0]] [primeira[1]] == cartas[segunda[0]][segunda[1]]:
        continue   
    
    else:
        back_card[primeira[0]][primeira[1]] = '🃏'
        back_card[segunda[0]][segunda[1]] = '🃏'
        
        