'''
--- Day 5: If You Give A Seed A Fertilizer ---

You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.

"A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.

"Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"

You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our food production problem. The latest Island Island Almanac just arrived and we're having trouble making sense of it."

The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

For example:

seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4

The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps that describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.

Consider again the example seed-to-soil map:

50 98 2
52 50 48

The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:

seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51

With this map, you can look up the soil number required for each initial seed number:

    Seed number 79 corresponds to soil number 81.
    Seed number 14 corresponds to soil number 14.
    Seed number 55 corresponds to soil number 57.
    Seed number 13 corresponds to soil number 13.

The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

    Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
    Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
    Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
    Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

So, the lowest location number in this example is 35.

What is the lowest location number that corresponds to any of the initial seed numbers?

--- Part Two ---

Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13

This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?


'''
import itertools
from dataclasses import dataclass, field
from pprint import pprint

from day5_data_ingestion import (process_maps, process_seeds,
                                 process_test_maps, process_test_seeds)


@dataclass
class MapRow():
    destination_range_start: int = field(repr=False)
    source_range_start: int = field(repr=False)
    range_length: int = field(repr=False)
    source_range: range = field(init=False)
    destination_range: range = field(init=False)
    range_tuple: tuple[range] = field(init=False)

    def __post_init__(self) -> None:
        self.destination_range = self.calculate_destination_range()
        self.source_range = self.calculate_source_range()
        self.range_tuple = (self.source_range, self.destination_range)
        
    def calculate_source_range(self) -> range:
        source_range_end = self.source_range_start + self.range_length
        return range(self.source_range_start, source_range_end)

    def calculate_destination_range(self) -> range:
        destination_range_end = self.destination_range_start + self.range_length
        return range(self.destination_range_start, destination_range_end)
    
@dataclass
class Map():
    source_type: str
    destination_type: str
    rows: list[MapRow] = field(repr=False)
    rows_sorted: list[MapRow] = field(init=False, repr=False)
    source_range_list: list[range] = field(init=False, repr=False)
    source_to_range_length_dict: dict = field(init=False)

    def __post_init__(self) -> None:
        self.rows_sorted = sorted([row for row in self.rows], key=lambda x: x.source_range_start)
        self.source_range_list = [row.source_range for row in self.rows_sorted]
        self.source_to_range_length_dict = {row.source_range_start: row.range_length for row in self.rows_sorted}


@dataclass
class Seed():
    seed_num: int


@dataclass
class SeedGroup():
    seed_range_start: int = field(repr=False)
    seed_range_length: int = field(repr=False)
    seed_range_end: int = field(init=False, repr=False)
    seed_range: range = field(init=False)
    
    def __post_init__(self) -> None:
        self.seed_range_end = self.seed_range_start + self.seed_range_length
        self.seed_range = range(self.seed_range_start, (self.seed_range_end))


def main():
    # raw_seeds_list = process_test_seeds()
    # raw_maps_list = process_test_maps()
    raw_seeds_list = process_seeds()
    raw_maps_list = process_maps()
    
    maps_list = create_map_objects(raw_maps_list)
    seed_group_list = create_seed_groups(raw_seeds_list)

    for map in maps_list:
        print(f"\n{map.source_type} to {map.destination_type}:  {map.source_to_range_length_dict}")
        
    # print(f"\n# of Seed Groups:  {len(seed_group_list)}")
    # for n, seed_group in enumerate(seed_group_list):
    #     print(f"Seed Group #{n+1}:  {seed_group.seed_range} ({len(seed_group.seed_range):,} seeds)")      

   

    # for each seed group, determine the seed-to-soil source range in which the starting and ending seed falls
    seed_to_soil_map = maps_list[0]
    for seed_group_num, seed_group in enumerate(seed_group_list):
        seed_group_start = seed_group.seed_range_start
        seed_group_start_range_num = 0
        seed_group_end = seed_group.seed_range_end
        seed_group_end_range_num = 0

        for i, source_range in enumerate(seed_to_soil_map.source_range_list):
            if seed_group_start in source_range:
                seed_group_start_range_num = i
                break

        for i, source_range in enumerate(seed_to_soil_map.source_range_list):
            if seed_group_end in source_range:
                seed_group_end_range_num = i
                break

        print(f"Seed Group #{seed_group_num+1}:  Starts in Seed-to-Soil Range #{seed_group_start_range_num}, ends in Seed-to-Soil Range #{seed_group_end_range_num} (spanning {seed_group_end_range_num - seed_group_start_range_num} ranges)")

    # NEXT STEPS:  
    #   - for each seed group, set an instance variable containing the # of seed-to-soil ranges spanned
    #   - for seed groups that span 2 or more ranges, figure out how to determine the points where the range changes happen
    #   - then, for each seed, you can just take the seed-to-soil range in which the seed falls and add the range length



    part_two_answer = None
    print(f"\nPART #2 ANSWER:  {part_two_answer}")  # correct answer is 41222968

    
    

def create_seed_groups(raw_seeds_list: list[int]) -> list[SeedGroup]:
    range_start_nums = [n for i, n in enumerate(raw_seeds_list) if (i % 2 == 0)]
    range_length_nums = [n for i, n in enumerate(raw_seeds_list) if (i % 2 != 0)]
    seed_group_list = [SeedGroup(range_start_nums[i], range_length_nums[i]) for i, x in enumerate(range_start_nums)]
    return sorted(seed_group_list, key=lambda x: x.seed_range_start)



def create_map_objects(map_coordinate_lists: list[list[list]]) -> list[Map]:
    output_list = []
    for map in map_coordinate_lists:
        output_list.append(Map(map[0], map[1], [MapRow(x[0], x[1], x[2]) for x in map[2]]))

    seed_to_soil = [x for x in output_list if x.source_type == 'seed']
    soil_to_fertilizer = [x for x in output_list if x.source_type == 'soil']
    fertilizer_to_water = [x for x in output_list if x.source_type == 'fertilizer']
    water_to_light = [x for x in output_list if x.source_type == 'water']
    light_to_temperature = [x for x in output_list if x.source_type == 'light']
    temperature_to_humidity = [x for x in output_list if x.source_type == 'temperature']
    humidity_to_location = [x for x in output_list if x.source_type == 'humidity']

    return [seed_to_soil + soil_to_fertilizer + fertilizer_to_water + water_to_light
            + light_to_temperature + temperature_to_humidity + humidity_to_location][0]
    




if __name__ == '__main__':
    main()

    