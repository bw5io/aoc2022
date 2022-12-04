from aoc_lib import fileToArray
day1list=fileToArray("day1-1.txt", True)
print(day1list)
currentSum, calorieList = 0, []
for i in day1list:
    if i!="":
        currentSum+=i
    else:
        calorieList.append(currentSum)
        currentSum = 0
calorieList.sort()

print (calorieList[-1]+calorieList[-2]+calorieList[-3])
    