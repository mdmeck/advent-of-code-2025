# dial lock
# 0 through 99 in order
# dial starts at 50
# ex: starting at 11, R8 would move right 8 spaces to 19

# The actual password is the number of times the dial is left
# pointing at 0 after any rotation in the sequence.

# input
# https://adventofcode.com/2025/day/1/input

with open("Input.txt", "r") as file:
    input_data = file.read()

location = 50
zeroCountPart1 = 0
zeroCountPart2 = 0

spins = input_data.split("\n")
#spins = spins[:200]
#spins = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]


for spin in spins:

    direction = spin[0]
    totalDistance = int(spin[1:])
    distance = totalDistance % 100
    totalSpins = int((totalDistance - distance) / 100)
    startingLocation = location

    zeroCountPart2 += totalSpins

    if direction == "R":
        location += distance
    else:
        location -= distance

    if location < 0:
        location += 100
        if location != 0 and startingLocation != 0: zeroCountPart2 += 1
    if location > 99:
        location -= 100
        if location != 0 and startingLocation != 0: zeroCountPart2 += 1
    location = abs(location)

    if location == 0:
        zeroCountPart1 += 1
        zeroCountPart2 += 1

    #print(location, totalSpins, zeroCountPart1, zeroCountPart2, spin)

print(zeroCountPart1, zeroCountPart2)