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

with open ('./input.txt') as file:
    FRESH_INGREDIENTS, INGREDIENTS = parse_input(file)
    print(count_fresh())