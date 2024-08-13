# symbol_list = ['*', '/', '-', '=', '&', '+', '#', '@', '$', '%']

# print(any([(x in symbol_list) for x in "as@sdf"]))

# print(len(symbol_list) - 1)

# asdf = "a----b"
# print(asdf[0])
# print(asdf[-1])

# num_list = [54, 53, 99, 100, 561, 999, 109234, 4]
# print([x for x in num_list if x in range(54, 100)])

# x = [x for x in range(5, 10)]
# y = [x for x in range(1, 20)]

# print(x == y)
# print(y == x)
# print(len(y))

# seed_range_length = 54001
# chunk_size = 100
# num_subranges = ((seed_range_length // chunk_size) + 1) if ((seed_range_length % chunk_size) != 0) else (seed_range_length // chunk_size)
# print(num_subranges)

# def create_subranges(seed_range_length: int) -> list[range]:
#     chunk_size = 10000
#     num_subranges = ((seed_range_length // chunk_size) + 1) if ((seed_range_length % chunk_size) != 0) else (seed_range_length // chunk_size)
    
#     output_list = []
#     for n in range(num_subranges):
#         output_list.append(range(chunk_size*n, min(seed_range_length, chunk_size*(n+1))))
        
#     return output_list

# print(create_subranges(350401))

# import itertools

# r1 = range(44, 59)
# r2 = range(51, 64)

# woii = itertools.chain(r1, r2)
# print(woii)

# r1 = range(234333330, 41223333333)
# r2 = range(1, 4293846239846)

# def is_in(x):
#     return x in r1

# print(any(map(is_in, r2)))

# from enum import IntEnum

# CARD_LIST = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# class HandType(IntEnum):
#     FIVE_OF_A_KIND = 6
#     FOUR_OF_A_KIND = 5
#     FULL_HOUSE = 4
#     THREE_OF_A_KIND = 3
#     TWO_PAIR = 2
#     ONE_PAIR = 1
#     HIGH_CARD = 0
    
# hand_list = [HandType.FULL_HOUSE, HandType.HIGH_CARD, HandType.ONE_PAIR, HandType.FOUR_OF_A_KIND, HandType.FOUR_OF_A_KIND, HandType.FULL_HOUSE, HandType.THREE_OF_A_KIND]

# hand_list_sorted = sorted(hand_list, reverse=True)
# print(hand_list_sorted)

# asdf = "A2JA3JKQA"
# # print(asdf.replace('J', ''))
# # print(asdf)
# # print(''.join(sorted(asdf.replace('J', ''), key=lambda x: asdf.count(x), reverse=True)))
# print(asdf[0])

# asdf = ['EFZ', 'OQZ', 'ZZZ', 'FEZ']
# print(asdf)
# aaaa = set([x[2] for x in asdf])
# print(len(aaaa))
# print('Z' in aaaa)
# print(set(asdf))

# woii = [0,0,0,0,0]
# print(set(woii) == {0})

# asdf = [0, 3, 6, 9, 12, 15]
# print(asdf[-2])

from enum import Enum
from typing import Any, Iterable
class Pipe(Enum):
    START = 'S'
    VERTICAL = '|'
    HORIZONTAL = '-'
    NORTH_TO_EAST = 'L'
    NORTH_TO_WEST = 'J'
    SOUTH_TO_WEST = '7'
    SOUTH_TO_EAST = 'F'
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

asdf = ['EFZ', 'OQZ', 'ZZZ', 'FEZ']

for x in Direction.__iter__():
    print(x)