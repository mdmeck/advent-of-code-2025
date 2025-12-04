import math

testInput = "TestInput.txt"
fullInput = "Input.txt"
useTestInput = False
inputToUse = testInput if useTestInput else fullInput

with open(inputToUse, "r") as file:
    input_data = file.read()
banks = input_data.split("\n")

def getMaxJoltage(bank, batteries):
    joltages = [int(i) for i in str(bank)]

    maxJoltage = ''
    battery = batteries
    while battery > 0:
        joltagesForMax = joltages.copy()
        pop = battery - 1
        if pop != 0:
            del joltagesForMax[-pop:]
        highestJoltage = max(joltagesForMax)
        maxJoltage += str(highestJoltage)
        highestJoltagePosition = joltages.index(highestJoltage) + 1
        del joltages[:highestJoltagePosition]
        battery -= 1

    #print(bank, maxJoltage)
    return maxJoltage

sumJoltage = 0

#getMaxJoltage(811111111111119, 12)

for bank in banks:
    sumJoltage += int(getMaxJoltage(bank, 12))

print(sumJoltage)