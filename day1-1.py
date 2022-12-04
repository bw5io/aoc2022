from aoc_lib import fileToArray
day1list=fileToArray("day1-1.txt", True)
print(day1list)
currentSum, currentMax = 0, 0
for i in day1list:
    if i!="":
        currentSum+=i
    else:
        currentMax = max(currentSum, currentMax)
        currentSum = 0
print (currentMax)
    