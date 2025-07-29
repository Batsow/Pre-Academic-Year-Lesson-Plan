#Ask user for input and then output the energy equivalent of that mass using einstein equation E=mc^2
mass = int(input()) #in kilograms
speed_of_light = 300000000  # in meters per second
energy = mass * (speed_of_light ** 2) # E = mc^2
print(energy)