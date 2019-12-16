def process_instructions (instruction):
    instruction = str(instruction)
    if len(instruction) > 1:
        opcode = instruction[-2:]
        output = [opcode]
    else:
        opcode = '0' + instruction
        output = [opcode]
    for n in range (-3, -6, -1):
        if abs(n) > len(instruction):
            output.append('0')
        else:
            output.append(instruction[n])
    return output

def check_parameter (parameter, mode):
    if mode == '0':
        output = program[parameter]
    elif mode == '1':
        output = parameter
    else:
        print ('Error with mode')
        output = 0
    return int(output)


input_file = open('input.txt', 'r')
program = [int(n) for n in input_file.read().split(",")]

ex = 0
instructions = process_instructions(program[ex])
opcode = instructions[0]
while opcode != '99':
    if opcode == '01':
        result = check_parameter(program[ex + 1], instructions[1]) + check_parameter(program[ex + 2], instructions[2])
        program[program[ex + 3]] = result
        skip_forward = 4
    elif opcode == '02':
        result = check_parameter(program[ex + 1], instructions[1]) * check_parameter(program[ex + 2], instructions[2])
        program[program[ex + 3]] = result
        skip_forward = 4
    elif opcode == '03':
        result = input('Enter input: ')
        program[program[ex + 1]] = result
        skip_forward = 2
    elif opcode == '04':
        result = check_parameter(program[ex + 1], instructions[1])
        print(f'Ouput is {result}')
        skip_forward = 2

    print(f'{ex}, {instructions}, {result}')

    ex += skip_forward
    instructions = process_instructions(program[ex])
    opcode = instructions[0]
