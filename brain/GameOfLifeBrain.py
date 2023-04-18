from random import randint


class Cell:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value


class GameOfLifeBrain:

    def __init__(self):
        self.running = False
        self.size = 100
        self.players = 1
        self.init_cells = 10
        self.universe = set()

    def run_check(self):
        return self.running

    def run_simulation(self, params):
        self.running = True
        self.size = params.get('size', 50)
        self.players = params.get('players', 1)
        self.init_cells = params.get('init_cells', 10)
        print(
            f"Starting Simulation, size is {self.size}, number of players is {self.players}, init cells is {self.init_cells}")
        self.place_init_cells()

    def stop_simulation(self):
        self.running = False
        self.universe = set()
        print("Stopping simulation")

    def ask_next_result(self):
        print('Giving result')
        result = self.calculate_next_step()
        return result

    def place_init_cells(self):
        for i in range(self.players):
            center_x = self.size / 4
            center_y = self.size / 4
            if i == 1:
                center_x = self.size / 4 * 3
            elif i == 2:
                center_y = self.size / 4 * 3
            elif i == 3:
                center_x = self.size / 4 * 3
                center_y = self.size / 4 * 3
            self.place_random_cells_around_center(center_x, center_y, i + 1)

    def place_random_cells_around_center(self, x, y, tribe):
        while not self.tribe_is_ready(tribe):
            rand_x = 10 - randint(0, 20)
            rand_y = 10 - randint(0, 20)
            cell = Cell(x + rand_x, y + rand_y, tribe)
            self.universe.add(cell)

    def tribe_is_ready(self, tribe):
        return len(list(filter(lambda cell: cell.value == tribe, self.universe))) >= self.init_cells

    def calculate_next_step(self):
        my_array = []
        n = self.size
        for i in range(n):
            my_row = []
            for j in range(n):
                my_row.append(0)
            my_array.append(my_row)

        for cell in self.universe:
            my_array[int(cell.x)][int(cell.y)] = int(cell.value)
        return my_array
