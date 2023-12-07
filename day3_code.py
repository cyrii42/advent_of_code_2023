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
    row_num: int
    num_string: str
    idx_start: int
    idx_end: int
    schematic_list: list[str] = field(repr=False)
    adjacent_to_symbol: bool = field(init=False)
    adjacent_to_asterisk: bool = field(init=False)
    

    def __post_init__(self):
        self.num_int = int(self.num_string)
        self.previous_row = ('' if (self.row_num) == 0 else self.schematic_list[self.row_num - 1])
        self.same_row = self.schematic_list[self.row_num]
        self.next_row = ('' if self.row_num == (len(self.schematic_list)-1) else self.schematic_list[self.row_num+1])
        self.final_index = (len(self.schematic_list[self.row_num]) - 1)
        # self.start_minus_two = (0 if (self.idx_start == 0) else (self.idx_start - 2))
        # self.end_plus_one = ((self.final_index) if (self.idx_end == self.final_index-1) else (self.idx_end + 1))
        # # self.characters_to_check = (self.same_row[self.start_minus_two:self.end_plus_one] +
        # #                     self.previous_row[self.start_minus_two:self.end_plus_one] +
        # #                     self.next_row[self.start_minus_two:self.end_plus_one])
        # self.characters_to_check = (self.same_row[self.idx_start-2:self.idx_end+1] +
        #                     self.previous_row[self.idx_start-2:self.idx_end+1] +
        #                     self.next_row[self.idx_start-2:self.idx_end+1])
        self.adjacent_to_symbol = self.test_number_adjacency()
        self.adjacent_to_asterisk = self.test_number_adjacency_to_asterisk()

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
        
    def test_number_adjacency_to_asterisk(self) -> bool:
        ''' Tests whether this `SchematicNumber` is adjacent to an asterisk.'''
        start_minus_one = (0 if (self.idx_start == 0) else (self.idx_start - 1))
        end_plus_one = (self.final_index if (self.idx_end == self.final_index) else (self.idx_end + 1))
        
        characters_to_check = (
            self.same_row[start_minus_one:end_plus_one] +
            self.previous_row[start_minus_one:end_plus_one] +
            self.next_row[start_minus_one:end_plus_one]
        )

        if any([(x in ['*']) for x in characters_to_check]):
            return True
        else:
            return False
        
        
