from textual.screen import Screen
from textual.app import ComposeResult
from textual import on
from textual.widgets import Header, Footer, Button, Static
from textual.containers import CenterMiddle    

from Jogo_da_Memoria.cartas import Baralho, figuras
# def tabelar_cartas(col):
#     tab_cards = []
#     row_cards = []
#     for i, card in enumerate(baralho):
#         btn = ButtonCard(carta=card, id=f'bt-card-{i}')
#         row_cards.append(btn)
#         if len(row_cards) == col:
#             row = row_cards.copy()
#             tab_cards.append(row)
#             row_cards = []
#         elif i > (len(baralho.cartas) // col) * col and i >= len(baralho.cartas) % col:
#             row = row_cards.copy()
#             tab_cards.append(row)
#             row_cards = []
#     return tab_cards


baralho = Baralho(figuras, 2)

class ButtonCard(Button):
    def __init__(self, carta: type, id: int):
        super().__init__()
        self._id = f'bt-card-{str(id)}'       
        self.label = carta.verso
        self.classes="button"
        self.variant= "success"
        self.frente = carta.frente
        self.clicado = False
        if self.clicado == True:
            self.label = self.frente
        
    def vira(self):
        self.clicado == True



class Memo_Game_Screen(Screen):
    
    CSS = """Screen {     
    background: $boost;
    height: 5;
    margin: 1;
    min-width: 50;
    padding: 1; }
    
             Horizontal {
                 align: center middle;}

CenterMiddle {
    layout: grid;
    grid-size: 5;
    grid-columns: 1fr;
    grid-rows: 1fr;
    margin: 1;
    min-width: 50;
    padding: 1;
}
ButtonCard {
    width: 1;
    height: 2;
}
    """
    
    
    def __init__(self):
        super().__init__()
        
    def compose(self)  -> ComposeResult:
        yield Header(show_clock=True)
        yield CenterMiddle   (
                        *( ButtonCard(carta=card, id=i) for i, card in enumerate(baralho)),
                        id='container_cards'
                        )
        yield Footer()
        yield Button('Sair', id='bt-sair')
        
        

    @on(Button.Pressed, id=f'#bt-card-{str(id)}')
    def vira_carta(self):
            self.query_one(f'#bt-card-{str(id)}').vira()
        
        
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'bt-sair':
            self.dismiss()  
