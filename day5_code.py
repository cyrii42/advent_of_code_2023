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
from dataclasses import dataclass, field
from pprint import pprint

from day5_data_ingestion import (process_maps, process_seeds,
                                 process_test_maps, process_test_seeds)

SOURCE_ORDER_LIST = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity']

@dataclass
class MapRow():
    destination_range_start: int = field(repr=False)
    source_range_start: int = field(repr=False)
    range_length: int = field(repr=False)
    destination_range: (int, int) = field(init=False)
    source_range: (int, int) = field(init=False)

    def __post_init__(self) -> None:
        self.destination_range = self.calculate_destination_range()
        self.source_range = self.calculate_source_range()
        
    def calculate_destination_range(self) -> (int, int):
        destination_range_end = self.destination_range_start - 1 + self.range_length
        return (self.destination_range_start, destination_range_end)

    def calculate_source_range(self) -> (int, int):
        source_range_end = self.source_range_start - 1 + self.range_length
        return (self.source_range_start, source_range_end)

    
@dataclass
class Map():
    source_type: str
    destination_type: str
    rows: list[MapRow] = field(repr=False)
    range_dict_list: list[dict] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.range_dict_list = self.construct_range_dict_list()

    def construct_range_dict_list(self) -> list[dict]:
        output_list = []
        for row in self.rows:
            output_list.append({'source_range': row.source_range, 'destination_range': row.destination_range})
        return output_list
        

@dataclass
class Seed():
    seed_num: int
    maps_list: list[Map] = field(repr=False)
    maps_dict: dict = field(init=False, repr=False)
    location_num: int = field(init=False)

    def __post_init__(self):
        self.maps_dict = {map.source_type: map for map in self.maps_list}
        self.location_num = self.find_location_num()        

    def find_location_num(self) -> int:
        num_to_test = self.seed_num
        for source_type in SOURCE_ORDER_LIST:
            current_map = self.maps_dict[source_type]
            for range_dict in current_map.range_dict_list:
                if num_to_test in range(range_dict['source_range'][0], range_dict['source_range'][1]+1):
                    old_num_to_test = num_to_test
                    num_to_test = range_dict['destination_range'][0] + (num_to_test - range_dict['source_range'][0])
                    # print(f"Seed #{self.seed_num}:  Paired {current_map.source_type} {old_num_to_test} with {current_map.destination_type} {num_to_test}")
                    break
        return num_to_test

    # def find_location_num_part_two(self) -> int:
    #     num_to_test = self.seed_num
    #     chunk_size = 10000
    #     ....

    # @staticmethod
    # def __test_seed_num_against_subrange(num_to_test: int, subrange: range) -> int:
    #     if num_to_test in subrange:
    #         num_to_test = range_dict['destination_range'][0] + (num_to_test - range_dict['source_range'][0])
    #         # print(f"Seed #{self.seed_num}:  Paired {current_map.source_type} {old_num_to_test} with {current_map.destination_type} {num_to_test}")
    #         # break
            

        
        # if num_to_test in range(range_dict['source_range'][0], range_dict['source_range'][1]+1):
        #     return range_dict['destination_range'][0] + (num_to_test - range_dict['source_range'][0])
        # else:
        #     return num_to_test


def find_answer_for_part_two(raw_seeds_list: list[int]) -> int:
    maps_list = create_map_objects(process_maps())

    range_start_nums = [n for i, n in enumerate(raw_seeds_list) if (i % 2 == 0)]
    range_length_nums = [n for i, n in enumerate(raw_seeds_list) if (i % 2 != 0)]
    seed_num_pairs = [(range_start_nums[i], range_length_nums[i]) for i, x in enumerate(range_start_nums)]

    # Find total number of seeds and print to console
    total_seeds_num = 0
    for pair in seed_num_pairs:
        total_seeds_num += len(range(pair[0], pair[0]+pair[1]))
    print(f"Total # of seeds in Part 2:  {total_seeds_num:,}")

    # Compare each new seed to the lowest location number found so far, and only keep the lowest. 
    lowest_location_num = 0
    chunk_size = 100000
    total_progress = 0
    for i, pair in enumerate(seed_num_pairs):
        for n, seed_num in enumerate(range(pair[0], pair[0]+pair[1])):
            seed = Seed(seed_num, maps_list)
            if i == 0 and n == 0:
                print(f"Processing Seed #{total_progress+n:,} of {total_seeds_num:,} ({(((total_progress+n)/total_seeds_num)*100):.2f}%).",
                      f"Current lowest location #:  {lowest_location_num}")
                lowest_location_num = seed.location_num
            else:
                if (n % chunk_size == 0):
                    print(f"Processing Seed #{total_progress+n:,} of {total_seeds_num:,} ({(((total_progress+n)/total_seeds_num)*100):.2f}%).",
                          f"Current lowest location #:  {lowest_location_num}")
                lowest_location_num = min(lowest_location_num, seed.location_num)
        total_progress += i+1
    return lowest_location_num

    # output_list = []
    # for pair in seed_num_pairs:
    #     output_list += [Seed(x, maps_list) for x in range(pair[0], pair[0]+pair[1])]

    # return output_list


def part_two():
    raw_seeds_list = process_seeds()

    part_two_answer = find_answer_for_part_two(raw_seeds_list)
    print(f"PART #2 ANSWER:  {part_two_answer}")





def part_one():
    maps_list = create_map_objects(process_maps())
    seeds_list = [Seed(x, maps_list) for x in process_seeds()]
    
    lowest_location_num = min([seed.location_num for seed in seeds_list])
    print(f"PART #1 ANSWER:  {lowest_location_num}")  # Part 1 answer:  457535844
    

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
    


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()

    