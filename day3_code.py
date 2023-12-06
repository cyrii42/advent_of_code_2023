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

'''
--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

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

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

'''

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
    previous_row: str = field(init=False, repr=False)
    same_row: str = field(init=False, repr=False)
    next_row: str = field(init=False, repr=False)
    adjacent_to_symbol: bool = field(init=False)

    def __post_init__(self):
        self.num_int = int(self.num_string)
        self.previous_row = ('' if (self.line_num) == 0 else self.schematic_list[self.line_num - 1])
        self.same_row = self.schematic_list[self.line_num]
        self.next_row = ('' if self.line_num == (len(self.schematic_list)-1) else self.schematic_list[self.line_num+1])
        self.final_index = (len(self.schematic_list[self.line_num]) - 1)
        self.adjacent_to_symbol = self.test_number_adjacency()

    def test_number_adjacency(self) -> bool:
        ''' Tests whether this `SchematicNumber` is adjacent to a symbol.'''
        start_minus_one = (0 if (self.idx_start == 0) else (self.idx_start - 1))
        end_plus_one = (self.final_index if (self.idx_end == self.final_index) else (self.idx_end + 1))
        
        characters_to_check = (
            self.same_row[start_minus_one:end_plus_one] +
            self.previous_row[start_minus_one:end_plus_one] +
            self.next_row[start_minus_one:end_plus_one]
        )

        if any([(x in SYMBOL_LIST) for x in characters_to_check]):
            return True
        else:
            return False
        
        
@dataclass
class SchematicRow():
    row_num: int
    row: str = field(repr=False)
    row_list: list[str] = field(repr=False)
    numbers_in_row: list[SchematicNumber] = field(init=False)
    adjacent_nums: list[int] = field(init=False)
    sum_of_adjacent_nums: int = field(init=False)
    
    def __post_init__(self) -> None:
        self.numbers_in_row = self.find_numbers()
        self.previous_row = ('' if self.row_num == 0 else self.row_list[self.row_num - 1])
        self.next_row = ('' if (self.row_num == (len(self.row_list)-1)) else self.row_list[self.row_num + 1])
        self.adjacent_nums = [x.num_int for x in self.numbers_in_row if x.adjacent_to_symbol]
        self.sum_of_adjacent_nums = sum(self.adjacent_nums)
        
    
    def find_numbers(self) -> list[SchematicNumber]:
        ''' Finds numbers in this `SchematicRow` and outputs a list of `SchematicNumber` objects.'''
        output_list = []
        for i, char in enumerate(self.row):
            if char.isnumeric() and (self.row[i-1].isnumeric() == False):
                num_string = char
                for x in range(i+1,len(self.row)):
                    if self.row[x].isnumeric():
                        num_string = num_string + self.row[x]
                        continue
                    else:
                        break
                output_list.append(SchematicNumber(self.row_num, num_string, i, i+len(num_string), self.row_list))
            else:
                continue
        return output_list


class Schematic():
    def __init__(self, input: str):
        self.input_string = input
        self.row_list = self.input_string.split(sep='\n')
        self.symbol_list = [x for x in set(self.input_string) if x.isnumeric() == False and x != '.']
        self.row_objects = [SchematicRow(i, x, self.row_list) for (i, x) in enumerate(self.row_list)]
        self.row_sums = [x.sum_of_adjacent_nums for x in self.row_objects]
    
    def find_total(self) -> int:
        ''' Finds the sum of all `SchematicNumber` objects in this `Schematic`.'''
        total = 0
        for subtotal in self.row_sums:
            total = total + subtotal
        return total
        
    
def main():
    with open('./inputs/day3.txt') as file:
        puzzle_input_string = file.read()
        
    with open('./inputs/day3_test.txt') as file:
        test_input_string = file.read()

    schematic = Schematic(puzzle_input_string)
    
    for row in schematic.row_objects:
        print(f"\nRow {row.row_num - 1}:    {row.previous_row}")
        print(f"*Row {row.row_num}*:  {row.row}")
        print(f"Row {row.row_num + 1}:    {row.next_row}") 
        print(f"Adjacent nums:  {row.adjacent_nums}")
        print(f"Sum of adjacent nums:  {row.sum_of_adjacent_nums}")
        
    print(f"\nGRAND TOTAL:  {schematic.find_total()}")


if __name__ == '__main__':
    main()