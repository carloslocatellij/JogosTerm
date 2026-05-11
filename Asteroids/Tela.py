# A tela do Jogo
from textual.screen import Screen


# def tela(x, y, char, last_pos):
    
#     next_pos = t[y][x]
    
#     t[y][x] = char
    
#     t[last_pos[1]][last_pos[0]] = next_po


class Tela(Screen):
    def __init__(self, tamanho= 100):
        super().__init__()
        self.matriz_da_tela = []
        self.objetos = []
        
    def compose(self) -> ComposeResult:
        yield Screen()
        
        
    def update_element_id_position(self, obj_x, obj_y,  last_pos):
        next_pos = obj_x, obj_y
        
        
    
    def update_elements_positions(self):
        """
        Purpose: 
        """
        
    # end def