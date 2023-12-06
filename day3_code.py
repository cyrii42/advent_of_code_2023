'''--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?'''

from dataclasses import dataclass, field
from pprint import pprint

SYMBOL_LIST = ['$', '&', '@', '%', '\n', '+', '*', '-', '/', '#', '=']

@dataclass
class SchematicNumber():
    line_num: int
    num_string: str
    idx_start: int
    idx_end: int
    schematic_list: list[str] = field(repr=False)
    num_int: int = field(init=False)
    previous_line: str = field(init=False, repr=False)
    same_line: str = field(init=False, repr=False)
    next_line: str = field(init=False, repr=False)
    adjacent_to_symbol: bool = field(init=False)

    def __post_init__(self):
        self.num_int = int(self.num_string)
        self.previous_line = ('' if (self.line_num) == 0 else self.schematic_list[self.line_num - 1])
        self.same_line = self.schematic_list[self.line_num]
        self.next_line = ('' if self.line_num == (len(self.schematic_list)-1) else self.schematic_list[self.line_num+1])
        self.final_index = (len(self.schematic_list[self.line_num]) - 1)
        self.adjacent_to_symbol = self.test_number_adjacency()

    def test_number_adjacency(self) -> bool:
        ''' Tests whether this `SchematicNumber` is adjacent to a symbol.'''
        start_minus_one = (0 if (self.idx_start == 0) else (self.idx_start - 1))
        end_plus_one = (self.final_index if (self.idx_end == self.final_index) else (self.idx_end + 1))
        
        characters_to_check = (
            self.same_line[start_minus_one:end_plus_one] +
            self.previous_line[start_minus_one:end_plus_one] +
            self.next_line[start_minus_one:end_plus_one]
        )

        if any([(x in SYMBOL_LIST) for x in characters_to_check]):
            return True
        else:
            return False


class Schematic():
    def __init__(self, input_string: str):
        self.input_string = input_string
        self.input_list = self.input_string.split(sep='\n')
        self.symbol_list = [x for x in set(self.input_string) if x.isnumeric() == False and x != '.']

    def find_numbers(self) -> list[SchematicNumber]:
        ''' Finds the numbers in the schematic object.  

        Outputs a list of `SchematicNumber` objects, each of which contains:

        - (1)  an integer corresponding to the line number in the schematic;
        - (2)  a string containing the number itself;
        - (3)  an integer corresponding to the starting index for the number; and
        - (4)  an integer corresponding to the ending index for the number;
        - (5)  a full copy of this `Schematic`'s `input_list`'''

        output_list = []
        for n, line in enumerate(self.input_list):
            for i, char in enumerate(line):
                if char.isnumeric() and (line[i-1].isnumeric() == False):
                    num_string = char
                    for x in range(i+1,(len(line)-1)):
                        if line[x].isnumeric():
                            num_string = num_string + line[x]
                            continue
                        else:
                            break
                    output_list.append(SchematicNumber(n, num_string, i, i+len(num_string), self.input_list))
                else:
                    continue
        return output_list

def main():
    with open('./inputs/day3.txt') as file:
        input_string = file.read()

    test_string = ("467..114.....*........35..633.......#...617*...........+.58...592...........755....$.*.....664.598..")

    schematic = Schematic(input_string)
    schematic_numbers = schematic.find_numbers()

    print(schematic_numbers)

    print(
        sum(
            [x.num_int for x in schematic_numbers if x.adjacent_to_symbol]
        )
    )
    


if __name__ == '__main__':
    main()