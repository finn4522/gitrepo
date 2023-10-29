"""Flood-fill to count chambers in a cave.
CS 210 project.
Finn Fujimura, 10/23/2023
Credits: TBD
"""
import doctest
import cave
from cave import AIR, STONE, WATER
import config
import cave_view
from cave_view import display
from config import CAVE_PATH, WIN_WIDTH, WIN_HEIGHT

def scan_cave(cavern: list[list[str]]) -> int:
    """Scan the cave for air pockets.  Return the number of
    air pockets encountered.

    >>> cavern_1 = cave.read_cave("data/tiny-cave.txt")
    >>> scan_cave(cavern_1)
    1
    >>> cavern_2 = cave.read_cave("data/cave.txt")
    >>> scan_cave(cavern_2)
    3
    """
   

    air_pocket_count = 0

    # Loop through the rows and columns of the cavern
    for row in range(len(cavern)):
        for col in range(len(cavern[0])):
            # If a cell is an air pocket, increment the count and mark it as visited
            if cavern[row][col] == config.AIR:
                air_pocket_count += 1
    return air_pocket_count

def main():
    doctest.testmod()
    cavern = cave.read_cave(config.CAVE_PATH)
    cave_view.display(cavern,config.WIN_WIDTH, config.WIN_HEIGHT)
    chambers = scan_cave(cavern)
    print(f"Found {chambers} chambers")
    cave_view.redisplay(cavern)
    cave_view.prompt_to_close()


if __name__ == "__main__":
    main()
