'''
--- Day 10: Pipe Maze ---

You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island. This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang glider behind.

You wander around for a while, but you don't find any people or animals. However, you do occasionally find signposts labeled "Hot Springs" pointing in a seemingly consistent direction; maybe you can find someone at the hot springs and ask them where the desert-machine parts are made.

The landscape here is alien; even the flowers and trees are made of metal. As you stop to admire some metal grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.

Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of tiles:

    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is one large, continuous loop.

For example, here is a square loop of pipe:

.....
.F-7.
.|.|.
.L-J.
.....

If the animal had entered this loop in the northwest corner, the sketch would instead look like this:

.....
.S-7.
.|.|.
.L-J.
.....

In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop as above:

-L|F7
7S-7|
L|7||
-L-J|
L|-JF

In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to S, pipes those pipes connect to, pipes those pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including S, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...

Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:

7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ

If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps along the loop to reach from the starting point - regardless of which way around the loop the animal went.

In the first example with the square loop:

.....
.S-7.
.|.|.
.L-J.
.....

You can count the distance each tile in the loop is from the starting point like this:

.....
.012.
.1.3.
.234.
.....

In this example, the farthest point from the start is 4 steps away.

Here's the more complex loop again:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...

Here are the distances for each tile on that loop:

..45.
.236.
01.78
14567
23...

Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?

--- Part Two ---

You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is within the area enclosed by the loop?

To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop. For example:

...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........

The above loop encloses merely four tiles - the two pairs of . in the southwest and southeast (marked I below). The middle . tiles (marked O below) are not in the loop. Here is the same loop again with those regions marked:

...........
.S-------7.
.|F-----7|.
.||OOOOO||.
.||OOOOO||.
.|L-7OF-J|.
.|II|O|II|.
.L--JOL--J.
.....O.....

In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, I is still within the loop and O is still outside the loop:

..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........

In both of the above examples, 4 tiles are enclosed by the loop.

Here's a larger example:

.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...

The above sketch has many random bits of ground, some of which are in the loop (I) and some of which are outside it (O):

OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO

In this larger example, 8 tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L

Here are just the tiles that are enclosed by the loop marked with I:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L

In this last example, 10 tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the area within the loop. How many tiles are enclosed by the loop?

'''

from dataclasses import dataclass, field
from enum import Enum

class Pipe(Enum):
    START = 'S'
    VERTICAL = '|'
    HORIZONTAL = '-'
    NORTH_TO_EAST = 'L'
    NORTH_TO_WEST = 'J'
    SOUTH_TO_EAST = 'F'
    SOUTH_TO_WEST = '7'
    GROUND = '.'

class Direction(Enum):
    NORTH = 'N'
    NORTH_EAST = 'NE'
    EAST = 'E'
    SOUTH_EAST = 'SE'
    SOUTH = 'S'
    SOUTH_WEST = 'SW'
    WEST = 'W'
    NORTH_WEST = 'NW'

