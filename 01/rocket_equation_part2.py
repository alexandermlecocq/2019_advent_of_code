input_file = open('input.txt', 'r')
total_fuel = 0
for module_mass in input_file:
    fuel = int(module_mass) // 3 - 2

    total_module_fuel = 0
    fuel_for_fuel = 0
    while fuel > 0:
        total_module_fuel += fuel
        fuel_for_fuel = fuel // 3 - 2
        fuel = fuel_for_fuel
    total_fuel += total_module_fuel


print(total_fuel)