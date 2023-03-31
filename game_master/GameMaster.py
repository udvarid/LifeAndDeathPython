class GameMaster:
    def __init__(self, ui, brain, init_size):
        self.ui = ui
        self.brain = brain
        self.init_size = init_size

    def start_simulation(self):
        self.ui.draw_ui(
            self.init_size,
            self.brain.run_check,
            self.brain.run_simulation,
            self.brain.ask_next_result
        )
