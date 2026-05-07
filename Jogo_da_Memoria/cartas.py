from dataclasses import dataclass
from random import shuffle
from typing import List

figuras  =  ['🦊', '🐢', '🐦', '🐥', '😺', '🐞', '🐑', '🍧', '🐒', '🍕' ,
                '🍇', '👻', '💎', '🍔', '🏀', '🌽', '⚽', '🌜', '👒', '🌎'
            ]

@dataclass
class Carta:
    'Uma carta de Jogo da Memória - Tem frente e tem Verso'
    
    def __init__(self, frente):
        self.frente = frente
        self.verso = '🃏'
    
    def __eq__(self, other):
        self == other
        
    def __str__(self):
        return '|'+ self.frente + '|'
        
       
class Baralho:
    def __init__(self, figuras: List[list:[]], nivel: int) -> List[Carta]:
        self.cartas = []
        if isinstance(nivel, int):
            if nivel in [1,2]:
                if nivel == 1: self.figuras = figuras[:10]
                if nivel == 2: self.figuras = figuras[:14]
        else:
             raise 'O NIVEL DEVE SE UM NÚMERO INTEIRO!!!'
        self.figuras = figuras * 2
        for figura in self.figuras:
            self.cartas.append(Carta(figura))
        
    def __str__(self):
        ' '.join([carta.frente for carta in self.cartas])
        
    def __iter__(self):
        return iter(self.cartas)  
    
    def __get__(self, pos):
        return self.cartas[pos]
    
    def embaralhar(self):
        return shuffle(self.figuras)
    
    