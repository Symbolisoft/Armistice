from pathlib import Path
from sprites.dirt import *
from sprites.trench_walls import *

def ground_map_translator(game, map):

    file_path = Path(map)

    with file_path.open('r') as file:
        content = file.read()

    for y, row in enumerate(content.split('\n')):
        for x, col in enumerate(row.split(',')):
            if col == '1':
                if y % 2 != 0:
                    Dirt1(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    Dirt1(game, x, (y+(16/TILESIZE))/2)
            if col == '2':
                if y % 2 != 0:
                    Dirt2(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    Dirt2(game, x, (y+(16/TILESIZE))/2)
            if col == 'W':
                if y % 2 != 0:
                    TrenchWalls1(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    TrenchWalls1(game, x, (y+(16/TILESIZE))/2)

