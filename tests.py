symbol_list = ['*', '/', '-', '=', '&', '+', '#', '@', '$', '%']

print(any([(x in symbol_list) for x in "as@sdf"]))

print(len(symbol_list) - 1)