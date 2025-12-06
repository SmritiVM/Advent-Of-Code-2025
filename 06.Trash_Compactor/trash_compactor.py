from functools import reduce

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

def operator_function(operator: str):
    if operator == '+': 
        return lambda x, y: x + y
    if operator == '*':
        return lambda x, y: x * y

def solve_worksheet():
    total = 0
    for index, operand in enumerate(OPERANDS[0]):
        problem = [operand]
        for operands in OPERANDS[1:]:
            problem.append(operands[index])
        total += reduce(operator_function(OPERATORS[index]), problem)
    return total

with open ('./input.txt') as file:
    OPERANDS, OPERATORS = parse_input(file)
    # print(OPERANDS, OPERATORS)
    print(solve_worksheet())