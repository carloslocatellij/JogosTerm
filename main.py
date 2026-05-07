from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Button
from textual.containers import Horizontal
from Jogo_da_Memoria.memo_screen import Memo_Game_Screen


class Menu(Screen):
    
    CSS = """Screen { align: center middle; background: $background; }
             Horizontal {align: center middle;}
            """
    
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Button('Jogo da Memória', id='bt-memo_game', ) 
            )
        yield Footer()

    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'bt-memo_game':
            self.app.push_screen(Memo_Game_Screen())
        

class Jogo(App):
    
    BINDINGS = [("q", "quit", "Sair")]
    
    def on_mount(self) -> None:
        self.push_screen(Menu())
            


if __name__ == '__main__':
    app = Jogo()
    app.run()