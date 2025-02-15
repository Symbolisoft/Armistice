from pathlib import Path
from sprites.dirt import *
from sprites.trench_walls import *
from sprites.trench_furniture import *

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
            if col == 'L':
                if y % 2 != 0:
                    TrenchLeftTaperTop(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    TrenchLeftTaperTop(game, x, (y+(16/TILESIZE))/2)
            if col == 'l':
                if y % 2 != 0:
                    TrenchLeftTaperBottom(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    TrenchLeftTaperBottom(game, x, (y+(16/TILESIZE))/2)
            if col == '-':
                if y % 2 != 0:
                    TrenchLeftRecess(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    TrenchLeftRecess(game, x, (y+(16/TILESIZE))/2)
            if col == 'R':
                if y % 2 != 0:
                    TrenchRightTaperTop(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    TrenchRightTaperTop(game, x, (y+(16/TILESIZE))/2)
            if col == 'r':
                if y % 2 != 0:
                    TrenchRightTaperBottom(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    TrenchRightTaperBottom(game, x, (y+(16/TILESIZE))/2)
            if col == '_':
                if y % 2 != 0:
                    TrenchRightRecess(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    TrenchRightRecess(game, x, (y+(16/TILESIZE))/2)

def furniture_map_translator(game, map):

    file_path = Path(map)

    with file_path.open('r') as file:
        content = file.read()

    for y, row in enumerate(content.split('\n')):
        for x, col in enumerate(row.split(',')):
            if col == 'B':
                if y % 2 != 0:
                    BunkRight(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    BunkRight(game, x, (y+(16/TILESIZE))/2)
            if col == 'b':
                if y % 2 != 0:
                    BunkLeft(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    BunkLeft(game, x, (y+(16/TILESIZE))/2)
            if col == 'S':
                if y % 2 != 0:
                    SandBagsRight(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    SandBagsRight(game, x, (y+(16/TILESIZE))/2)
            if col == 's':
                if y % 2 != 0:
                    SandBagsLeft(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    SandBagsLeft(game, x, (y+(16/TILESIZE))/2)
            if col == 'C':
                if y % 2 != 0:
                    CabinetRight(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    CabinetRight(game, x, (y+(16/TILESIZE))/2)
            if col == 'c':
                if y % 2 != 0:
                    CabinetLeft(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    CabinetLeft(game, x, (y+(16/TILESIZE))/2)
            if col == 'G':
                if y % 2 != 0:
                    GunRackRight(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    GunRackRight(game, x, (y+(16/TILESIZE))/2)
            if col == 'g':
                if y % 2 != 0:
                    GunRackLeft(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    GunRackLeft(game, x, (y+(16/TILESIZE))/2)
            if col == 'A':
                if y % 2 != 0:
                    GreenCratesRight(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    GreenCratesRight(game, x, (y+(16/TILESIZE))/2)
            if col == 'a':
                if y % 2 != 0:
                    GreenCratesLeft(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    GreenCratesLeft(game, x, (y+(16/TILESIZE))/2)
            if col == '>':
                if y % 2 != 0:
                    ArtyShellsRight(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    ArtyShellsRight(game, x, (y+(16/TILESIZE))/2)
            if col == '<':
                if y % 2 != 0:
                    ArtyShellsLeft(game, x+(16/TILESIZE), (y+(16/TILESIZE))/2)
                else:
                    ArtyShellsLeft(game, x, (y+(16/TILESIZE))/2)