@dataclass
class SchematicAsterisk():
    row_num: int
    index: int
    schematic_list: list[str] = field(repr=False)
    is_gear: bool = field(init=False)

    def __post_init__(self):
        self.previous_row = ('' if (self.row_num) == 0 else self.schematic_list[self.row_num - 1])
        self.same_row = self.schematic_list[self.row_num]
        self.next_row = ('' if self.row_num == (len(self.schematic_list)-1) else self.schematic_list[self.row_num+1])
        self.final_index = (len(self.schematic_list[self.row_num]) - 1)
        self.characters_to_check = (self.previous_row[self.index-1:self.index+2] +
                                    self.same_row[self.index-1:self.index+2] +
                                    self.next_row[self.index-1:self.index+2])
        self.is_gear = self.test_gear_status()

    def test_gear_status(self) -> bool:
        ''' Tests whether this `SchematicAsterisk` qualifies as a "gear," and outputs a boolean.  
            If output is `True`, this method proceeds to set values for `self.num1`, `self.num2`, and `self.gear_ratio`'''
        
        print(f"\nChecking asterisk found in Row #{self.row_num}... Chars to check:  {self.characters_to_check}")

        if len([x for x in self.characters_to_check if x.isnumeric()]) <= 1:
            print("No adjacent numeric characters found.")
            return False
        else:
            print(f"Numeric characters found!  Processing...")
            self.__process_numeric_characters()
            
    def __process_numeric_characters(self) -> list[dict]:
        ''' Private method, to be called only if `test_gear_status()` determines that there exist at least two 
            numeric characters adjacent to this `SchematicAsterisk`.  This method:
            
            - (1) determines whether the set of found numeric characters include exactly two discrete, non-adjacent integers;
            - (2) if so, sets values for `self.num1`, `self.num2`, and `self.gear_ratio`'''
            
        char_dicts_list = self.__create_char_dictionaries()
        print(char_dicts_list)
        full_numbers = self.__find_full_numbers_from_list_of_dicts(char_dicts_list)
        print(full_numbers)
        
        
        
    def __create_char_dictionaries(self) -> list[dict]:
        ''' Returns a list of dictionaries containing, for each numeric character found:
            - (a) the character
            - (b) the row number
            - (c) the index position'''
        list_of_dicts = []
        for n, row in enumerate([self.previous_row, self.same_row, self.next_row]):
            row_num = self.row_num + (n - 1)
            for i, char in enumerate(row[self.index-1:self.index+2]):
                if char.isnumeric():
                    print(f"Found a numeric character!  {char} in row {row_num} at index {i}")
                    char_dict = {'character': char, 'row_num': row_num, 'index': i}
                    list_of_dicts.append(char_dict)
        return list_of_dicts
        
        
            
    def __find_full_numbers_from_list_of_dicts(self, input_list_of_dicts: list[dict]) -> list[dict]:
        ''' Private method.  Takes a list of dictionaries from `__create_char_dictionaries()` and
            determines the corresponding full number for each.  Outputs a list of dictionaries, each
            of which contains:
            
            - (1) the full number (as an integer)
            - (2) the starting index position
            - (3) the ending index position'''
        
        prev_row_dicts = [x for x in input_list_of_dicts if x['row_num'] == (self.row_num - 1)]
        same_row_dicts = [x for x in input_list_of_dicts if x['row_num'] == (self.row_num + 0)]
        next_row_dicts = [x for x in input_list_of_dicts if x['row_num'] == (self.row_num + 1)]
        
        output_list_of_dicts = []
        for n, char_dicts_list in enumerate([prev_row_dicts, same_row_dicts, next_row_dicts]):
            row_num = self.row_num + (n - 1)
            print(f"Length of current 'char_dicts_list':  {len(char_dicts_list)}")
            # if the current row has no num chars, just move on to the next row
            if len(char_dicts_list) == 0:
                continue  
            
            # if the current row has ONE num char (or THREE, which means one continguous one), find its full number & move on
            elif (len(char_dicts_list) == 1 or len(char_dicts_list) == 3):
                full_num_dict = self.__find_full_number_for_num_char(char_dicts_list[0])
                output_list_of_dicts.append(full_num_dict)    
                continue
                
            # if the current row has EXACTLY TWO num chars, check if they're contiguous;
            elif ((char_dicts_list[1]['index'] - char_dicts_list[0]['index']) == 1):
                print("Found a two-digit contiguous num")
                full_num_dict = self.__find_full_number_for_num_char(char_dicts_list[0])
                output_list_of_dicts.append(full_num_dict)    
                continue
            
            # if the current row has EXACTLY TWO num char and they're NOT contiguous, find the full number for each one
            else:
                print("Found two NON-contiguous num chars!!!!!!!!!!!!!")
                full_num_dict_1 = self.__find_full_number_for_num_char(char_dicts_list[0])
                output_list_of_dicts.append(full_num_dict_1)    
                full_num_dict_2 = self.__find_full_number_for_num_char(char_dicts_list[1])
                output_list_of_dicts.append(full_num_dict_2)    
                
        return output_list_of_dicts
    
    def __find_full_number_for_num_char(self, input_dict: dict) -> dict:
        print(f"Finding full number for {input_dict}")
        return "SDSFHSDFOHSDOFIHSDOFIH"
        
        
