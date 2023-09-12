import random

from worm.Worm import State, Worm


class WormBrain:
    def __init__(self):
        self.running = False
        self.size = 0
        self.worms = []

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
        for worm in self.worms:
            worm.next_phase()
        self.handle_attacked_worms()
        self.kill_brainless_worms()
        self.kill_worms_with_only_brain()
        self.clear_dead_worms()

        result = self.draw_random_data()
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

    def handle_attacked_worms(self):
        for attacked_worm in [x for x in self.worms if x.state == State.ATTACKED]:
            damaged_body_parts = attacked_worm.get_damaged_body_parts()
            if len(damaged_body_parts) > 1:
                attacked_worm.state = State.KILLED
            else:
                damaged_body_part = damaged_body_parts[0]
                index_of_body = [i for i, e in enumerate(attacked_worm.body_parts) if
                                 e.coordinate == damaged_body_part.coordinate][0]
                if index_of_body == 0 or index_of_body == len(attacked_worm.body_parts) - 1:
                    del attacked_worm.body_parts[index_of_body]
                    attacked_worm.state = State.MOVE
                else:
                    self.create_new_worm(attacked_worm, attacked_worm.body_parts[index_of_body + 1:])
                    attacked_worm.body_parts = attacked_worm.body_parts[:index_of_body]
                    attacked_worm.state = State.MOVE

    def create_new_worm(self, attacked_worm, body_parts):
        coor = body_parts[0].coordinate
        new_worm = Worm(coor, attacked_worm.body_types_origin, attacked_worm.color, attacked_worm.worm_brain)
        new_worm.state = State.REST
        new_worm.body_parts = body_parts
        self.worms.append(new_worm)

    def kill_brainless_worms(self):
        for worm in self.worms:
            if not worm.worm_has_brain():
                worm.state = State.KILLED

    def kill_worms_with_only_brain(self):
        for worm in self.worms:
            if worm.state not in [State.EGG, State.BIRTH] and len(worm.get_active_body_parts()) == 1 and worm.worm_has_brain():
                worm.state = State.KILLED

    def clear_dead_worms(self):
        self.worms = list(filter(lambda x: x.state is not State.KILLED, self.worms))

    def check_way(self, coordinate):
        for worm in self.worms:
            for body_part in worm.body_parts:
                if body_part.coordinate == coordinate:
                    return False
        return True

    def clear_way(self, coordinate):
        for worm in self.worms:
            for body_part in worm.body_parts:
                if body_part.coordinate == coordinate:
                    body_part.damaged = True
                    if worm.state in [State.ATTACKED, State.EGG, State.BIRTH]:
                        worm.state = State.KILLED
                    else:
                        worm.state = State.ATTACKED

    def get_number_of_color_type_worm(self, color):
        return len(list(filter(lambda x: x.color == color, self.worms)))
