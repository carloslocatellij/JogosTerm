from textual.widgets import Static
from textual.reactive import var


class wizzard(Static):                
    def __init__(self, x: int, y: int): 
        super().__init__("🧙🏻‍♂️", classes="person")
        self.id = 'Player_person'
        self.x = var(float(x))
        self.y = var(float(y))
    
    
    def move_para_cima(self):
        self.y -= 1
    def move_para_baixo(self):
        self.y += 1
    def move_para_direita(self):
        self.x += 2
    def move_para_esquerda(self):
        self.x -= 2
        
    def on_mount(self) -> None:
        self.styles.offset = (int(self.x), int(self.y))
        
        
        
class enemy(Static):                
    def __init__(self, x: int, y: int):
        super().__init__("👾", classes="enemy")
        self.x = var(float(x))
        self.y = var(float(y))

    def move_para_cima(self):
        self.y -= 1
    def move_para_baixo(self):
        self.y += 1
    def move_para_direita(self):
        self.x += 2
    def move_para_esquerda(self):
        self.x -= 2
        
    def on_mount(self) -> None:
        self.styles.offset = (int(self.x), int(self.y))
        
        
        
        
class speel(Static):                 
    def __init__(self, x, y):     
        self.x = x
        self.y = y