def parse_input(file):
    fresh_ingredients = list() # [[start, end], [start, end]]
    ingredients = list()
    for line in file:
        if line == '\n':
            break
        fresh_ingredients.append(list(map(int, line.split('-'))))

    for line in file:
        ingredients.append(int(line.strip()))

    return fresh_ingredients, ingredients

def count_fresh():
    count = 0
    for ingredient in INGREDIENTS:
        for start, end in FRESH_INGREDIENTS:
            if start <= ingredient <= end:
                count += 1
                break

    return count


# Find total non overlapping distinct subsets
def merge_intervals(intervals):
    if not intervals: return []

    intervals.sort()
    merged = [intervals[0]]

    for current in intervals[1:]:
        prev_start, prev_end = merged[-1]
        curr_start, curr_end = current
        if curr_start <= prev_end: # overlapping subsets
            merged[-1][1] = max(prev_end, curr_end) # prev interval is extended
        else:
            merged.append(current)
    return merged

def total_possible_fresh():
    total = 0
    for start, end in MERGED_FRESH_INGREDIENTS:
        total += (end - start + 1)
    return total

with open ('./input.txt') as file:
    FRESH_INGREDIENTS, INGREDIENTS = parse_input(file)
    print(count_fresh())
    MERGED_FRESH_INGREDIENTS = merge_intervals(FRESH_INGREDIENTS)
    # print(MERGED_FRESH_INGREDIENTS)
    print(total_possible_fresh())
