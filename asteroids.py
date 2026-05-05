#import random as rd
import click
#import asyncio
import time

enemy = '👾' # Inimigo que ainda não implementei

largura_tela, altura_tela = 9, 5  #Variaveis que não estou usando agora mas prentendo usar depois


# A tela é uma lista "t" que contem 7 outras listas dentro, cada uma é uma linha da tela

t = [[] for _ in range(7)]
t[0] = ['~~' for _ in range(10)] # céu
t[1] = ['  ' for _ in range(10)]
t[2] = ['  ' for _ in range(10)]
t[3] = ['  ' for _ in range(10)]
t[4] = ['  ' for _ in range(10)]
t[5] = ['  ' for _ in range(10)]
t[6] = ['==' for _ in range(10)] # chão

# A nave espacial Orientada a Objeto  -> POO

#navinha = spaceship( 3, 3)

class spaceship():                # DEFINO A CLASSE NAVE - É como um modelo do que deve ser uma "nave" 
    def __init__(self, x, y):     # o método __init__ é o metodo de inicialiação/criação da classe
        self.x = x
        self.y = y
        self.char = '🛦 '
        self.life = 10
        self.shot_char = "'"
        
    def shot(self):
        shot_x = self.x
        shot_y = self.y
        while shot_y >= 1:
            tela(shot_x, shot_y -1, self.shot_char, (shot_x, shot_y -1))       
            shot_y -= 1
    
    def andar(self):
        c = click.getchar()
        last_pos =   self.x, self.y
        
        match (c):
            case ('a'): 
                if not self.x <= 0: self.x -= 1
            case ('d'):
                if not self.x > 8: self.x += 1 
                else: self.x
            case ('w'):
                if not self.y <= 1: self.y -= 1 
                else: self.y
            case ('s'):
                if not self.y > 4: self.y += 1  
                else: self.y
            case (' '):
                self.shot() 
            case (_): pass
        return last_pos
    

            


nave = spaceship(4,3)



def tela(x, y, char, last_pos):
    
    next_pos = t[y][x]
    
    t[y][x] = char
    
    t[last_pos[1]][last_pos[0]] = next_pos
    
    tela = f'''
######################
#{t[0][0]}{t[0][1]}{t[0][2]}{t[0][3]}{t[0][4]}{t[0][5]}{t[0][6]}{t[0][7]}{t[0][8]}{t[0][9]}#
#{t[1][0]}{t[1][1]}{t[1][2]}{t[1][3]}{t[1][4]}{t[1][5]}{t[1][6]}{t[1][7]}{t[1][8]}{t[1][9]}#
#{t[2][0]}{t[2][1]}{t[2][2]}{t[2][3]}{t[2][4]}{t[2][5]}{t[2][6]}{t[2][7]}{t[2][8]}{t[2][9]}#
#{t[3][0]}{t[3][1]}{t[3][2]}{t[3][3]}{t[3][4]}{t[3][5]}{t[3][6]}{t[3][7]}{t[3][8]}{t[3][9]}#
#{t[4][0]}{t[4][1]}{t[4][2]}{t[4][3]}{t[4][4]}{t[4][5]}{t[4][6]}{t[4][7]}{t[4][8]}{t[4][9]}#
#{t[5][0]}{t[5][1]}{t[5][2]}{t[5][3]}{t[5][4]}{t[5][5]}{t[5][6]}{t[5][7]}{t[5][8]}{t[5][9]}#
#{t[6][0]}{t[6][1]}{t[6][2]}{t[6][3]}{t[6][4]}{t[6][5]}{t[6][6]}{t[6][7]}{t[6][8]}{t[6][9]}#

    '''
    click.clear()
    print(tela)

    
while True:
    time.sleep(0.07)
    vai = nave.andar()
    tela(nave.x, nave.y, nave.char, vai)
    
    
    
    # if x <= 3 and y <=6:
    #     y += 1
    #     asyncio.sleep(0.4)
    # elif y >= 6 and x <= 3:
    #     x += 1
    #     asyncio.sleep(0.4)as
    # else:
    #     if y >= 6 and x >=4:
    #         y -= 1
    #         asyncio.sleep(0.4)
    #     elif y <= 6 and x >=4:
    #         asyncio.sleep(0.4)
    #         x -= 1
    #     # else:
    #     #     asyncio.sleep(0.4)
    #     #     x +=1
    
        