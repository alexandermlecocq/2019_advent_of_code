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

def check_parameter (program, parameter, mode):
    if mode == '0':
        output = program[parameter]
    elif mode == '1':
        output = parameter
    else:
        print ('Error with mode')
        output = 0
    return int(output)

def execute_program (program, phase_setting, input_value):
    entered_phase_setting = False
    ex = 0
    instructions = process_instructions(program[ex])
    opcode = instructions[0]
    while opcode != '99':
        if opcode == '01':
            result = check_parameter(program, program[ex + 1], instructions[1]) + check_parameter(program, program[ex + 2], instructions[2])
            program[program[ex + 3]] = result
            ex += 4
        elif opcode == '02':
            result = check_parameter(program, program[ex + 1], instructions[1]) * check_parameter(program, program[ex + 2], instructions[2])
            program[program[ex + 3]] = result
            ex += 4
        elif opcode == '03':
            if entered_phase_setting:
                result = input_value
            else:
                result = phase_setting
                entered_phase_setting = True
            program[program[ex + 1]] = result
            ex += 2
        elif opcode == '04':
            result = check_parameter(program, program[ex + 1], instructions[1])
            output_value = result
            ex += 2
        elif opcode == '05':
            result = check_parameter(program, program[ex + 1], instructions[1])
            if result != 0:
                ex = check_parameter(program, program[ex + 2], instructions[2])
            else:
                ex += 3
        elif opcode == '06':
            result = check_parameter(program, program[ex + 1], instructions[1])
            if result == 0:
                ex = check_parameter(program, program[ex + 2], instructions[2])
            else:
                ex += 3
        elif opcode == '07':
            result = check_parameter(program, program[ex + 1], instructions[1]) - check_parameter(program, program[ex + 2], instructions[2])
            if result < 0:
                program[program[ex + 3]] = '1'
                ex += 4
            else:
                program[program[ex + 3]] = '0'
                ex += 4
        elif opcode == '08':
            result = check_parameter(program, program[ex + 1], instructions[1]) - check_parameter(program, program[ex + 2], instructions[2])
            if result == 0:
                program[program[ex + 3]] = '1'
                ex += 4
            else:
                program[program[ex + 3]] = '0'
                ex += 4
                
        # print(f'{ex}, {instructions}, {result}')

        instructions = process_instructions(program[ex])
        opcode = instructions[0]
    return output_value



input_file = open('input.txt', 'r')
original_program = [int(n) for n in input_file.read().split(",")]

from itertools import permutations 
phase_setting_permutations = list(permutations(range(0, 5)))

highest_output = 0
for phase_setting_permutation in phase_setting_permutations:
    input_value = 0
    for phase_setting in phase_setting_permutation:
        output_value = execute_program(original_program, phase_setting, input_value)
        input_value = output_value
    
    if output_value > highest_output:
        highest_output = output_value
        print(f'{phase_setting_permutation} : {output_value}')