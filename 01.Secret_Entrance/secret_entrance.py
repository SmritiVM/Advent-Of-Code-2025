
OFFSET = {'L':-1, 'R':1}

    
def find_zero_landings(dial_position: int, instructions) -> int:
    destination_zero, intermediate_zero = 0, 0
    for line in instructions:
        direction, value = line[0], int(line[1:])
        current_offset = dial_position + OFFSET[direction] * value

        if current_offset <= 0:
            intermediate_zero += abs(current_offset // 100)
            if current_offset % 100 == 0: intermediate_zero += 1
            if dial_position == 0: intermediate_zero -= 1
        
        elif current_offset >= 100:
            intermediate_zero += current_offset // 100

        dial_position = current_offset % 100
        if dial_position == 0: 
            destination_zero += 1
    return destination_zero, intermediate_zero
    

with open('./input.txt') as instructions:
    print(find_zero_landings(50, instructions))

