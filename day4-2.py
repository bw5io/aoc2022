from aoc_lib import file_to_array

result=0

day4input = file_to_array("day4-1.txt")
print(day4input)
index=0
while day4input[index]!="":
    thisLine = day4input[index].split(",")
    left = thisLine[0].split("-")
    right = thisLine[1].split("-")
    if (int(left[0])>=int(right[0]) and int(left[0])<=int(right[1])) or (int(left[0])<=int(right[0]) and int(left[1])>=int(right[0])):
        print(left,right)
        result+=1
    index+=1
print(result)