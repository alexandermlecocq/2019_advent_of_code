input_file = open('input.txt', 'r')

def contains_double (number):
    string_num = str(number)
    for n in range(1, 5):
        if string_num[n - 1] == string_num[n]:
            return True
    return False

start = '153517'
final = '630395'
valid_passwords = 0

for d1 in range(int(start[0]), int(final[0])):
    for d2 in range(d1, 10):
        for d3 in range(d2, 10):
            for d4 in range(d3, 10):
                for d5 in range(d4, 10):
                    for d6 in range(d5, 10):
                        password = int(str(d1) + str(d2) +str(d3) + str(d4) +str(d5) +str(d6))
                        if (password >= int(start)) & (password <= int(final)):
                            if contains_double(password):
                                valid_passwords += 1

print('Final Count: ' + str(valid_passwords))