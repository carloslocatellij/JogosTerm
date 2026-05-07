from random import shuffle
from os import system
from interface import tela
import sys

# def embaralhar():
#     figuras  =  ['🦊', '🐢', '🐦', '🐥', '😺', '🐞', '🐑', '🍧', '🐒', '🍕' ,
#                 '🍇', '👻', '💎', '🍔', '🏀', '🌽', '⚽', '🌜', '👒', '🌎'
#                 ]
# #figuras_menos = figuras[:14]
#     figuras = figuras * 2
#     shuffle(figuras)
#     cartas = []
#     for _ in range(5):
#         cartas.append ([figuras.pop() for _ in range(8)])
#     back_card = []
#     for _ in range(5):
#         back_card.append(['🃏' for z in range(8)])
#     return cartas, back_card
# cartas, back_card = embaralhar()
        
# # print(cartas)
# # print(back_card)
# system('clear')

# print('''REGRAS DO JOGO: Até dois players podem jogar!
#            Para escolher sua carta: digite de A até E para escolher a linha 
#            da carta e de 0 a 7 para escolher a posição da carta da linha. 
#            Por exemplo:
#            Se você digitar B2 estará escolhendo terceira carta da
#            segunda linha.
#            Caso encontre duas figuras iguais (um par) você joga novamente.
#            Se estiver jogando sozinho e fizer par, você também ganha pontos.
#            Se não fizer par: você não perde pontos, mas perde sua vez de
#            jogar. 
#            Para sair digite 'Q'.       
#            ''') 
# print('Escolha duas _cartas')
  

linha = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

# def troca( cart: tuple):
#     back_card[cart[0]][cart[1]] = cartas[cart[0]][cart[1]]

# def sair(x):
#     if x in ['Q', 'q']:
#         print(" Até a próxima. bye bye")
#         sys.exit()    
#     else:
#         return True
        
def escolha():
    esc = ""
    while not sair(esc) or len(esc) != 2 or \
        esc[0] not in linha \
        or not esc[1].isdigit(): #verifica a entrada
        
        print(f'Digite apenas {list(linha.keys())} e em seguida um número de 0 a 7 ')
        esc = input()
        esc = esc.upper().strip()

    else:
        cart = (linha[esc[0]] , int(esc[1]))     
        if back_card[cart[0]][cart[1]] != '🃏':
            print('''Você deve escolher duas cartas distintas e então tentar formar um par!
                Agora escolha outra carta!''')  
            return escolha() 
        else: 
            troca(cart)
            system('clear')
            tela(back_card)
            return cart

print("Pressione Enter para iniciar.")
input()


def venceu():
    print('PARABÉNS VOCÊ VENCEU !')
    print('Jogue Novamente')
    
    

def loop_principal ():
    while back_card != cartas:
        primeira = escolha()
        segunda = escolha()  
        
        if cartas[primeira[0]][primeira[1]] == cartas[segunda[0]][segunda[1]]:
            continue   
        else:
            back_card[primeira[0]][primeira[1]] = '🃏'
            back_card[segunda[0]][segunda[1]] = '🃏'
    else:
        venceu()
        embaralhar()
        
     
if __name__ == '__main__':
    loop_principal()
    
