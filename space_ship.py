import random
from textual.app import App, ComposeResult
from textual.widgets import Static, Footer, Header
from textual.binding import Binding

# --- Classes dos Elementos do Jogo ---

class Laser(Static):
    """Widget que representa o tiro da nave."""
    def __init__(self, x: int, y: int):
        super().__init__("│", classes="laser")
        self.x = x
        self.y = float(y)

    def on_mount(self) -> None:
        self.styles.offset = (self.x, int(self.y))

class Enemy(Static):
    """Widget que representa os inimigos."""
    def __init__(self, x: int, y: int):
        super().__init__("👾", classes="enemy")
        self.x = x
        # Usamos float para mover o inimigo mais devagar (frações de espaço)
        self.y = float(y)

    def on_mount(self) -> None:
        self.styles.offset = (self.x, int(self.y))

# --- Aplicação Principal ---

class SpaceShipApp(App):
    """Um mini jogo de nave espacial no terminal com tiros e inimigos."""

    CSS = """
    Screen {
        background: #050510;
        overflow: hidden;
    }

    #ship {
        position: absolute;
        width: 3;
        height: 1;
    }

    .laser {
        position: absolute;
        color: #00ffff; /* Ciano para o laser */
        text-style: bold;
    }

    .enemy {
        position: absolute;
    }
    """

    BINDINGS = [
        Binding("up,w", "move_up", "Cima"),
        Binding("down,s", "move_down", "Baixo"),
        Binding("left,a", "move_left", "Esquerda"),
        Binding("right,d", "move_right", "Direita"),
        Binding("space", "shoot", "Atirar"),
        Binding("q", "quit", "Sair")
    ]

    def __init__(self):
        super().__init__()
        self.ship_x = 40
        self.ship_y = 20
        self.lasers = []
        self.enemies = []
        self.score = 0

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("🚀", id="ship")
        yield Footer()

    def on_mount(self) -> None:
        self.update_score()
        self.update_ship_position()
        
        # Cria os "Timers" do jogo
        # game_loop roda 20x por segundo (0.05s) para animar tiros e inimigos
        self.set_interval(0.05, self.game_loop)
        # spawn_enemy cria um inimigo novo a cada 1 segundo
        self.set_interval(1.0, self.spawn_enemy)

    def update_score(self) -> None:
        self.title = f"Space Ship - Pontos: {self.score}"

    def update_ship_position(self) -> None:
        # Limita a nave para não sair da tela (usando as dimensões do console)
        max_x = self.console.size.width - 4
        max_y = self.console.size.height - 4
        
        self.ship_x = max(0, min(self.ship_x, max_x))
        self.ship_y = max(2, min(self.ship_y, max_y)) # 2 para não cobrir o Header
        
        ship = self.query_one("#ship")
        ship.styles.offset = (self.ship_x, self.ship_y)

    # --- Ações do Jogador ---
    
    def action_move_up(self) -> None:
        self.ship_y -= 1
        self.update_ship_position()

    def action_move_down(self) -> None:
        self.ship_y += 1
        self.update_ship_position()

    def action_move_left(self) -> None:
        self.ship_x -= 2
        self.update_ship_position()

    def action_move_right(self) -> None:
        self.ship_x += 2
        self.update_ship_position()

    def action_shoot(self) -> None:
        # Cria um laser logo acima da nave
        laser = Laser(self.ship_x + 1, self.ship_y - 1)
        self.lasers.append(laser)
        self.mount(laser) # Adiciona visualmente na tela

    # --- Lógica Automática do Jogo ---

    def spawn_enemy(self) -> None:
        # Sorteia uma posição horizontal na tela
        x = random.randint(2, self.console.size.width - 4)
        enemy = Enemy(x, 1) # Começa no topo
        self.enemies.append(enemy)
        self.mount(enemy)

    def game_loop(self) -> None:
        """Move lasers, inimigos e checa colisões."""
        
        # 1. Move os Lasers para cima
        for laser in self.lasers[:]:
            laser.y -= 1.5
            if laser.y <= 0:
                laser.remove() # Remove da tela
                self.lasers.remove(laser) # Remove da lista
            else:
                laser.styles.offset = (laser.x, int(laser.y))

        # 2. Move os Inimigos para baixo
        for enemy in self.enemies[:]:
            enemy.y += 0.3 # Move devagar
            if enemy.y > self.console.size.height - 2:
                enemy.remove()
                self.enemies.remove(enemy)
            else:
                enemy.styles.offset = (enemy.x, int(enemy.y))

        # 3. Checa Colisões
        for laser in self.lasers[:]:
            for enemy in self.enemies[:]:
                # Se a altura bater e a distância horizontal for curta (margem de erro do emoji)
                if int(laser.y) == int(enemy.y) and abs(laser.x - enemy.x) <= 2:
                    # Acertou! Destrói ambos.
                    laser.remove()
                    enemy.remove()
                    
                    if laser in self.lasers: self.lasers.remove(laser)
                    if enemy in self.enemies: self.enemies.remove(enemy)
                    
                    self.score += 10
                    self.update_score()
                    break # Sai do loop de inimigos pois o laser já foi destruído

if __name__ == "__main__":
    app = SpaceShipApp()
    app.run()