from enum import Enum

class Team(str, Enum):
    MAKER = "maker"
    BREAKER = "breaker"

class GameEngine:

    def __init__(self, n: int):
        self.n = n
        self.winner: Optional[Team] = None
        self.turn = Team.MAKER

        self.edge_owner = {}

        for row in range(n + 1):
            for col in range(n + 1):
                edge = (("h", row, col), ("h", row, col + 1))
                self.edge_owner[edge] = None

        for row in range(n + 1):
            for col in range(n + 1):
                edge = (("v", row, col), ("v", row + 1, col))
                self.edge_owner[edge] = None

        self.available_edges = set(self.edge_owner.keys())

    def get_game_state(self) -> dict:
        return {
            "turn": self.turn,
            "winner": self.winner,
            "edge_owner": self.edge_owner
        }
