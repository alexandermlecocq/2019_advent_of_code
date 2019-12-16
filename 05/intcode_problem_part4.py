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

# input_string = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
# program = [int(n) for n in input_string.split(",")]

ex = 0
instructions = process_instructions(program[ex])
opcode = instructions[0]
while opcode != '99':
    if opcode == '01':
        result = check_parameter(program[ex + 1], instructions[1]) + check_parameter(program[ex + 2], instructions[2])
        program[program[ex + 3]] = result
        ex += 4
    elif opcode == '02':
        result = check_parameter(program[ex + 1], instructions[1]) * check_parameter(program[ex + 2], instructions[2])
        program[program[ex + 3]] = result
        ex += 4
    elif opcode == '03':
        result = input('Enter input: ')
        program[program[ex + 1]] = result
        ex += 2
    elif opcode == '04':
        result = check_parameter(program[ex + 1], instructions[1])
        print(f'Ouput is {result}')
        ex += 2
    elif opcode == '05':
        result = check_parameter(program[ex + 1], instructions[1])
        if result != 0:
            ex = check_parameter(program[ex + 2], instructions[2])
        else:
            ex += 3
    elif opcode == '06':
        result = check_parameter(program[ex + 1], instructions[1])
        if result == 0:
            ex = check_parameter(program[ex + 2], instructions[2])
        else:
            ex += 3
    elif opcode == '07':
        result = check_parameter(program[ex + 1], instructions[1]) - check_parameter(program[ex + 2], instructions[2])
        if result < 0:
            program[program[ex + 3]] = '1'
            ex += 4
        else:
            program[program[ex + 3]] = '0'
            ex += 4
    elif opcode == '08':
        result = check_parameter(program[ex + 1], instructions[1]) - check_parameter(program[ex + 2], instructions[2])
        if result == 0:
            program[program[ex + 3]] = '1'
            ex += 4
        else:
            program[program[ex + 3]] = '0'
            ex += 4


    print(f'{ex}, {instructions}, {result}')

    instructions = process_instructions(program[ex])
    opcode = instructions[0]
