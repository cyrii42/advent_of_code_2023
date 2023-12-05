'''--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:'''

test_string = '''
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
'''

'''In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
'''

from day3_input import day3_input_full as input_string
from day3_input import day3_input_list as input_list

input_string = input_string.replace('\n','')
symbol_list = [x for x in set(input_string) if x.isnumeric() == False and x != '.']

test_list = ['467..114..', '...*......', '..35..633.', '......#...', '617*......', '.....+.58.', '..592.....', '......755.', '...$.*....', '.664.598..']
test_string = test_string     # defined above
symbol_list_test = [x for x in set(test_string) if x.isnumeric() == False and x != '.']



def find_number_indices(line: str) -> list[int]:
    ''' Takes a single line from a schematic and returns a list of indices 
        at which integers can be found in the line.'''

    return [i for (i, char) in enumerate(line) if char.isnumeric()]

for line in test_list:
    print(find_number_indices(line))


            
        



def get_stats() -> None:   
    print(f"# of lines in input list:  {len(input_list)}")
    print(f"# of characters in each line:  {len(input_list[0])}")
    print(f"# of total characters in input string:  {len(input_string)}")  
    print(f"Unique symbols in input string:  {symbol_list}")
    
    # print(f"\n# of lines in test list:  {len(test_list)}")
    # print(f"# of characters in each line:  {len(test_list[0])}")
    # print(f"# of total characters in test string:  {len(test_string)}")
    # print(f"Unique symbols in test string:  {symbol_list}")


# def main():
#     pass

# if __name__ == '__main__':
#     main()