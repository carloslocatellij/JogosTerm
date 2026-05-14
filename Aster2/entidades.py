from textual.reactive import var
# --- LÓGICA PURA (Independente do Textual) ---

class EntidadeLogica:
    """Representa os dados puros de qualquer coisa no mapa."""
    def __init__(self, id: str, x: int, y: int, solido: bool = True):
        self.id = id
        self.x = x
        self.y = y
        self.solido = solido

class InteragivelMixin:
    """Adiciona a capacidade de ser ativado por um botão (Ex: Baú, NPC)."""
    def ao_interagir(self, ator: EntidadeLogica) -> str:
        raise NotImplementedError

class ColidivelMixin:
    """Adiciona a capacidade de ativar algo ao ser pisado (Ex: Armadilha, Portal)."""
    def ao_colidir(self, ator: EntidadeLogica) -> None:
        raise NotImplementedError

# --- EXEMPLOS DE ENTIDADES ESCALÁVEIS ---

class Bau(EntidadeLogica, InteragivelMixin):
    def __init__(self, id, x, y):
        super().__init__(id, x, y, solido=True)
        self.aberto = False

    def ao_interagir(self, ator):
        if not self.aberto:
            self.aberto = True
            return "Você encontrou uma Espada!"
        return "O baú já está vazio."

class Espinho(EntidadeLogica, ColidivelMixin):
    def __init__(self, id, x, y):
        super().__init__(id, x, y, solido=False) # Não é sólido, dá para pisar

    def ao_colidir(self, ator):
        # Aplica dano ao jogador que pisou
        if hasattr(ator, 'hp'):
            ator.hp -= 10
            

class wizzard(EntidadeLogica, InteragivelMixin):                
    def __init__(self, x: int, y: int): 
        super().__init__("🧙🏻‍♂️", classes="person")
        self.id = 'Player_person'
        self.x = var(float(x))
        self.y = var(float(y))
    
    def on_mount(self) -> None:
        self.styles.offset = (int(self.x), int(self.y))
    def move_para_cima(self):
        self.y -= 1
    def move_para_baixo(self):
        self.y += 1
    def move_para_direita(self):
        self.x += 2
    def move_para_esquerda(self):
        self.x -= 2
        
    def ao_interagir(self, ator):
        return f"Está falando com o {self.label}"
        
        
        
class enemy(EntidadeLogica, ColidivelMixin):                
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
        
    def ao_colidir(self, ator):
        # Aplica dano ao jogador que pisou
        # if hasattr(ator, 'hp'):
        #     ator.hp -= 10
        return f"Bateu!"
        
        
class speel():                 
    def __init__(self, x, y):     
        self.x = x
        self.y = y