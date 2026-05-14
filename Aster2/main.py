from entidades import wizzard
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Footer
from textual.reactive import reactive
from textual.message import Message
from textual.binding import Binding
from textual import work
import asyncio

# Mensagem para atualizar a UI quando o servidor mandar novos dados
class AtualizacaoDeEstado(Message):
    def __init__(self, estado_entidades: dict):
        super().__init__()
        self.estado_entidades = estado_entidades

class WidgetEntidade(Static):
    """Representação visual genérica controlada pelo servidor."""
    x = reactive(0)
    y = reactive(0)
    emoji = reactive("")

    def watch_x(self, _): self.styles.offset = (self.x * 2, self.y)
    def watch_y(self, _): self.styles.offset = (self.x * 2, self.y)
    def watch_emoji(self, novo_emoji): self.update(novo_emoji)


MATRIZ_CENARIO = [
        ['~~' for _ in range(40)], # 0: Céu
        *(['_|' for _ in range(40)] for _ in range(20)) , # 5
        ['==' for _ in range(40)], # 6: Chão
]

class TelaMultiplayer(Screen):
    CSS = "tela.tcss"
    
    BINDINGS = [
        Binding("w,up", "mover_jogador('cima')", "Cima"),
        Binding("s,down", "mover_jogador('baixo')", "Baixo"),
        Binding("a,left", "mover_jogador('esquerda')", "Esquerda"),
        Binding("d,right", "mover_jogador('direita')", "Direita"),
        Binding('q', 'quit', 'exit')]
    
    def compose(self) -> ComposeResult:
        # Renderiza apenas o fundo estático
        texto_mapa = "\n".join(["".join(linha) for linha in self.MATRIZ_CENARIO])
        yield Static(texto_mapa, id="fundo_mapa")
        yield Footer()
        # As entidades serão injetadas dinamicamente aqui

    def on_mount(self) -> None:
        # Inicia a escuta do servidor (seja rede ou local)
        self.conectar_ao_servidor()

    @work(thread=True)
    def conectar_ao_servidor(self):
        """Worker assíncrono que escuta o estado global do jogo."""
        # Simulação de recebimento de dados de um servidor via rede/engine
        while True:
            # Exemplo do pacote JSON que o servidor enviaria a cada frame:
            pacote_do_servidor = {
                "player_1": {"x": 5, "y": 10, "emoji": "👽"},
                "player_2": {"x": 8, "y": 10, "emoji": "🧙🏻‍♂️"},
                "bau_1": {"x": 2, "y": 2, "emoji": "📦"}
            }
            self.post_message(AtualizacaoDeEstado(pacote_do_servidor))
            asyncio.sleep(0.05) # 20 ticks por segundo

    def on_atualizacao_de_estado(self, msg: AtualizacaoDeEstado) -> None:
        """Sincroniza os widgets da tela com os dados reais do servidor."""
        for ent_id, dados in msg.estado_entidades.items():
            try:
                # Se o widget já existe, apenas atualiza as reatividades
                widget = self.query_one(f"#{ent_id}", WidgetEntidade)
                widget.x = dados["x"]
                widget.y = dados["y"]
                widget.emoji = dados["emoji"]
            except:
                # Se não existe (novo jogador conectou ou item dropou), cria na tela
                novo_widget = WidgetEntidade(id=ent_id)
                novo_widget.x = dados["x"]
                novo_widget.y = dados["y"]
                novo_widget.emoji = dados["emoji"]
                self.mount(novo_widget)


    # --- INPUT DO JOGADOR ---
    def action_mover_jogador(self, direcao: str):
        """Em vez de mover, envia o comando para a Engine validar."""
        """Captura o teclado e move o jogador se a posição for válida."""
        player = self.query_one("#player_1")
        
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
        
        
        
    def action_interagir(self):
        """Pressionou o botão de ação (Ex: Espaço ou 'E')."""
        # Envia comando de interação para a Engine verificar o que está na frente do jogador
        pass