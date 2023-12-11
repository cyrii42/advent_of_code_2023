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

def create_subranges(seed_range_length: int) -> list[range]:
    chunk_size = 10000
    num_subranges = ((seed_range_length // chunk_size) + 1) if ((seed_range_length % chunk_size) != 0) else (seed_range_length // chunk_size)
    
    output_list = []
    for n in range(num_subranges):
        output_list.append(range(chunk_size*n, min(seed_range_length, chunk_size*(n+1))))
        
    return output_list

print(create_subranges(350401))