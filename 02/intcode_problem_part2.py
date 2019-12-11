for verb in range(0, 100):
    for noun in range (0, 100):
        input_file = open('input.txt', 'r')
        program = [int(n) for n in input_file.read().split(",")]
        program[1] = noun
        program[2] = verb
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
        if program[0] == 19690720:
            break
    if program[0] == 19690720:
        break


print(program)