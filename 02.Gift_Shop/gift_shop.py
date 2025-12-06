def parse_input(file):
    return file.read().split(',')

def is_valid(id: str):
    length = len(id)
    if length % 2: return True
    right, left = id[:length//2], id[length//2:]
    if right == left: return False
    return True

def is_valid_2(id: str):
    length = len(id)
    for chunk_size in range(1, length // 2 + 1):
        chunks = [id[i:i + chunk_size] for i in range(0, length, chunk_size)]
        if all([chunk == chunks[0] for chunk in chunks]): return False
    return True


def find_invalid_id_sum(ranges: list, valid_id_function):
    total = 0
    for current_range in ranges:
        start, end = current_range.split('-')
        for id in range(int(start), int(end) + 1):
            if not valid_id_function(str(id)): total += id
    return total

with open('./input.txt') as file:
   ranges = parse_input(file) 
   print(find_invalid_id_sum(ranges, is_valid))
   print(find_invalid_id_sum(ranges, is_valid_2))