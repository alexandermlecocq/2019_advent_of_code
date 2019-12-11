input_file = open('input.txt', 'r')
program = [int(n) for n in input_file.read().split(",")]

ex = 0
opcode = program[ex]
while opcode != 99:
    if opcode == 1:
        result = program[program[ex + 1]] + program[program[ex + 2]]
        program[program[ex + 3]] = result
    if opcode == 2:
        result = program[program[ex + 1]] * program[program[ex + 2]]
        program[program[ex + 3]] = result
    ex += 4
    opcode = program[ex]


print(program)