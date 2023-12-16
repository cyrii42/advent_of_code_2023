'''
--- Day 8: Haunted Wasteland ---

You're still riding a camel across Desert Island when you spot a sandstorm quickly approaching. When you turn to warn the Elf, she disappears before your eyes! To be fair, she had just finished warning you about ghosts a few minutes ago.

One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about how to navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains a list of left/right instructions, and the rest of the documents seem to describe some kind of network of labeled nodes.

It seems like you're meant to use the left/right instructions to navigate the network. Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!

After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now, and you have to follow the left/right instructions until you reach ZZZ.

This format defines each node of the network individually. For example:

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)

Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.

Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes 6 steps to reach ZZZ:

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)

Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

--- Part Two ---

The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had the camel follow the instructions, but you've barely left your starting position. It's going to take significantly more steps to escape!

What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of spacetime? Only one way to find out.

After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

For example:

LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)

Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

    Step 0: You are at 11A and 22A.
    Step 1: You choose all of the left paths, leading you to 11B and 22B.
    Step 2: You choose all of the right paths, leading you to 11Z and 22C.
    Step 3: You choose all of the left paths, leading you to 11B and 22Z.
    Step 4: You choose all of the right paths, leading you to 11Z and 22B.
    Step 5: You choose all of the left paths, leading you to 11B and 22C.
    Step 6: You choose all of the right paths, leading you to 11Z and 22Z.

So, in this example, you end up entirely on nodes that end in Z after 6 steps.

Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?

'''
from pprint import pprint
from datetime import datetime
from dataclasses import dataclass, field
import math

@dataclass
class Ghost():
    start: str
    maps_dict: dict
    instructions_str: str

    def __post_init__():
        pass

    
with open('./inputs/day8.txt') as file:
    line_list = file.read().split(sep='\n')
instructions_str = line_list.pop(0)
maps_dict = {row[0:3]: (row[7:10], row[12:15]) for row in line_list[1:]}




def find_node_ending_in_Z(starting_point: str) -> tuple:
    total = 0
    next_location = starting_point
    while True:
        for dir in instructions_str:
            total += 1
            current_location = maps_dict[next_location]
            if dir == 'L':
                next_location = current_location[0]
            else:
                next_location = current_location[1]
                
            if next_location[2] == 'Z':
                print(f"\nPart Two:  Went from {starting_point} to {next_location} in {total} steps!")
                return (starting_point, next_location, total)




def part_two():
    list_a = [x for x in maps_dict.keys() if x[2] == 'A']

    a_to_z_list = []
    for starting_point in list_a:
        a_to_z_list.append(find_node_ending_in_Z(starting_point))
    print(f"\nTuple List:  {a_to_z_list}")
  
    print(f"\nLeast Common Multiple (i.e., Part Two Answer):  {math.lcm(*[x[2] for x in a_to_z_list]):,}")  # correct answer is 22103062509257


def show_info():
    list_a = [x for x in maps_dict.keys() if x[2] == 'A']

    line_list_sorted = sorted(line_list[1:], key=lambda x: x[2])
    final_letter_set = sorted(list(set([x[2] for x in line_list[1:]])))  # 20: ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z']

    group_list = []
    for letter in final_letter_set:
        # group_list.append(sorted([x for x in line_list[1:] if x[2] == letter], key=lambda x: (x[2], x[0], x[1])))
        group_list.append([x for x in line_list[1:] if x[2] == letter])

    part_two_maps_dict = {x[0][2]: x for x in group_list}
    for (key, value) in part_two_maps_dict.items():
        print(f"{key}:  {len(value)}")
    pprint(part_two_maps_dict)
    

def main():
    part_one()
    part_two()













def part_one() -> int:
    with open('./inputs/day8.txt') as file:
        line_list = file.read().split(sep='\n')
    instructions_str = line_list.pop(0)
    maps_dict = {row[0:3]: (row[7:10], row[12:15]) for row in line_list[1:]}
    
    total = 0
    next_location = 'AAA'
    while True:
        for dir in instructions_str:
            total += 1
            current_location = maps_dict[next_location]
            if dir == 'L':
                next_location = current_location[0]
            else:
                next_location = current_location[1]
                
            if next_location == 'ZZZ':
                print(f"\nPart One:  Found ZZZ in {total} steps!")
                return total






if __name__ == '__main__':
    main()







    # list_a = [x for x in maps_dict.keys() if x[2] == 'A']

    # line_list_sorted = sorted(line_list[1:], key=lambda x: x[2])
    # final_letter_set = sorted(list(set([x[2] for x in line_list[1:]])))  # 20: ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z']

    # group_list = []
    # for letter in final_letter_set:
    #     # group_list.append(sorted([x for x in line_list[1:] if x[2] == letter], key=lambda x: (x[2], x[0], x[1])))
    #     group_list.append([x for x in line_list[1:] if x[2] == letter])

    # part_two_maps_dict = {x[0][2]: x for x in group_list}
    # for (key, value) in part_two_maps_dict.items():
    #     print(f"{key}:  {len(value)}")
    # pprint(part_two_maps_dict)













# def part_two() -> int:
#     list_a = [x for x in maps_dict.keys() if x[2] == 'A']
#     list_z = [x for x in maps_dict.keys() if x[2] == 'Z']
#     # GROUP_SIZE = len(list_a)

#     total = 0
#     starting_point_list = [starting_point for (starting_point, options) in maps_dict.items() if starting_point[2] == 'A']
#     options_list = [options for (starting_point, options) in maps_dict.items() if starting_point[2] == 'A']
#     REPORTING_CHUNK_SIZE = 1_000_000
#     while True:
#         for dir in instructions_str:
#             total += 1
#             if total == 1 or total % REPORTING_CHUNK_SIZE == 0:
#                 print(f"{datetime.now().strftime('%-I:%M:%S %p')}:  Trying {starting_point_list} at Step #{total:,}...")
#             new_starting_point_list = []
#             for starting_point in starting_point_list:
#                 options = maps_dict[starting_point]
#                 if dir == 'L':
#                     starting_point = options[0]
#                 else:
#                     starting_point = options[1]
#                 new_starting_point_list.append(starting_point)
#             last_letter_set = set([x[2] for x in new_starting_point_list])
#             if len(last_letter_set) == 1 and 'Z' in last_letter_set:
#                 print(f"\nPart Two:  Found ZZZ in {total} steps!")
#                 return total
#         starting_point_list = new_starting_point_list



        # line_list_sorted = sorted(line_list[1:], key=lambda x: x[2])
    # final_letter_set = sorted(list(set([x[2] for x in line_list[1:]])))  # 20: ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z']

    # group_list = []
    # for letter in final_letter_set:
    #     # group_list.append(sorted([x for x in line_list[1:] if x[2] == letter], key=lambda x: (x[2], x[0], x[1])))
    #     group_list.append([x for x in line_list[1:] if x[2] == letter])

    # part_two_maps_dict = {x[0][2]: x for x in group_list}
    # for (key, value) in part_two_maps_dict.items():
    #     print(f"{key}:  {len(value)}")
    # pprint(part_two_maps_dict)