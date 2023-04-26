from brain.GameOfLifeBrain import GameOfLifeBrain
from game_master.GameMaster import GameMaster
from game_ui.GameUI import GameUI

if __name__ == "__main__":
    ui = GameUI()
    brain = GameOfLifeBrain()
    game_master = GameMaster(ui, brain, 50)

    game_master.start_simulation()

