input_file = open('input.txt', 'r')
total_fuel = 0
for module_mass in input_file:
    fuel = int(module_mass) // 3 - 2
    total_fuel += fuel
print(total_fuel)