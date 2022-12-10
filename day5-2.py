from aoc_lib import file_to_array_no_strip

day5input = file_to_array_no_strip("day5-1.txt")

stack = {}
lineIndex = 0
rowIndex = 1

while not day5input[lineIndex][1].isdigit():
    # print(day5input[lineIndex])
    while (rowIndex-1)*4+1 < len(day5input[lineIndex]):
        # print(stack)
        if day5input[lineIndex][(rowIndex-1)*4+1]!=" ":
            if rowIndex in stack:
                stack[rowIndex].insert(0,day5input[lineIndex][(rowIndex-1)*4+1])
            else:
                stack[rowIndex]=[day5input[lineIndex][(rowIndex-1)*4+1]]
        rowIndex+=1
    lineIndex+=1
    rowIndex=1

lineIndex+=2
print(stack)


while day5input[lineIndex]!="":
    thisline=day5input[lineIndex].strip().split(" ")
    print(thisline)
    src = stack[int(thisline[3])]
    print(src)
    newSrc=src[0:len(src)-int(thisline[1])]
    newTgt=src[len(src)-int(thisline[1]):]
    stack[int(thisline[5])]+=newTgt
    stack[int(thisline[3])]=newSrc
    lineIndex+=1

print(stack)

i=1
result=""
while i in stack:
    result+=stack[i][-1]
    i+=1
print(result)