@dataclass
class SchematicRow():
    row_num: int
    row: str = field(repr=False)
    row_list: list[str] = field(repr=False)
    numbers_in_row: list[SchematicNumber] = field(init=False, repr=False)
    adjacent_nums: list[int] = field(init=False, repr=False)
    sum_of_adjacent_nums: int = field(init=False, repr=False)
    
    def __post_init__(self) -> None:
        self.numbers_in_row = self.find_numbers()
        self.previous_row = ('' if self.row_num == 0 else self.row_list[self.row_num - 1])
        self.next_row = ('' if (self.row_num == (len(self.row_list)-1)) else self.row_list[self.row_num + 1])
        self.adjacent_nums = [x.num_int for x in self.numbers_in_row if x.adjacent_to_symbol]
        self.sum_of_adjacent_nums = sum(self.adjacent_nums)
        self.asterisks_in_row = self.find_asterisks()
        
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
    
    def find_asterisks(self) -> list[SchematicAsterisk]:
        # schematicnumbers_adj_to_asterisks = [x for x in self.find_numbers() if x.adjacent_to_asterisk]
        # return schematicnumbers_adj_to_asterisks
        
        ''' Finds asterisk symbols in this `SchematicRow` and outputs a list of `SchematicAsterisk` objects.'''
        output_list = []
        for i, char in enumerate(self.row):
            if char == '*':
                output_list.append(SchematicAsterisk(self.row_num, i, self.row_list))
            else:
                continue
        return output_list  #if len(output_list) > 0 else None
    
    def print_adjacent_rows_part_one(self) -> None:
        print(f"\nRow {self.row_num - 1}:    {self.previous_row}") if self.row_num > 0 else print('')
        print(f"*Row {self.row_num}*:  {self.row}")
        print(f"Row {self.row_num + 1}:    {self.next_row}") if self.row_num < len(self.row_list)-1 else print('END')
        print(f"Adjacent nums:  {self.adjacent_nums}")
        print(f"Sum of adjacent nums:  {self.sum_of_adjacent_nums}")
        
    def print_adjacent_rows_part_two(self) -> None:
        print(f"\nRow {self.row_num - 1}:    {self.previous_row}") if self.row_num > 0 else print('START')
        print(f"*Row {self.row_num}*:  {self.row}")
        print(f"Row {self.row_num + 1}:    {self.next_row}") if self.row_num < len(self.row_list)-1 else print('END')
        # print(self.find_asterisks())
        # print(f"# of asterisks in Row {self.row_num}:  {len(self.asterisks_in_row)}")


class Schematic():
    def __init__(self, input: str):
        self.input_string = input
        self.row_list = self.input_string.split(sep='\n')
        self.symbol_list = [x for x in set(self.input_string) if x.isnumeric() == False and x != '.']
        self.row_objects = [SchematicRow(i, x, self.row_list) for (i, x) in enumerate(self.row_list)]
        self.part_one_row_sums = [x.sum_of_adjacent_nums for x in self.row_objects]
    
    def find_part_one_total(self) -> int:
        ''' Finds the sum of all `SchematicNumber` objects in this `Schematic`.'''
        total = 0
        for subtotal in self.part_one_row_sums:
            total = total + subtotal
        return total
    
    def find_part_two_total(self) -> int:
        ''' Finds the sum of all "gear ratios" 'in this `Schematic`.'''
        pass
        
    
    



    
def part_two(puzzle_string: str) -> None:
    schematic = Schematic(puzzle_string)

    # for row in schematic.row_objects:
        # row.print_adjacent_rows_part_two()
        # print(row.find_asterisks())
        
        
        
        
        

def part_one(puzzle_string: str) -> None:
    schematic = Schematic(puzzle_string)
    
    for row in schematic.row_objects:
        row.print_adjacent_rows_part_one()
        
    print(f"\nGRAND TOTAL:  {schematic.find_part_one_total()}")


def main():
    with open('./inputs/day3.txt') as file:
        puzzle_input_string = file.read()
        
    with open('./inputs/day3_test.txt') as file:
        test_input_string = file.read()
        
    # part_one(puzzle_input_string)  ## answer should be 526404
    part_two(puzzle_input_string)  
    

if __name__ == '__main__':
    main()