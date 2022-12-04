from aoc_lib import fileToArray

day3list=fileToArray("day3-1.txt", False)

prioritySum=0

for i in day3list:
    if i=="":
        break
    ilist=list(i)
    halfPoint=len(ilist)//2
    firstHalf=set(ilist[0:halfPoint])
    secondHalf=set(ilist[halfPoint:])
    print(len(firstHalf),len(secondHalf))
    resultChar=list(firstHalf.intersection(secondHalf))[0]
    result=ord(resultChar)
    print(resultChar)
    if result>=97:
        result-=96
    else:
        result-=(64-26)
    prioritySum+=result

print(prioritySum)