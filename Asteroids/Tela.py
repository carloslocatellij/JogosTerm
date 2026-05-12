# A tela do Jogo
from typing import int
from textual.app import ComposeResult
from textual.screen import Screen
from textual.reactive import reactive

# def tela(x, y, char, last_pos):
    
#     next_pos = t[y][x]
    
#     t[y][x] = char
    
#     t[last_pos[1]][last_pos[0]] = next_po


class Tela(Screen):
    matriz = [[] for _ in range(7)]
    matriz[0] = ['~~' for _ in range(10)] # céu
    matriz[1] = ['  ' for _ in range(10)]
    matriz[2] = ['  ' for _ in range(10)]
    matriz[3] = ['  ' for _ in range(10)]
    matriz[4] = ['  ' for _ in range(10)]
    matriz[5] = ['  ' for _ in range(10)]
    matriz[6] = ['==' for _ in range(10)] # chão
    
    matriz_da_tela = reactive(matriz)
    
    def __init__(self, tamanho= 100):
        super().__init__()
        self.objetos = []
        
    def compose(self) -> ComposeResult:
        yield Screen()
        
        
    def update_element_id_position(self, elem_id: int, obj_x: int, obj_y: int) -> None:
        
        next_pos = obj_x, obj_y
        
        self.matriz_da_tela[obj_x][obj_y] = self.query_one(elem_id).label 
        
        self.matriz_da_tela[last_pos[1]][last_pos[0]] = next_pos 
        
    
    
    def update_elements_positions(self, pos_atualizations: dict) -> None:
        """
        Purpose: 
        """
        for k, v in pos_atualizations.items():
            self.update_element_id_position(k, [v[0], v[1]] )
            
        
    def watch_matriz_da_tela(self) -> None:
        