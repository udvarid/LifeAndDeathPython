import random


class DummyBrain:

    def __init__(self):
        self.running = False
        self.size = 0

    def run_check(self):
        return self.running

    def run_simulation(self, params):
        self.running = True
        self.size = params.get('size')
        print(f"Starting Simulation, size is {self.size}")

    def stop_simulation(self):
        self.running = False
        print("Stopping simulation")

    def ask_next_result(self):
        print('Giving result')
        result = self.draw_random_data()
        # if bool(random.getrandbits(1)):
        #     self.running = False
        return result

    def draw_random_data(self):
        my_array = []
        n = self.size
        for i in range(n):
            my_row = []
            for j in range(n):
                my_row.append(random.randint(0, 1))
            my_array.append(my_row)
        return my_array
