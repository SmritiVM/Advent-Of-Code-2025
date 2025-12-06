def parse_input(file):
    return file.read().split(',')

def is_valid(id: str):
    length = len(id)
    if length % 2: return True
    right, left = id[:length//2], id[length//2:]
    if right == left: return False
    return True

def find_invalid_id_sum(ranges: list):
    total = 0
    for current_range in ranges:
        start, end = current_range.split('-')
        for id in range(int(start), int(end) + 1):
            if not is_valid(str(id)): total += id
    return total

with open('./input.txt') as file:
   ranges = parse_input(file) 
   print(find_invalid_id_sum(ranges))