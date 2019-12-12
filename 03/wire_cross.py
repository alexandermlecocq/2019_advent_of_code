class line_class:
    horizontal = False
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

def iswithin (a, b, c):
    if (c >= a) & (c <= b):
        return True
    elif (c >= b) & (c <= a):
        return True
    else:
        return False

def intersect (line1, line2):
    if line1.horizontal != line2.horizontal: # Lines are not parallel
        if line1.horizontal:
            if iswithin (line2.y1, line2.y2, line1.y1): 
                if iswithin (line1.x1, line1.x2, line2.x1):
                    return [line2.x1, line1.y1]
        else:
            if iswithin (line1.y1, line1.y2, line2.y1):
                if iswithin (line2.x1, line2.x2, line1.x1):
                    return [line1.x1, line2.y1]

    return [False, False]

def create_line (instruction, x1, y1):
    new_line = line_class()
    new_line.x1 = x1
    new_line.y1 = y1
    direction = instruction[0]
    length = int(instruction[1:])
    if direction == 'U':
        new_line.horizontal = False
        new_line.x2 = x1
        new_line.y2 = y1 + length
    elif direction == 'D':
        new_line.horizontal = False
        new_line.x2 = x1
        new_line.y2 = y1 - length
    elif direction == 'L':
        new_line.horizontal = True
        new_line.x2 = x1 + length
        new_line.y2 = y1
    elif direction == 'R':
        new_line.horizontal = True
        new_line.x2 = x1 - length
        new_line.y2 = y1
    return new_line

def print_lines (line):
    print([line.horizontal, [line.x1, line.y1], [line.x2, line.y2]])

input_file = open('input.txt', 'r')
wire_lines = []
wire_number = 0
for wire_instructions in input_file.readlines():
    wire_lines.append([])
    start_x = 0
    start_y = 0
    for instruction in wire_instructions.split(","):
        line = create_line(instruction, start_x, start_y)
        wire_lines[wire_number].append(line)
        start_x = line.x2
        start_y = line.y2
    wire_number += 1

lowest_distance = -1
for wire1_line in wire_lines[0]:
    for wire2_line in wire_lines[1]:
        intersection = intersect(wire1_line, wire2_line)
        if intersection != [False, False]:
            Manhattan_distance = abs(intersection[0]) + abs(intersection[1])
            if lowest_distance == -1:
                lowest_distance = Manhattan_distance
            elif Manhattan_distance < lowest_distance:
                lowest_distance = Manhattan_distance


print(lowest_distance)