from src.core import GameEngine, Team

def test_game_init():
    g = GameEngine(n = 3)

    state = g.get_game_state()

    assert len(state["edge_owner"]) > 0
    assert all(owner is None for owner in state["edge_owner"].values())

    assert state["winner"] is None
    assert state["turn"] == Team.MAKER

    assert g.available_edges == set(state["edge_owner"].keys())
