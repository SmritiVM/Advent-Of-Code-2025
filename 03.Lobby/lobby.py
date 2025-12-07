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

def max_joltage(battery: str):
    n = len(battery)
    largest_power, largest_power_index = find_largest_power(battery, 0, n - 1) # finding the largest before the end
    second_largest_power, _ = find_largest_power(battery, largest_power_index + 1, n) # find the largest after the first largest number. we don't need the index here
    return int(largest_power + second_largest_power)

def find_largest_joltage(batteries: list):
    total = 0
    for battery in batteries:
        # print(max_joltage(battery))
        total += max_joltage(battery)
    return total
        
with open('./input.txt') as file:
    batteries = parse_input(file)
    print(find_largest_joltage(batteries))