def contains_double_but_no_more (number):
    string_num = str(number) + 'X'
    digit = 'N'
    digit_count = 1
    for n in range(1, 7):
        if digit != string_num[n]:
            if digit_count == 2:
                return True
            else:
                digit_count = 1
        if (string_num[n - 1] == string_num[n]):
            digit = string_num[n]
            digit_count += 1
    return False

start = '153517'
final = '630395'
# start = '155555'
# final = '155999'
valid_passwords = 0


for d1 in range(int(start[0]), int(final[0]) + 1):
    for d2 in range(d1, 10):
        for d3 in range(d2, 10):
            for d4 in range(d3, 10):
                for d5 in range(d4, 10):
                    for d6 in range(d5, 10):
                        password = int(str(d1) + str(d2) +str(d3) + str(d4) +str(d5) +str(d6))
                        if (password >= int(start)) & (password <= int(final)):
                            if contains_double_but_no_more(password):
                                valid_passwords += 1
                                print(f'GOOD: {password}')
                            else:
                                print(f'BAD: {password}')

print('Final Count: ' + str(valid_passwords))