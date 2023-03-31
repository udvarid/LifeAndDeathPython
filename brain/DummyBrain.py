import random


class DummyBrain:

    def __init__(self):
        self.running = False

    def run_check(self):
        return self.running

    def run_simulation(self, params):
        self.running = True
        print("Starting Simulation")

    def ask_next_result(self):
        print('Giving result')
        result = []
        if bool(random.getrandbits(1)):
            self.running = False
        return result
