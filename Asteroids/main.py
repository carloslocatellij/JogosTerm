from textual.app import App, ComposeResult
from textual.widgets import Static, Footer, Header
from textual.binding import Binding
from Asteroids import Tela
import random



class Game(App):
    ''' A classe princiapal'''
    
    BINDINGS = [
        Binding("up,w", "move_up", "Cima"),
        Binding("down,s", "move_down", "Baixo"),
        Binding("left,a", "move_left", "Esquerda"),
        Binding("right,d", "move_right", "Direita"),
        Binding("space", "shoot", "Atirar"),
        Binding("q", "quit", "Sair")
    ]
    
    

    def compose(self) -> ComposeResult:
        yield(Header())
        yield(Tela())
        yield(Footer())
        



if __name__ == '__main__':
    game = Game()
    game.run()
    