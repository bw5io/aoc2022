from aoc_lib import file_to_array

day3list=file_to_array("day3-1.txt", False)

prioritySum=0
pointer=0

for i in range(0,len(day3list),3):
    if day3list[i]=="":
        break
    print(i)
    resultChar=list(set(day3list[i]).intersection(set(day3list[i+1]).intersection(day3list[i+2])))[0]
    result=ord(resultChar)
    print(resultChar)
    if result>=97:
        result-=96
    else:
        result-=(64-26)
    prioritySum+=result

print(prioritySum)