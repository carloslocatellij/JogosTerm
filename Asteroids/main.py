# from textual.app import App, ComposeResult
# from textual.widgets import Static, Footer, Header
# from textual.binding import Binding
# from Asteroids import Tela
# import random



# class Game(App):
#     ''' A classe princiapal'''
    
#     BINDINGS = [
#         Binding("up,w", "move_up", "Cima"),
#         Binding("down,s", "move_down", "Baixo"),
#         Binding("left,a", "move_left", "Esquerda"),
#         Binding("right,d", "move_right", "Direita"),
#         Binding("space", "shoot", "Atirar"),
#         Binding("q", "quit", "Sair")
#     ]
    
    

#     def compose(self) -> ComposeResult:
#         yield(Header())
#         yield(Tela())
#         yield(Footer())
        



# if __name__ == '__main__':
#     game = Game()
#     game.run()
    
    
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Footer, Button
from textual.reactive import reactive
from textual.binding import Binding
import random


class Entidade(Static):
    """Classe base para personagens e inimigos."""
    
    x = reactive(0)
    y = reactive(0)

    def __init__(self, emoji: str, x: int, y: int, **kwargs):
        super().__init__(emoji, **kwargs)
        self.x = x
        self.y = y

    def watch_x(self, novo_x: int) -> None:
        """Chamado sozinho quando self.x muda."""
        self.atualizar_offset_visual()

    def watch_y(self, novo_y: int) -> None:
        """Chamado sozinho quando self.y muda."""
        self.atualizar_offset_visual()

    def atualizar_offset_visual(self) -> None:
        """Ajusta a posição visual no terminal."""
        self.styles.offset = (self.x * 2, self.y)
        
    def move_para_cima(self): self.y -= 1
    def move_para_baixo(self): self.y += 1
    def move_para_direita(self): self.x += 1
    def move_para_esquerda(self): self.x -= 1


class Wizard(Entidade):
    def __init__(self, x: int, y: int):
        super().__init__("👽", x, y, id="player", classes="person")


class Enemy(Entidade):
    def __init__(self, x: int, y: int):
        super().__init__("👾", x, y, classes="enemy")


class Tela(Screen):
    
    CSS = "tela.tcss"

    MATRIZ_CENARIO = [
        ['~~' for _ in range(40)], # 0: Céu
        *(['_|' for _ in range(40)] for _ in range(20)) , # 5
        ['==' for _ in range(40)], # 6: Chão
    ]

    BINDINGS = [
        Binding("w,up", "mover_jogador('cima')", "Cima"),
        Binding("s,down", "mover_jogador('baixo')", "Baixo"),
        Binding("a,left", "mover_jogador('esquerda')", "Esquerda"),
        Binding("d,right", "mover_jogador('direita')", "Direita"),
        Binding('q', 'quit', 'exit')
    ]

    def compose(self) -> ComposeResult:
        """Monta os elementos visuais na tela."""
        
        texto_mapa = "\n".join(["".join(linha) for linha in self.MATRIZ_CENARIO])
        yield Static(texto_mapa, id="fundo_mapa")
        yield Footer()

        yield Wizard(x=3, y=5)
        yield Enemy(x=7, y=5)
        self.set_interval(0.5, self.mover_inimigo)
        

    def action_mover_jogador(self, direcao: str) -> None:
        """Captura o teclado e move o jogador se a posição for válida."""
        player = self.query_one("#player", Wizard)
        
        proximo_x, proximo_y = player.x, player.y
        if direcao == 'cima': proximo_y -= 1
        elif direcao == 'baixo': proximo_y += 1
        elif direcao == 'esquerda': proximo_x -= 1
        elif direcao == 'direita': proximo_x += 1

        if 0 <= proximo_x < 40 and 0 < proximo_y <= 20:
            if direcao == 'cima': player.move_para_cima()
            elif direcao == 'baixo': player.move_para_baixo()
            elif direcao == 'esquerda': player.move_para_esquerda()
            elif direcao == 'direita': player.move_para_direita()
    
    def mover_inimigo(self):
        inimigo = self.query_one('.enemy', Enemy)
        direcao = random.choice(['cima', 'baixo', 'esquerda', 'direita'])
        
        proximo_x, proximo_y = inimigo.x, inimigo.y
        if direcao == 'cima': proximo_y -= 1
        elif direcao == 'baixo': proximo_y += 1
        elif direcao == 'esquerda': proximo_x -= 1
        elif direcao == 'direita': proximo_x += 1
        
        if 0 <= proximo_x < 40 and 0 < proximo_y <= 20:
            if direcao == 'cima': inimigo.move_para_cima()
            elif direcao == 'baixo': inimigo.move_para_baixo()
            elif direcao == 'esquerda': inimigo.move_para_esquerda()
            elif direcao == 'direita': inimigo.move_para_direita()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'quit':
            self.exit()
        else:
            self.app.bell()
        

class JogoApp(App):
    def on_mount(self) -> None:
        self.push_screen(Tela())

if __name__ == "__main__":
    app = JogoApp()
    app.run()