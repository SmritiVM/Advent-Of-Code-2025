def parse_input(file):
    batteries = list()
    for line in file:
        batteries.append(line.strip())
    return batteries

def find_largest_power(battery: str, start_index: int, end_index: int):
    largest, largest_index = '-1', start_index
    for index, num in enumerate(battery[start_index:end_index]):
        if num > largest:
            largest = num
            largest_index = index
    return largest, largest_index

def max_joltage(battery: str, limit: int):
    n = len(battery)
    joltage = ''
    start_index = 0
    for offset in range(limit, 0, -1):
        power, index = find_largest_power(battery, start_index, n - offset + 1)
        joltage += power
        start_index += (index + 1)
        # print(power, index, end = ' ')
    return int(joltage)

def find_largest_joltage(batteries: list, limit: int):
    total = 0
    for battery in batteries:
        # print(max_joltage(battery, limit))
        total += max_joltage(battery, limit)
    return total
        
with open('./input.txt') as file:
    batteries = parse_input(file)
    print(find_largest_joltage(batteries, limit=2))
    print(find_largest_joltage(batteries, limit=12))