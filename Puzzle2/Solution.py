import math

# invalid ID's are where the ENTIRE ID is made of ONLY a sequence repeated twice
# 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

with open("Input.txt", "r") as file:
    input_data = file.read()
ranges = input_data.split(",")

# example ranges: 11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659, 824824821-824824827,2121212118-2121212124
# ranges = ["11-22"] # has two invalid IDs, 11 and 22.
# ranges = ["95-115"] # has one invalid ID, 99.
# ranges = ["998-1012"] # has one invalid ID, 1010.
# ranges = ["1188511880-1188511890"] # has one invalid ID, 1188511885.
# ranges = ["222220-222224"] # has one invalid ID, 222222.
# ranges = ["1698522-1698528"] # contains no invalid IDs.
# ranges = ["446443-446449"] # has one invalid ID, 446446.
# ranges = ["38593856-38593862"] # has one invalid ID, 38593859.
# The rest of the ranges contain no invalid IDs.
# ranges = ["824824821-824824827"]
# ranges = ["11-22","95-115"]
# ranges = ["11-22","95-115","824824821-824824827"]
# ranges = ["3636336362-3636336364"]

def getRepeatLength(currentId, exactlyOneRepeat):
    if(exactlyOneRepeat):
        if(len(str(currentId)) % 2 != 0):
            return 0
        return int(len(str(currentId)) / 2)
    else:
        firstNum = str(currentId)[0]
        halfway = math.floor(len(str(currentId)) / 2) # 3 -> 2, 2 -> 1
        matchFound = False
        repeatLength = 0
        for j in range(0,halfway):
            if str(currentId)[j+1] == firstNum:
                matchFound = True
                repeatLength = j + 1
                if(len(str(currentId)) % repeatLength != 0):
                    matchFound = False
                    repeatLength = 0
        return repeatLength

def checkInvalid(currentId, repeatLength):
    result = list(range(0, len(str(currentId)), repeatLength))
    for j in range(repeatLength):
        checks = list(range(j, len(str(currentId)), repeatLength))
        for check in checks:
            if str(currentId)[j] != str(currentId)[check]:
                return False
    return True

def sumIds(ranges, oneRepeatOnly):
    invalidIds = []
    for r in ranges:
        rangeMin = int(r.split("-")[0])
        rangeMax = int(r.split("-")[1])

        for i in range(rangeMin, rangeMax+1):
            repeatLength = getRepeatLength(i, oneRepeatOnly)
            if(repeatLength == 0):
                continue
            isInvalid = False
            if(oneRepeatOnly):
                isInvalid = checkInvalid(i, repeatLength)
            else:
                isInvalid = checkInvalid(i, repeatLength)
            if isInvalid:
                invalidIds.append(i)
    return sum(invalidIds)

sumIds1 = sumIds(ranges, True)
print(sumIds1)
sumIds2 = sumIds(ranges, False)
print(sumIds2)