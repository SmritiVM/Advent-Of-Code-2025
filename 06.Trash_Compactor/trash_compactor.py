from functools import reduce
from collections import defaultdict

def parse_input(file):
    # N number of lines
    # last line is operations
    operands = list()
    operators = list()
    for line in file:
        if line[0] in ['*', '+']:
            operators = line.strip().split()
        else:
            operands.append(list(map(int, line.strip().split())))
    return operands, operators

def parse_input_2(file):
    operands = defaultdict(list)
    operator_positions = defaultdict(str)
    for line in file:
        for index, char in enumerate(line):
            if char.isdigit():
                operands[index].append(char)
            if char in ['+', '*']:
                operator_positions[index] = char
    max_index = 0
    for key in operands:
        operands[key] = int(''.join(operands[key]))
        max_index = max(max_index, key)
    operator_positions[max_index + 2] = None 
    return operands, operator_positions
    

def operator_function(operator: str):
    if operator == '+': 
        return lambda x, y: x + y
    if operator == '*':
        return lambda x, y: x * y
    return lambda x: x

def solve_worksheet(operands, operators):
    total = 0
    for index, operand in enumerate(operands[0]):
        problem = [operand]
        for operands in operands[1:]:
            problem.append(operands[index])
        total += reduce(operator_function(operators[index]), problem)
    return total

def solve_worksheet_r_l(operands, operators):
    total = 0
    prev_position = 0
    for position in operators:
        if position == 0: continue
        problem = list()
        for x in range(prev_position, position - 1):
            problem.append(operands[x])
        total += reduce(operator_function(operators[prev_position]), problem)
        prev_position = position
    return total


with open ('./input.txt') as file:
    # operands, operators = parse_input(file)
    # print(solve_worksheet(operands, operators))
    operands, operators = parse_input_2(file)
    print(solve_worksheet_r_l(operands, operators))