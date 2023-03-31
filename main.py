from brain.DummyBrain import DummyBrain
from game_master.GameMaster import GameMaster
from game_ui.GameUI import GameUI

if __name__ == "__main__":
    ui = GameUI()
    brain = DummyBrain()
    game_master = GameMaster(ui, brain, 100)

    game_master.start_simulation()

