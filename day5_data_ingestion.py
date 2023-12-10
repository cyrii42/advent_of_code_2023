from day5_code import Map, MapRow
from day5_input import (fertilizer_to_water_map_list,
                        humidity_to_location_map_list,
                        light_to_temperature_map_list, seed_to_soil_map_list,
                        soil_to_fertilizer_map_list,
                        temperature_to_humidity_map_list,
                        water_to_light_map_list)


def convert_map_list_to_map(map_list: list) -> Map:
    output_list = []
    for row in map_list:
        split_row = row.split(sep=' ')
        map_row_object = MapRow(split_row[0], split_row[1], split_row[2])
        output_list.append(map_row_object)
    return Map(output_list)

fertilizer_to_water = convert_map_list_to_map(fertilizer_to_water_map_list)
humidity_to_location = convert_map_list_to_map(humidity_to_location_map_list)
light_to_temperature = convert_map_list_to_map(light_to_temperature_map_list)
seed_to_soil = convert_map_list_to_map(seed_to_soil_map_list)
soil_to_fertilizer = convert_map_list_to_map(soil_to_fertilizer_map_list)
temperature_to_humidity = convert_map_list_to_map(temperature_to_humidity_map_list)
water_to_light = convert_map_list_to_map(water_to_light_map_list)