@dataclass
class MapChar():
    row_num: int
    index: int
    char: Pipe #= field(repr=False)
    north: Pipe = field(repr=False)
    north_east: Pipe = field(repr=False)
    east: Pipe = field(repr=False)
    south_east: Pipe = field(repr=False)
    south: Pipe = field(repr=False)
    south_west: Pipe = field(repr=False)
    west: Pipe = field(repr=False)
    north_west: Pipe = field(repr=False)
    connection_1: Direction | None = field(init=False)
    connection_2: Direction | None = field(init=False)
    part_of_main_loop: bool = False

    def __post_init__(self) -> None:
        self.find_connections_from_start() if self.char == Pipe.START else self.find_connections()

    def find_connections(self) -> None:
        if self.char == Pipe.VERTICAL:
            self.connection_1 = Direction('N') if self.north is not None else None
            self.connection_2 = Direction('S') if self.south is not None else None
        elif self.char == Pipe.HORIZONTAL:
            self.connection_1 = Direction('E') if self.east is not None else None
            self.connection_2 = Direction('W') if self.west is not None else None
        elif self.char == Pipe.NORTH_TO_EAST:
            self.connection_1 = Direction('N') if self.north is not None else None
            self.connection_2 = Direction('E') if self.east is not None else None
        elif self.char == Pipe.NORTH_TO_WEST:
            self.connection_1 = Direction('N') if self.north is not None else None
            self.connection_2 = Direction('W') if self.west is not None else None
        elif self.char == Pipe.SOUTH_TO_EAST:
            self.connection_1 = Direction('S') if self.south is not None else None
            self.connection_2 = Direction('E') if self.east is not None else None
        elif self.char == Pipe.SOUTH_TO_WEST:
            self.connection_1 = Direction('S') if self.south is not None else None
            self.connection_2 = Direction('W') if self.west is not None else None
        else:
            self.connection_1 = None
            self.connection_2 = None

    def find_connections_from_start(self) -> None:
        conn_list = []
        if self.north == Pipe.VERTICAL or self.north == Pipe.SOUTH_TO_EAST or self.north == Pipe.SOUTH_TO_WEST:
            conn_list.append(Direction('N')) if self.north is not None else conn_list.append(None)
        if self.east == Pipe.HORIZONTAL or self.east == Pipe.NORTH_TO_WEST or self.east == Pipe.SOUTH_TO_WEST:
            conn_list.append(Direction('E')) if self.east is not None else conn_list.append(None)
        if self.south == Pipe.VERTICAL or self.south == Pipe.NORTH_TO_EAST or self.south == Pipe.NORTH_TO_WEST:
            conn_list.append(Direction('S')) if self.south is not None else conn_list.append(None)
        if self.west == Pipe.HORIZONTAL or self.west == Pipe.NORTH_TO_EAST or self.west == Pipe.SOUTH_TO_EAST:
            conn_list.append(Direction('W')) if self.west is not None else conn_list.append(None)
        if len(conn_list) != 2:
            raise ConnectionNumError(f"Starting MapChar must have exactly 2 connections; this one has {len(conn_list)}")
        else:
            self.connection_1 = conn_list[0]
            self.connection_2 = conn_list[1]

@dataclass
class Map():
    char_list: list[MapChar] = field(repr=False)
    starting_point: MapChar = field(init=False)
    steps_to_farthest_point: int = field(init=False)

    def __post_init__(self) -> None:
        self.starting_point = next(filter(lambda x: x.char == Pipe.START, self.char_list))
        self.steps_to_farthest_point = self.calculate_steps_to_farthest_point()
        self.tiles_enclosed_by_loop = self.calculate_tiles_enclosed_by_loop()

    def calculate_tiles_enclosed_by_loop(self) -> int:
        total = 0
        for mapchar in self.char_list:
            if mapchar.part_of_main_loop:
                continue
            else:
                # print([dir for dir in Direction.__iter__()])
                print(f"Checking {mapchar}...")
                char_list = [self.get_mapchar_from_direction(mapchar, dir) for dir in Direction.__iter__()]
                # print(f"Checking {char_list}")
                if any([char for char in char_list if char is None or char.part_of_main_loop == False]):
                    continue
            total += 1
        return total

    def calculate_steps_to_farthest_point(self) -> int:
        current_pipe = self.starting_point
        previous_pipe = current_pipe
        current_pipe.part_of_main_loop = True
        steps = 0
        while True:
            print(f"Trying {current_pipe}...")
            if steps == 0:
                next_pipe = self.get_mapchar_from_direction(current_pipe, current_pipe.connection_1)
            elif self.get_mapchar_from_direction(current_pipe, current_pipe.connection_1) != previous_pipe:
                next_pipe = self.get_mapchar_from_direction(current_pipe, current_pipe.connection_1)
            else:
                next_pipe = self.get_mapchar_from_direction(current_pipe, current_pipe.connection_2)
            next_pipe.part_of_main_loop = True
            if steps > 0 and next_pipe.char == Pipe.START:
                print(f"Found Pipe:  {next_pipe}")
                return steps // 2 + 1
            previous_pipe = current_pipe
            current_pipe = next_pipe
            steps += 1

    def get_mapchar_from_direction(self, mapchar: MapChar, direction: Direction) -> MapChar:
        if direction == Direction.NORTH:
            return None if mapchar.row_num == 0 else next(filter(lambda x: x.row_num == mapchar.row_num-1 and x.index == mapchar.index, self.char_list))
        if direction == Direction.NORTH_EAST:
            return None if mapchar.row_num == 0 or mapchar.index == 139 else next(filter(lambda x: x.row_num == mapchar.row_num-1 and x.index == mapchar.index+1, self.char_list))
        if direction == Direction.EAST:
            return None if mapchar.index == 139 else next(filter(lambda x: x.row_num == mapchar.row_num and x.index == mapchar.index+1, self.char_list))
        if direction == Direction.SOUTH_EAST:
            return None if mapchar.row_num == 139 or mapchar.index == 139 else next(filter(lambda x: x.row_num == mapchar.row_num+1 and x.index == mapchar.index+1, self.char_list))
        if direction == Direction.SOUTH:
            return None if mapchar.row_num == 139 else next(filter(lambda x: x.row_num == mapchar.row_num+1 and x.index == mapchar.index, self.char_list))
        if direction == Direction.SOUTH_WEST:
            return None if mapchar.row_num == 139 or mapchar.index == 0 else next(filter(lambda x: x.row_num == mapchar.row_num+1 and x.index == mapchar.index-1, self.char_list))
        if direction == Direction.WEST:
            return  None if mapchar.index == 0 else next(filter(lambda x: x.row_num == mapchar.row_num and x.index == mapchar.index-1, self.char_list))
        if direction == Direction.NORTH_WEST:
            return None if mapchar.row_num == 0 or mapchar.index == 0 else next(filter(lambda x: x.row_num == mapchar.row_num-1 and x.index == mapchar.index-1, self.char_list))

    


