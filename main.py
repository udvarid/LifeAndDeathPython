from enum import Enum

from brain.GameOfLifeBrain import GameOfLifeBrain
from brain.WormBrain import WormBrain
from game_master.GameMaster import GameMaster
from game_ui.GameUI import GameUI
from worm.Worm import Worm, BodyType, Worm_colour, Coordinate, State


class Map_type(Enum):
    BRAIN = 1
    MOUTH = 2
    LEG = 3
    MULTIPLIER = 4
    EGG = 5
    EMPTY = 6


class Map_cell:
    def __init__(self, coordinate, map_type):
        self.coordinate = coordinate
        self.map_type = map_type


def get_map_sign(sign):
    sign_back = "."
    if sign == Map_type.BRAIN:
        sign_back = "B"
    elif sign == Map_type.MOUTH:
        sign_back = "M"
    elif sign == Map_type.LEG:
        sign_back = "L"
    elif sign == Map_type.MULTIPLIER:
        sign_back = "X"
    elif sign == Map_type.EGG:
        sign_back = "O"
    return sign_back


if __name__ == "__main__":
    # ui = GameUI()
    # brain = GameOfLifeBrain()
    # game_master = GameMaster(ui, brain, 50)
    #
    # game_master.start_simulation()

    wormBrain = WormBrain()

    body_types = [BodyType.MOUTH, BodyType.BRAIN, BodyType.LEG, BodyType.MULTIPLIER, BodyType.LEG, BodyType.BRAIN]

    new_worm_blue = Worm(Coordinate(5, 5), body_types, Worm_colour.BLUE, wormBrain)
    new_worm_red = Worm(Coordinate(20, 20), body_types, Worm_colour.RED, wormBrain)
    wormBrain.worms.append(new_worm_blue)
    wormBrain.worms.append(new_worm_red)

    header_num1 = list(map(lambda x: x + 1, range(10)))
    header_num2 = list(map(lambda x: x + 1, range(10,25)))
    header1 = '  '.join([str(i) for i in header_num1])
    header2 = ' '.join([str(i) for i in header_num2])
    header = header1 + " " + header2

    while True:
        worm_map = []
        for i in range(25):
            row_map = []
            for j in range(25):
                map_cell = Map_cell(Coordinate(j + 1, i + 1), Map_type.EMPTY)
                row_map.append(map_cell)
            worm_map.append(row_map)

        for worm in wormBrain.worms:
            if worm.state in [State.EGG, State.BIRTH]:
                egg_position = worm.get_unborn_body_parts()[0].coordinate
                worm_map[egg_position.y - 1][egg_position.x - 1].map_type = Map_type.EGG

            for active_body_part in worm.get_active_body_parts():
                if not active_body_part.damaged:
                    body_type = active_body_part.body_type
                    map_type = Map_type.EMPTY
                    if body_type == BodyType.LEG:
                        map_type = Map_type.LEG
                    elif body_type == BodyType.BRAIN:
                        map_type = Map_type.BRAIN
                    elif body_type == BodyType.MOUTH:
                        map_type = Map_type.MOUTH
                    elif body_type == BodyType.MULTIPLIER:
                        map_type = Map_type.MULTIPLIER
                    worm_map[active_body_part.coordinate.y - 1][active_body_part.coordinate.x - 1].map_type = map_type

        red_worms = wormBrain.get_number_of_color_type_worm(Worm_colour.RED)
        blue_worms = wormBrain.get_number_of_color_type_worm(Worm_colour.BLUE)

        print(f"--------red:{red_worms}----------blue:{blue_worms}-----------------------------------------------------")
        print(f"      {header}")
        for y in range(25):
            row_string = f'{y + 1} - ' if y < 9 else f'{y + 1} -'
            for x in range(25):
                sign = get_map_sign(worm_map[y][x].map_type)
                row_string = row_string + "  " + sign
            print(row_string)

        print("----------------------------------------------------------------------------------------------")
        wormBrain.ask_next_result()

    print("h")


# TODO Coordinata object összehasonlítható és mindenhol azt használjuk
# TODO EGG places részt szépíteni