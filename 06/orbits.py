class body_class:
    def __init__(self, name):
        self.name = name
        self.orbiters = []
        self.total_orbits = 0

COM = body_class('COM')
bodies = [COM]


def find_body(body_name):
    for body in bodies:
        if body_name == body.name:
            return body

def count_orbiters(orbitee):
    for body in orbitee.orbiters:
        body.total_orbits = orbitee.total_orbits + 1
        count_orbiters(body)

# Create Bodies List
input_file = open('input.txt', 'r')
for orbit in input_file.read().splitlines():
    current_bodies = orbit.split(')')
    new_body = body_class(current_bodies[1])
    bodies.append(new_body)

print(f'Number of bodies: {len(bodies)}')

# Populate orbiter lists
input_file = open('input.txt', 'r')
for orbit in input_file.read().splitlines():
    current_bodies = orbit.split(')')
    orbitee = find_body(current_bodies[0])
    orbiter = find_body(current_bodies[1])
    orbitee.orbiters.append(orbiter)
    print(f'{orbitee.name} : {len(orbitee.orbiters)}')


count_orbiters(find_body('COM'))

total_map_orbits = 0

for body in bodies:
    print(f'{body.name} : {len(body.orbiters)} , {body.total_orbits}')
    total_map_orbits += body.total_orbits

print(total_map_orbits)