def main():
    map = create_map()
    print(map.starting_point)
    print(f"\nPart Two Answer:  {map.tiles_enclosed_by_loop}")  # 322 is too low

    
def create_map() -> Map:
    with open('./inputs/day10.txt') as file:
        line_list = file.read().split(sep='\n')

    map_char_list = []
    for row_num, row in enumerate(line_list):
        if row_num == 0:
            map_char_list.append(
                [MapChar(row_num, i, Pipe(char), 
                        None,                                                       # north
                        None,                                                       # north_east
                        Pipe(line_list[row_num][i+1]) if i < len(row)-1 else None,    # east
                        Pipe(line_list[row_num+1][i+1]) if i< len(row)-1 else None,   # south_east
                        Pipe(line_list[row_num+1][i]),                              # south
                        Pipe(line_list[row_num+1][i-1]),                              # south_west
                        Pipe(line_list[row_num][i-1]),                              # west
                        None,                                                         # north_west
                    ) for (i, char) in enumerate(row)])
        elif row_num >= len(line_list)-1:
            map_char_list.append(
                [MapChar(row_num, i, Pipe(char), 
                        Pipe(line_list[row_num-1][i]),                              # north
                        Pipe(line_list[row_num-1][i+1])  if i < len(row)-1 else None, # north_east
                        Pipe(line_list[row_num][i+1]) if i < len(row)-1 else None,    # east
                        None,                                                       # south_east
                        None,                                                       # south
                        None,                                                         # south_west
                        Pipe(line_list[row_num][i-1]),                              # west
                        Pipe(line_list[row_num-1][i-1]),                              # north_west
                    ) for (i, char) in enumerate(row)])
        else:
            map_char_list.append(
                [MapChar(row_num, i, Pipe(char), 
                        Pipe(line_list[row_num-1][i]),                              # north
                        Pipe(line_list[row_num-1][i+1]) if i < len(row)-1 else None,  # north_east
                        Pipe(line_list[row_num][i+1]) if i < len(row)-1 else None,    # east
                        Pipe(line_list[row_num+1][i+1]) if i< len(row)-1 else None,   # south_east
                        Pipe(line_list[row_num+1][i]),                              # south
                        Pipe(line_list[row_num+1][i-1]),                              # south_west
                        Pipe(line_list[row_num][i-1]),                              # west
                        Pipe(line_list[row_num-1][i-1]),                              # north_west
                    ) for (i, char) in enumerate(row)])
            
    return Map([char for row in map_char_list for char in row])


class ConnectionNumError(Exception):
    ''' To be raised when a `MapChar` has less or more than 2 connections.'''
    pass

if __name__ == '__main__':
    main()
